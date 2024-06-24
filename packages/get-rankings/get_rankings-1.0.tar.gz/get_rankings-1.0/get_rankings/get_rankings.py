#!/usr/bin/env python3

import logging
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm
import os
import sys
import datetime
from dateutil.parser import parse as parsedate
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import re
import shutil
from io import StringIO

from get_rankings.hash_cache import load_hash_caches, save_hash_caches, default_cache
from get_rankings.tools import levenshtein, download, get_in_ordered_list


def comp_lower(a, b):
    return isinstance(a, str) and isinstance(b, str) and a.lower() == b.lower()


def get_dblp(url, cache=True, cache_dir=None):
    if cache_dir is None:
        cache_dir = default_cache()
    _, target = url.split("//")
    filename = "%s/%s" % (cache_dir, target.replace("/", "_"))
    os.makedirs(cache_dir, exist_ok=True)
    if not os.path.exists(filename) or not cache:
        data = download(url, filename)
    else:
        with open(filename, "rb") as file:
            data = file.read()

    soup = BeautifulSoup(data, "html.parser")

    articles = soup.find_all("li", class_="entry")

    res = []
    for a in articles:
        if "inproceedings" in a["class"] or "article" in a["class"]:
            name = (
                a.find("span", itemprop="isPartOf").find("span", itemprop="name").text
            )
            year = a.find("span", itemprop="datePublished").text
            venue, second_name, _ = a["id"].split("/")
            res.append([venue, name, second_name, year])
    return soup.title.text, res


def get_core_year(year):
    if year >= 2023:
        return "CORE2023"
    if year >= 2021:
        return "CORE2021"
    if year >= 2020:
        return "CORE2020"
    if year >= 2018:
        return "CORE2018"
    if year >= 2017:
        return "CORE2017"
    if year >= 2014:
        return "CORE2014"
    if year >= 2013:
        return "CORE2013"
    if year >= 2010:
        return "ERA2010"
    return "CORE2008"


def get_core_rank(name, year):

    source = get_core_year(int(year))
    url = "http://portal.core.edu.au/conf-ranks/?search=%s&by=all&source=%s&page=1" % (
        name,
        source,
    )

    data = download(url)
    cc_soup = BeautifulSoup(data, "html.parser")
    table = cc_soup.find_all("table")
    if len(table) == 0:
        return None
    df = pd.read_html(StringIO(str(table)))[0]

    for index, row in df.iterrows():
        # print(name, year, '    ', row.Title, row.Acronym, row.Rank)
        if comp_lower(row.Title, name) or comp_lower(row.Acronym, name):
            return row.Rank, row.Title, row.Acronym
    return None


class Sjr:
    def __init__(self):
        self.ranking_caches = load_hash_caches("sjr")

    def close(self):
        save_hash_caches(self.ranking_caches, "sjr")

    def get_issn(self, acronym):
        data = download("https://dblp.org/db/journals/%s/index.html" % acronym)
        soup = BeautifulSoup(data, "html.parser")
        full_name = soup.find("h1").text
        try:
            issn = soup.find(
                "a", attrs={"href": re.compile("^https://portal.issn.org/resource/ISSN/")}
            ).text
        except:
            issn = None
        return (full_name, issn)

    def get(self, name, second_name, year):
        if (name, second_name) in self.ranking_caches:
            rankings = self.ranking_caches[(name, second_name)]
        else:
            _ , issn = self.get_issn(second_name)
            rankings = self.get_sjr_rank(issn)
            self.ranking_caches[(name, second_name)] = rankings
        rank = None if rankings is None else get_in_ordered_list(rankings, int(year))
        if rank is None:
            return ["J", name, second_name, int(year), None, None, None]
        else:
            return ["J", name, second_name, int(year), rank[1], None, rank[2]]

    def get_sjr_rank(self, name):
        if name is None:
            return None
        url = "https://www.scimagojr.com/journalsearch.php?q=%s" % name.replace(
            " ", "+"
        )
        data = download(url)
        sjr_soup = BeautifulSoup(data, "html.parser")

        revues = sjr_soup.find("div", class_="search_results")
        dist = -1
        reference = None
        best_name = None
        for revue in revues.find_all("a"):
            tmp = revue.find("span").text
            lev = levenshtein(tmp, name)
            if dist == -1 or lev < dist:
                dist = lev
                best_name = tmp
                reference = "https://www.scimagojr.com/%s" % revue["href"]
            if dist == 0:
                break

        if reference is None:
            return []

        data = download(reference)
        sjr_soup = BeautifulSoup(data, "html.parser")
        table = sjr_soup.find_all("table")
        if len(table) == 0:
            return []

        df = pd.read_html(StringIO(str(table)))[0]
        if "Quartile" in df:
            df["Rank"] = [int(val[1]) for val in df.Quartile]
        else:
            return []

        mins = df.groupby("Year").min().Rank
        maxs = df.groupby("Year").max().Rank.to_dict()
        result = []
        for (y, v) in mins.items():
            if v == maxs[y]:
                ranking = "Q%s" % v
            else:
                ranking = "Q%s-Q%s" % (v, maxs[y])
            result.append((y, best_name, ranking))

        return result

def main():

    sjr = Sjr()
    core_ranking_caches = load_hash_caches("core")

    parser = argparse.ArgumentParser(
        description="Get ranking from DBLP and show a small summary"
    )
    parser.add_argument("url", help="DBLP url (or use clear-cache to clear the cache, is should be done regularly)")
    parser.add_argument("--start", type=int, default=-1, help="starting year")
    parser.add_argument("--end", type=int, default=10000, help="ending year")
    parser.add_argument(
        "-o", metavar=("output.csv"), default=None, help="output csv file"
    )
    parser.add_argument(
        "-d", action="store_true", help="display conference and journal list"
    )
    parser.add_argument(
        "--debug",
        help="Print lots of debugging statements",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Be verbose",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    args = parser.parse_args()

    url = args.url
    end_year = args.end
    csv_output = args.o
    start_year = args.start
    display_list = args.d
    logging.basicConfig(level=args.loglevel, format="%(levelname)s %(message)s")

    if args.url == 'clear-cache':
        cache_dir = default_cache()
        print("Cleaning the cache :", cache_dir);
        shutil.rmtree(cache_dir)
        print("Cache clear");
        sys.exit(0)
    
    username, elements = get_dblp(url)

    # Keeps only elements in the requested range
    elements = [elem for elem in elements if start_year <= int(elem[-1]) <= end_year]

    print(username)
    result = []
    with logging_redirect_tqdm():
        for venue, name, second_name, year in tqdm(elements):
            if venue == "conf":
                if (name, second_name, year) in core_ranking_caches:
                    rank = core_ranking_caches[(name, second_name, year)]
                else:
                    rank = get_core_rank(name, year)
                    if rank is None:
                        rank = get_core_rank(second_name, year)
                    core_ranking_caches[(name, second_name, year)] = rank
                if rank is None:
                    result.append(["C", name, second_name, int(year), None, None, None])
                else:
                    result.append(
                        [
                            "C",
                            name,
                            second_name,
                            int(year),
                            rank[1],
                            rank[2],
                            rank[0],
                        ]
                    )

            elif venue == "journals":
                result.append(sjr.get(name, second_name, year))
            else:
                tqdm.write(f"venue: {venue} ?")

    save_hash_caches(core_ranking_caches, "core")
    sjr.close()

    df = pd.DataFrame(
        result, columns=["type", "name", "short", "year", "longname", "acronym", "rank"]
    )

    df = df.fillna(value="")

    if start_year != -1:
        print("Starting year", start_year)
    else:
        print("Starting year", min(df["year"]))

    if end_year != 10000:
        print("Ending year", end_year)
    else:
        print("Ending year", max(df["year"]))

    print(
        "Not found",
        len(df) - df["rank"].count(),
        "out of a total of",
        len(df),
    )

    evaluation = df.groupby("rank").count()
    print(
        evaluation.drop(
            ["name", "short", "year", "longname", "acronym"], axis=1
        ).rename(columns={"type": "number"})
    )

    if not csv_output is None:
        df.to_csv(csv_output, index=False)

    if display_list:
        pd.set_option("display.max_rows", len(df))
        print(df)

if __name__ == "__main__":
    main()

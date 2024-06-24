import numpy
import requests

import logging
from tqdm import tqdm

LOG = logging.getLogger(__name__)

def levenshtein(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]


def download(url, filename=None):
    LOG.info(f"fetching {url}")
    r = requests.get(url, stream=True)
    data = b""
    total_size = int(r.headers.get("content-length", 0))
    for chunk in tqdm(
            r.iter_content(32 * 1024),
            total=total_size,
            unit="B",
            unit_scale=True,
            leave=False,
    ):
        if chunk:
                data += chunk
    if not filename is None:
        with open(filename, "wb") as file:
            file.write(data)

    return data

def get_in_ordered_list(ordered_list, year):
    if ordered_list == []:
        return None
    current = ordered_list[0]
    for elem in ordered_list[1:]:
        if year < elem[0]:
            return current
        current = elem
    return current

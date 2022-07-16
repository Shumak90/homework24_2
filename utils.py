import re
from typing import Iterator, List, Any


def query(cmd: str, value: str, file: Iterator) -> List[Any]:
    if "filter" == cmd:
        res = list(filter(lambda x: value in x, file))
        return res
    if "map" == cmd:
        res = list(map(lambda x: x.split()[int(value)], file))
        return res
    if "unique" == cmd:
        res = list(set(file))
        return res
    if "sort" == cmd:
        reverse = value == 'desc'
        res = list(sorted(file, reverse=reverse))
        return res
    if "limit" == cmd:
        val = int(value)
        res = list(file)[:val]
        return res
    if "regex" == cmd:
        result = re.compile(value)
        return list(filter(lambda x: result.search(x), file))
    return []

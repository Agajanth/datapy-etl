

from typing import List


def contains(*args, **kwg):
    is_not_contained:List = []
    check_all:bool = True
    for val in args[0]:
        if kwg[str(val)]:
            continue
        else:
            check_all = False
            is_not_contained.append(val)

    return is_not_contained, check_all

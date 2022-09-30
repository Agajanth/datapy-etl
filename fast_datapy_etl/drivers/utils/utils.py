

from typing import List


def contains(*args, **kwg):
    is_not_contained:List = []
    check_all:bool = True
    kwg_keys = kwg.keys()
    for val in args[0]:
        if val in kwg_keys:
            continue
        else:
            check_all = False
            is_not_contained.append(val)

    return is_not_contained, check_all

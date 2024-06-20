import sys
sys.path.append(".")

from typing import Dict

import rlmc


def main():
    rg = rlmc.Register()
    rg.register(rlmc.metaList)

    @rg.meta("metaList")
    class B(list): ...

    b = B()
    print(b.__dict__)
    c = [10, "nan", "nan", 80, 70, 60, "nan", 0, 20, "nan", "nan"]
    c = c[::-1]
    print(c)
    b << c
    b.appendleft(666)
    print(b)
    # index=b.head_anno()
    index = b.tail_anno()

    for i in index:
        print(b[i[0] : i[1]])
    d = B([9, 0, "c", "0"])
    type(d)
    print(type(rlmc.metaList))

    # @rg("乘法")
    # def mult(a: int, b: int):
    #     return a * b

    # @rg
    # def minus(a: int, b: int, c):
    #     """
    #     减法
    #     :param a: 减数
    #     """
    #     return a - b -c

    # print(dir(Dict))
    # print(type(Dict.values))
    # print(rg)
    # res = rg["minus"](1,2,9)
    # print(rg.values())
    # print(res)
    # print(type(Dict))

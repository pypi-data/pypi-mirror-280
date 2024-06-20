"""
@File    :   ab.py
@Time    :   2024/06/19 13:54:57
@Author  :   RayLam
@Contact :   1027196450@qq.com
"""

from abc import ABCMeta, abstractmethod


class Example(metaclass=ABCMeta):  # 抽象类
    @abstractmethod
    def example(self):  # 制定规范，其他子类中必须有pay方法，否则报错
        pass

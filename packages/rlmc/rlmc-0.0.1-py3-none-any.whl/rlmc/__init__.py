"""
@File    :   __init__.py
@Time    :   2024/06/19 13:38:17
@Author  :   RayLam
@Contact :   1027196450@qq.com
"""

import sys

sys.path.append(".")

from rlmc.utils.logger import Logger
from rlmc.utils.mc import metaList
from rlmc.utils.register import Register
from rlmc.utils.sudict import suDict


reg = Register()
reg.register(metaList)
reg.register(Logger)
reg.register(suDict)

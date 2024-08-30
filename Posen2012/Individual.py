# -*- coding: utf-8 -*-
# @Time     : 8/26/2024 16:20
# @Author   : Junyi
# @FileName: Individual.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import numpy as np


class Individual:
    def __init__(self, N=None):
        self.N = N
        self.belief = [np.random.uniform(0, 1) for _ in range(N)]
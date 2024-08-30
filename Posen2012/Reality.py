# -*- coding: utf-8 -*-
# @Time     : 8/26/2024 16:21
# @Author   : Junyi
# @FileName: Reality.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import numpy as np

class Reality:
    def __init__(self, N=None, ):
        """
        Reality produce rewards according to the arms and their probability
        :param N: number of arms
        """
        self.N = N
        self.arms = [np.random.beta(2, 2) for _ in range(N)]  # not sure why not normal distribution N(0.5, 0.22)?
        # It appears to bound the value between zero and one

    def turbulence(self):
        pass

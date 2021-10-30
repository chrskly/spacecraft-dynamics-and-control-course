#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import numpy as np

import ea
import dcm

class ModifiedRodriguesParameters:
    """
    MRP vector defined in terms of Euler parameters:
      σi = βi/(1+βo)   i=1,2,3
    """

    def __init__(self):
        self.sigma = []

    def init_from_sigma(self, sigma):
        pass

    def init_from_euler_parameters(self, eps):
        pass

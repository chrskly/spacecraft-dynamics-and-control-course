#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import numpy as np

import ea
import dcm

from lib import *

class ModifiedRodriguesParameters:
    """
    MRP vector defined in terms of Euler parameters:
      σi = βi/(1+βo)   i=1,2,3
    """

    def __init__(self, sigma=None):
        if sigma != None:
            self.sigma = sigma
        else:
            self.sigma = []
        logging.debug("mrp:init : sigma : %s" % self.sigma)

    def init_from_sigma(self, sigma):
        pass

    def init_from_euler_parameters(self, eps):
        pass

    def to_direction_cosine_matrix(self):
        """
        σ^2n = (σTσ)^n
        """
        sigma_2 = np.dot(np.transpose(self.sigma), self.sigma)
        logging.debug("mrp:to_direction_cosine_matrix : sigma_2: %s" % sigma_2)
        # sigma tilde
        sigma_tilde = tilde(self.sigma)
        logging.debug("mrp:to_direction_cosine_matrix : sigma_tilde: %s" % sigma_tilde)
        # calculate DCM
        top = 8 * np.dot(sigma_tilde, sigma_tilde) - np.dot(4 * (1 - sigma_2), sigma_tilde)
        bottom = (1 + sigma_2) * (1 + sigma_2)
        C = np.identity(3) + ( top / bottom )
        logging.debug("mrp:to_direction_cosine_matrix : C: %s" % C)
        return C









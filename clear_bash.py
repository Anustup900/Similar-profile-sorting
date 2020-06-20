# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:55:37 2020

@author: Anustup
"""
import os

class clear_bash(object):
    def __init__(self):
        self.clean()

    def clean(self):
        os.system('cls' if os.name == 'nt' else 'clear')
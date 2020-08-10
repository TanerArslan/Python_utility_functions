#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:39:05 2019

@author: tanerarslan
"""

def list2txt(lsts, fileName):
    '''
    Export list to txt file

    Parameter:
    ---------
    lsts: list output

    fileName: path

    return:
    -------
    txt file
    '''

    path = fileName + ".txt"

    with open(path, 'w') as f:
        for score in lsts:
            f.write("%s\n" % score)

    return

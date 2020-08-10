#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:39:05 2019

@author: tanerarslan
"""


def dict2txt(dict_output, fileName):
    '''
    Export dictionary to txt file

    Parameter:
    ---------
    dict_output: dictionary formatted output

    fileName: path

    return:
    -------
    txt file
    '''
    path = fileName + ".txt"

    with open(path, 'w') as f:
        for key, value in dict_output.items():
            string = "{}\t{}".format(key, value)
            f.write("%s\n" % string)

    return

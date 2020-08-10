#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:39:05 2019

@author: tanerarslan
"""

import os
import pandas as pd

def load_data(path, file_name):
    
    '''
    Load the data
    -------------
    
    Parameters
    ----------
    path: string, path of the data
    
    file_name: string, name of the file
    
    Return
    -------
    df: data.frame
    '''
    
    df_path = os.path.join(path, file_name)
    df = pd.read_table(df_path, sep = '\t')
    
    return df

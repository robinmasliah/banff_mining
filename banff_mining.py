#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:09:49 2018

@author: robin
"""

import tika
from tika import parser
import pandas as pd 
import re
import glob
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
import warnings
warnings.filterwarnings("ignore")


# get data file names:
path = r'/home/robin/Documents/INSERM/biopsy_scrap/'
filenames = glob.glob(path + "/*.pdf")

pdfs = []
for filename in filenames:
    pdfs.append(parser.from_file(filename))
    
    
appended_data = []
for i, pdf in enumerate(pdfs):
    df = search_direct_values(pdfs[i]['content'])
    appended_data.append(df)
appended_data = pd.concat(appended_data)
appended_data = appended_data.reset_index(drop=True)

appended_data = clean_table(appended_data)
add_ifta(appended_data)

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read in realtor data
realtor_data = pd.read_excel('USA Real Estate Dataset new.xlsx')

#Trim data to only texas properties
texas_realtor_data = realtor_data[realtor_data['state'] == 'Texas']

texas_realtor_data.head()
# https://www.kaggle.com/datasets/brijlaldhankour/hair-loss-dataset/data

# import the packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data
hair_loss = pd.read_csv('Kaggle/hair_loss/hair_loss.csv')

#explore the data
hair_loss.head()
hair_loss.shape

#check for missing values
hair_loss.isna().sum()

#look at some basic stats
hair_loss.describe()



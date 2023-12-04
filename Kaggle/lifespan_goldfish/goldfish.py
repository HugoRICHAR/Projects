#https://www.kaggle.com/datasets/stealthtechnologies/predict-lifespan-of-a-comet-goldfish

# import the packages
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder


# load the data
fish_data = pd.read_csv('Kaggle/lifespan_goldfish/fish_data.csv')

#remove the useless data
fish_data.drop('id',axis='columns',inplace=True)

#look at the missing data
fish_data.isnull().sum()

#one hot encoding
habitat=pd.get_dummies(fish_data['habitat'])
fish_data=fish_data.join(habitat)
color=pd.get_dummies(fish_data['color'])
fish_data=fish_data.join(color)
gender=pd.get_dummies(fish_data['Gender'])
fish_data=fish_data.join(gender)



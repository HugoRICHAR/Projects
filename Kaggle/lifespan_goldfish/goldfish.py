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

# load the data
fish_data = pd.read_csv('Kaggle/lifespan_goldfish/fish_data.csv')
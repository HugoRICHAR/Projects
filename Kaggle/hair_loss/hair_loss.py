# https://www.kaggle.com/datasets/brijlaldhankour/hair-loss-dataset/data

# import the packages
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# load the data
hair_loss = pd.read_csv('Kaggle/hair_loss/hair_loss.csv')

# explore the data
hair_loss.head()
hair_loss.shape

# check for missing values
hair_loss.isna().sum()

# look at some basic stats
hair_loss.describe()

# check if the sample is balanced
hair_loss['hair_fall'].hist()

# look at the correlation between the features
correlation = hair_loss.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)

# split the data
df_train, df_test = train_test_split(hair_loss, test_size=0.25, random_state=777)

X_train = df_train.drop('hair_fall', axis=1)
Y_train = df_train['hair_fall']

X_test = df_test.drop('hair_fall', axis=1)
Y_test = df_test['hair_fall']

# Scale the data to have std 1 and mean 0 (better to do it after splitting)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

# try with the K-neighbors
clf = KNeighborsClassifier(n_neighbors=20, weights='distance')
clf.fit(X_train, Y_train)

# look at the confusion matrix
prediction = clf.predict(X_test)
cm_knn = confusion_matrix(Y_test, prediction)  # doesn't work well

# try with decision tree
clf = DecisionTreeClassifier().fit(X_train, Y_train)
prediction = clf.predict(X_test)
cm_dtree = confusion_matrix(Y_test, prediction)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing

# load the dataset
df = pd.read_csv("cluster_mpg.csv")

#display first 5 rows

print(df.head())

label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(df["origin"])

print(list(label_encoder.classes_))
print()

print(label_encoder.transform(df["origin"]))

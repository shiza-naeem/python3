import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
df = pd.read_csv(Book1.csv)
print(df)
%matplotlib inline
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area, df.price, color = 'red', marker = '+')
new_df = df.drop('price', axis = 'columns')
print(new_df)
import pandas as pd
df = pd.read_csv('salary.csv')
df.head()
inputs = df.drop('Salary', axis = 1)
target = df['Salary']
from sklearn.preprocessing import LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()
inputs['company_n'] = le_company.fit_transform(inputs['copmany'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['Degree'])
input_n = inputs.drop(['comapny','job','Degree'])
input_n
from sklearn import tree
model = tree.DesicionTreeClassifier()
model.fit(input_n , target)
model.score(input_n , target)
model.predict([[2,1,0]])
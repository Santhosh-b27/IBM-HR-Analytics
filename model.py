import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#Load the File
df=pd.read_csv(r"D:\Projects\IBM HR Analytics\HR-Employee-Attrition.csv")
pd.set_option("display.max_column", None)

#Data Preprocessing
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df['BusinessTravel'] = le.fit_transform(df['BusinessTravel'])
df['Department'] = le.fit_transform(df['Department'])
df['EducationField'] = le.fit_transform(df['EducationField'])
df['Gender'] = le.fit_transform(df['Gender'])
df['JobRole'] = le.fit_transform(df['JobRole'])
df['MaritalStatus'] = le.fit_transform(df['MaritalStatus'])
df['Over18'] = le.fit_transform(df['Over18'])
df['OverTime'] = le.fit_transform(df['OverTime'])
df['Attrition'] = le.fit_transform(df['Attrition'])
print(df)

#Data Spliting
x=df.drop(columns=['Attrition'])
y=df['Attrition']
print("Input", x)
print("Output", y)

#Data Fitting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=12)

print("DF", df.shape)
print("x_train", x_train.shape)
print("y_train", y_train.shape)
print("x_test", x_test.shape)
print("y_test", y_test.shape)

#Model For Preddiction
print("Processingggg......")
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
LR=LogisticRegression()
LR.fit(x_train,y_train)
y_pred=LR.predict(x_test)
print("accuracy_score:", accuracy_score(y_pred,y_test))

test_prediction = LR.predict([[41,2,1102,2,1,2,1,1,1,2,0,94,3,2,7,4,2,5993,19479,8,0,1,11,3,1,80,0,8,0,1,6,4,0,5]])
if test_prediction==1:
    print("The Employee Left The Company")
else:
    print("The Employee Retained In the Company")

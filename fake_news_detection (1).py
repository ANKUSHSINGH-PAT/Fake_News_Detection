# -*- coding: utf-8 -*-
"""Fake_news_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lgCwy7kKUE69HHJUTWMeECg1gumCFseS

**Importing required library**
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import re
import string

"""**Importing file from drive**"""

from google.colab import drive
drive.mount('/content/drive')

path_fake='/content/drive/MyDrive/Colab Notebooks/Fake.csv'          # Inserting fake and real dataset
path_true='/content/drive/MyDrive/Colab Notebooks/True.csv'
df_fake=pd.read_csv(path_fake)
df_true=pd.read_csv(path_true)

df_true.tail(5)

df_fake.head(5)

"""**Inserting a column called "class" for fake and real news dataset to categories fake and true news.**"""

df_fake["class"] = 0
df_true["class"] = 1

df_fake.shape,df_true.shape

"""**Removing last 10 rows from both the dataset, for manual testing**"""

df_fake_manual_testing=df_fake.tail(10)
for i in range(23480,23470,-1):
  df_fake.drop([i], axis=0, inplace=True)  #delete the records row_wise
df_true_manual_testing=df_true.tail(10)
for i in range(21416,21406,-1):
  df_true.drop([i], axis=0, inplace=True)  #delete the records row_wise

"""**Merging the manual testing dataframe in single dataset and save it in a csv file**"""

df_manual_testing=pd.concat([df_fake_manual_testing,df_true_manual_testing],axis=0)
df_manual_testing.to_csv("manual_testing")

"""**Merging the main fake and true dataframe and "title", "subject" and "date" columns is not required for detecting the fake news, so I am going to drop the columns.**"""

df_merge=pd.concat([df_fake,df_true],axis=0)
df=df_merge.drop(["title","subject","date"],axis=1)
df.head(10)

"""**Randomly shuffling the dataframe**"""

df = df.sample(frac = 1)
df.tail(10)

df.isnull().sum()

"""**Creating a function to convert the text in lowercase, remove the extra space, special chr., ulr and links.**"""

def word_drop(text):                                   
  text = text.lower()
  text = re.sub('\\[.*?\\]', '', text)
  text = re.sub("\\W"," ", text)
  text = re.sub('https?://\\S+|www\\.\\S+', '', text)
  text = re.sub('<.*?>+', '', text)
  text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
  text = re.sub('\\n', '', text)
  text = re.sub('\\w*\\d\\w*', '', text)
  return text

df["text"]=df["text"].apply(word_drop)
df.to_csv("news")
df.head(10)

"""**Defining dependent and independent variable as x and y**"""

x=df["text"]
y=df["class"]

"""**Splitting the dataset into training set and testing set.**"""

x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=.25)

"""**Convert text to vectors**"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorization= TfidfVectorizer()
xv_train=vectorization.fit_transform(x_train)
xv_test=vectorization.transform(x_test)

"""**Implementation Of Logistic Regression**"""

from sklearn.linear_model import LogisticRegression

LR=LogisticRegression()
LR.fit(xv_train,y_train)

LR.score(xv_test,y_test)

predict_LR=LR.predict(xv_test)

cm=confusion_matrix(y_test, predict_LR)
cmd = ConfusionMatrixDisplay(cm, display_labels=['Fake','Real'])
cmd.plot()

print(classification_report(y_test,predict_LR))

"""**Implementation Of Decision Tree Classifier**"""

from sklearn.tree import DecisionTreeClassifier

DT=DecisionTreeClassifier()
DT.fit(xv_train,y_train)

DT.score(xv_test,y_test)

predict_DT=DT.predict(xv_test)

cm=confusion_matrix(y_test, predict_DT)
cmd = ConfusionMatrixDisplay(cm, display_labels=['Fake','Real'])
cmd.plot()

print(classification_report(y_test,predict_DT))

"""**Implementation Of Random Forest Classifier**"""

from sklearn.ensemble import RandomForestClassifier

RFC=RandomForestClassifier(random_state=0)
RFC.fit(xv_train,y_train)

RFC.score(xv_test,y_test)

predict_RFC=RFC.predict(xv_test)

cm=confusion_matrix(y_test, predict_RFC)
cmd = ConfusionMatrixDisplay(cm, display_labels=['Fake','Real'])
cmd.plot()

print(classification_report(y_test,predict_RFC))

"""**Manual Testing**"""

def output_lable(n):
  if n == 0:
    return "Fake News"
  elif n == 1:
    return "Not A Fake News"

def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(word_drop) 
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_RFC = RFC.predict(new_xv_test)

    return print("\n\nLR Prediction: {} \nDT Prediction: {} \nRFC Prediction: {}".format(output_lable(pred_LR[0]), 
                                                                                                              output_lable(pred_DT[0]),  
                                                                                                              output_lable(pred_RFC[0])))

news = str(input())
manual_testing(news)

dataframe = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/news.csv')

x = dataframe['text']
y = dataframe['label']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

tfvect = TfidfVectorizer(stop_words='english',max_df=0.7)
tfid_x_train = tfvect.fit_transform(x_train)
tfid_x_test = tfvect.transform(x_test)

LR = LogisticRegression()
LR.fit(tfid_x_train,y_train)

y_pred = LR.predict(tfid_x_test)
score = accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

DT = DecisionTreeClassifier()
DT.fit(tfid_x_train,y_train)

y_pred = DT.predict(tfid_x_test)
score = accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

RFC = RandomForestClassifier()
RFC.fit(tfid_x_train,y_train)

y_pred = RFC.predict(tfid_x_test)
score = accuracy_score(y_test,y_pred)
print(f'Accuracy: {round(score*100,2)}%')

import pickle
pickle.dump(LR,open('model.pkl', 'wb'))
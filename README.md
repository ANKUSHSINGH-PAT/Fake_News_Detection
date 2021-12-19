# Fake_News_Detection
Use Three Classifier algorithm to predict whether the news is true or Fake.

In this paper, we propose a solution to the fake news detection problem using the machine learning ensemble approach. Our study explores different textual properties that could be used to distinguish fake contents from real. By using those properties, we train a combination of different machine learning algorithms using various ensemble methods that are not thoroughly explored in the current literature. The ensemble learners have proven to be useful in a wide variety of applications, as the learning models have the tendency to reduce error rate by using techniques such as bagging and boosting. These techniques facilitate the training of different machine learning algorithms in an effective and efficient manner. We also conducted extensive experiments on real world publicly available datasets. The results validate the improved performance of our proposed technique using the 4 commonly used performance metrics (namely, accuracy, precision, recall, and F-1 score).


3 Live prediction

Designed a web application which receive input text(news) and predict whether the news is fake or real.
Created a html page for frontend and flask for connection to localhost server. Choose the best classifier from the given three classifiers. The accuracy score of the classifiers are as follows: -

Logistic Regression - 91.55% 

Decision Tree – 83.5%

Random Forest Classifier -90.21%

We choose Logistic regression as it has better accuracy.

UI Design



 


 





# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:39:41 2020

@author: Anustup
"""

from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('...//.html')

@app.route('/predict',methods=['POST'])
def predict():
	df= pd.read_csv("..//data", encoding="latin-1")
	df.drop(['Name', 'Graduation_year', 'Sex'], axis=1, inplace=True)
	# Features and Labels
	
	df['label'] = df['job_tags'].map({'Job_tag1': 0, 'job_tag2': 1,'Job_tag3':2})
X = df['What_are_looking_for']
y = df['label']
	
	# Extract Feature With CountVectorizer
	cv = CountVectorizer()
	X = cv.fit_transform(X) # Fit the Data
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	#Naive Bayes Classifier
	from sklearn.naive_bayes import MultinomialNB

	clf = MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)
	#Alternative Usage of Saved Model
	# joblib.dump(clf, 'NB_spam_model.pkl')
	# NB_spam_model = open('NB_spam_model.pkl','rb')
	# clf = joblib.load(NB_spam_model)

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template('..//.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
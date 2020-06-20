# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:21:50 2020

@author: Anustup
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from keras.preprocessing.text import Tokenizer

class DatasetSpliter(object):

    def __init__(self,dataset_path,vocab_size,max_length):
        self.data = pd.read_csv(dataset_path, header = 0, names = ['title', 'skill_name'])
        self.split_data()
        self.vocab_size=vocab_size
        self.max_length=max_length
        self.split_data()
        
    def split_data(self):
        # Split data to train and test (80 - 20)
        train, test = train_test_split(self.data, test_size=0.2)

        self.train_descs = train['skill_name']
        self.train_labels = train['title']

        self.test_descs = test['skill_name']
        self.test_labels = test['title']
        
        
    def data_encode(self):

        # define Tokenizer with Vocab Size
        tokenizer = Tokenizer(num_words=self.vocab_size)
        tokenizer.fit_on_texts(self.train_descs)
        x_train = tokenizer.texts_to_matrix(self.train_descs, mode='tfidf')
        x_test = tokenizer.texts_to_matrix(self.test_descs, mode='tfidf')
        
        encoder = LabelBinarizer()
        encoder.fit(self.train_labels)
        y_train = encoder.transform(self.train_labels)
        y_test = encoder.transform(self.test_labels)

        return x_train, y_train, x_test, y_test
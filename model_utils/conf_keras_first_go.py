# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:46:46 2020

@author: Anustup
"""


#Dataset path
dataset_path ='./data/skills.csv'

#Parameters
vocab_size=500
max_length=500
batch_size = 500
nb_epoch = 30

#Model Parameters
dense=512
dropout=0.1
labels=25
activation_function='relu'
last_activation_function='softmax'

#Complile Parameters
optimizer = 'adam' # or 'sgd'
loss = 'categorical_crossentropy'

#Model fit
validation_split=0.1
verbose=1
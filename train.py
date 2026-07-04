import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

import os


# Load Titanic dataset automatically
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

data = pd.read_csv(url)


# Select required columns
data = data[['Age','Sex','Fare','Pclass','Survived']]


# Handle missing values
data['Age'] = data['Age'].fillna(data['Age'].mean())


# Convert Gender
encoder = LabelEncoder()
data['Sex'] = encoder.fit_transform(data['Sex'])


# Input and output

X = data[['Age','Sex','Fare','Pclass']]

y = data['Survived']


# Scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)


# ANN Model

model = Sequential()

model.add(Dense(16,activation='relu',
                input_shape=(4,)))

model.add(Dense(8,activation='relu'))

model.add(Dense(1,activation='sigmoid'))


model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)


early = EarlyStopping(
    patience=5,
    restore_best_weights=True
)


# Train

model.fit(
    X_train,
    y_train,
    epochs=50,
    validation_data=(X_test,y_test),
    callbacks=[early]
)


# Accuracy

loss,acc = model.evaluate(X_test,y_test)

print("Accuracy:",acc)


# Save model

os.makedirs("model",exist_ok=True)

model.save("model/titanic_model.h5")


print("Model saved")
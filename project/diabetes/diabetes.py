import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers

f = open('diabetes.csv', encoding='utf-8')
data = pd.read_csv(f)
train_data = pd.get_dummies(data).values
train_data = np.array(train_data)
# print(train_data)

# shape: (768, 8)
train_data_x = np.array(train_data[:, 0:8])
# shape: (768, 1)
train_data_y = np.array(train_data[:, -1:])
# print(train_data_y.shape)
# print(train_data_x.shape)

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x=train_data_x, y=train_data_y, epochs=150, batch_size=10)

scores = model.evaluate(x=train_data_x, y=train_data_y)
print(scores)

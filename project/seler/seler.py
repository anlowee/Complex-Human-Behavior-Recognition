import numpy as np
from keras import Sequential
from keras.layers import LSTM, Dense
import time

seed = 2
look_back = 2
batch_size = 1
features = 18
np.random.seed(seed)
start = time.time()


def create_dataset(dataset):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        x = dataset[i:i + look_back]
        dataX.append(x)
        y = dataset[i + look_back]
        dataY.append(y)
        # print('X : %s, Y : %s' % (x, y))
    return np.array(dataX), np.array(dataY)


set1 = np.random.randint(0, 4, [4, features])
set2 = np.random.randint(10, 15, [3, 5])
set3 = np.random.randint(5, 10, [3, 6])
set4 = np.random.randint(0, 3, [3, 7])
set5 = np.concatenate([set2, set3, set4], axis=1)
dataset = np.concatenate([set1, set5], axis=0)


def build_model():
    model = Sequential()
    model.add(LSTM(units=4, batch_input_shape=(batch_size, look_back, features), stateful=True, return_sequences=True))
    model.add(LSTM(units=4, stateful=True))
    model.add(Dense(units=features))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


X_train, Y_train = create_dataset(dataset)
model = build_model()
model.fit(X_train, Y_train, epochs=3000, verbose=1, validation_split=0.25, batch_size=batch_size)

test = np.concatenate([Y_train[-2], Y_train[-1]], axis=0)
test = np.reshape(test, (1, look_back, features))
predict_train = model.predict(test).astype(int)

end = time.time()
print(dataset)
print(predict_train)
print((end - start))

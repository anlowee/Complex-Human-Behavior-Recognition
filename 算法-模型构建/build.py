from keras import Sequential
from keras.layers import LSTM, Dense

seed = 2
look_back = 2
batch_size = 1
features = 18

def build_model():
    model = Sequential()
    model.add(LSTM(units=4, batch_input_shape=(batch_size, look_back, features), stateful=True, return_sequences=True))
    model.add(LSTM(units=4, batch_input_shape=(batch_size, look_back, features), stateful=True))
    model.add(Dense(units=features))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


model = build_model()
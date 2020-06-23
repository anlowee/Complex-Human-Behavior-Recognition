import numpy as np

seed = 2
look_back = 2
batch_size = 1
features = 18

def create_dataset(dataset):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        x = dataset[i:i + look_back]
        dataX.append(x)
        y = dataset[i + look_back]
        dataY.append(y)
    return np.array(dataX), np.array(dataY)

X_train, Y_train = create_dataset(dataset)
model.fit(X_train, Y_train, epochs=1500, batch_size=batch_size)
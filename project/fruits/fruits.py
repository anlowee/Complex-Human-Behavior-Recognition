from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten
from keras.utils import to_categorical

ds_train = ImageDataGenerator().flow_from_directory(
    directory='C:\\Users\\anlow\\OneDrive\\dataset\\fruits-360_dataset\\fruits-360\\Training',
    batch_size=32,
    target_size=(100, 100))
ds_test = ImageDataGenerator().flow_from_directory(
    directory='C:\\Users\\anlow\\OneDrive\\dataset\\fruits-360_dataset\\fruits-360\\Test',
    batch_size=32,
    target_size=(100, 100))


def build():
    model = Sequential()
    model.add(Conv2D(4, kernel_size=(5, 5), activation='relu', input_shape=(100, 100, 3)))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(16, kernel_size=(5, 5), activation='relu'))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add((Conv2D(32, kernel_size=(5, 5), activation='relu')))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add((Conv2D(64, kernel_size=(5, 5), activation='relu')))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dense(120, activation='softmax'))
    return model


my_model = build()
my_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
my_model.fit_generator(generator=ds_train, epochs=10)
scores = my_model.evaluate_generator(generator=ds_test)
print(scores)




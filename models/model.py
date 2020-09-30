from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

def train_model(learning_rate = 0.001, momentum = 0.8):
    model = Sequential()
    model.add(Dense(18, input_dim=9, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.1))

    model.add(Dense(9, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))

    sgd = SGD(lr = learning_rate, momentum = momentum, nesterov=False)
    model.compile(loss='mean_squared_error', optimizer=sgd)

    print(model.summary())
    return model
import tensorflow as tf
import numpy as np
from keras.models import Model
from keras.layers import Input, Dense, Lambda
from keras.callbacks import EarlyStopping

class GRSBA(tf.keras.Model):
    def __init__(self, num_inputs, num_outputs, t=2, c=1.0, kernel_initializer='he_normal', clip_value=1.0, units=60, activation='relu', optimizer='adam', learning_rate=0.001, loss='mse', patience=10, epochs=100, batch_size=32, verbose=1):
        super(GRSBA, self).__init__()
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.t = t
        self.c = c
        self.kernel_initializer = kernel_initializer
        self.clip_value = clip_value
        self.units = units
        self.activation = activation
        self.optimizer = optimizer
        self.learning_rate = learning_rate
        self.loss = loss
        self.patience = patience
        self.epochs = epochs
        self.batch_size = batch_size
        self.verbose = verbose
        self.running = False

    def mod(self, value, modulus):
        """Applies modular arithmetic to wrap values around the modulus, creating a toroidal effect."""
        return tf.math.floormod(value, modulus)

    def call(self, inputs):
        return self.custom_output_layer(inputs)

    def custom_output_layer(self, inputs):
        a, s, r, w, v, u = tf.split(inputs, num_or_size_splits=self.num_inputs, axis=1)

        epsilon = 1e-10

        # Primeira parte da fórmula
        term1_numerator = v + (u - v) / (1 - (u * v) / (self.c ** 2) + epsilon)
        term1_denominator = 1 + (v * (u * v) / (1 - (u * v) / (self.c ** 2) + epsilon)) / (self.c ** 2)
        term1 = term1_numerator / (term1_denominator + epsilon)  # Evitar divisão por zero

        # Segunda parte da fórmula
        term2_numerator = 4 * w * r
        term2_denominator = np.pi * tf.sqrt(1 - (w * r) ** 2 / (self.c ** 2) + epsilon)
        term2 = term2_numerator / (term2_denominator + epsilon)  # Evitar divisão por zero

        # Aplicar o limite inverso de "a"
        term_limit = tf.pow(a + epsilon, -1)  # Adicionar epsilon para evitar divisão por zero

        result = (term1 + term2) * term_limit * self.t

        # Garantir que todos os tensores tenham a mesma forma antes das operações
        a = tf.reshape(a, [-1, 1])
        s = tf.reshape(s, [-1, 1])
        r = tf.reshape(r, [-1, 1])
        w = tf.reshape(w, [-1, 1])
        v = tf.reshape(v, [-1, 1])
        u = tf.reshape(u, [-1, 1])
        result = tf.reshape(result, [-1, 1])

        recursive_result = tf.concat([
            tf.expand_dims(self.mod(result[:, 0] + a[:, 0], self.clip_value), axis=1),
            tf.expand_dims(self.mod(result[:, 0] + s[:, 0], self.clip_value), axis=1),
            tf.expand_dims(self.mod(result[:, 0] + r[:, 0], self.clip_value), axis=1),
            tf.expand_dims(self.mod(result[:, 0] + w[:, 0], self.clip_value), axis=1),
            tf.expand_dims(self.mod(result[:, 0] + v[:, 0], self.clip_value), axis=1),
            tf.expand_dims(self.mod(result[:, 0] + u[:, 0], self.clip_value), axis=1)
        ], axis=1)

        combined_result = self.mod(result + recursive_result[:, 0], self.clip_value)

        x1 = combined_result + a[:, 0]
        y1 = self.mod(combined_result + s[:, 0], self.clip_value)
        z1 = self.mod(combined_result + r[:, 0], self.clip_value)
        x2 = self.mod(combined_result + w[:, 0], self.clip_value)
        y2 = self.mod(combined_result + v[:, 0], self.clip_value)
        z2 = self.mod(combined_result + u[:, 0], self.clip_value)

        output = tf.concat([x1, y1, z1, x2, y2, z2], axis=1)
        return tf.reshape(output, [-1, self.num_outputs])

def create_model(grsba):
    """Creates and compiles the Keras model using the GRSBA layer."""
    input_layer = Input(shape=(grsba.num_inputs,)) 
    hidden_layer = Dense(grsba.units, activation=grsba.activation, kernel_initializer=grsba.kernel_initializer, kernel_regularizer=tf.keras.regularizers.l2(0.01))(input_layer)
    hidden_layer = Dense(grsba.units, activation=grsba.activation, kernel_initializer=grsba.kernel_initializer, kernel_regularizer=tf.keras.regularizers.l2(0.01))(hidden_layer)
    hidden_layer = Dense(grsba.units, activation=grsba.activation, kernel_initializer=grsba.kernel_initializer, kernel_regularizer=tf.keras.regularizers.l2(0.01))(hidden_layer)
    output_layer = Lambda(lambda x: grsba.custom_output_layer(x), output_shape=(grsba.num_outputs,))(hidden_layer)

    if grsba.optimizer == 'adam':
        optimizer = tf.keras.optimizers.Adam(learning_rate=grsba.learning_rate, clipvalue=grsba.clip_value)
    elif grsba.optimizer == 'sgd':
        optimizer = tf.keras.optimizers.SGD(learning_rate=grsba.learning_rate, clipvalue=grsba.clip_value)
    else:
        optimizer = grsba.optimizer

    model = Model(inputs=input_layer, outputs=output_layer)
    model.compile(optimizer=optimizer, loss=grsba.loss)
    return model

def train(grsba, X, y, model):
    """Trains the model on the given data."""
    early_stopping = EarlyStopping(monitor='loss', patience=grsba.patience, restore_best_weights=True)
    history = model.fit(X, y, epochs=grsba.epochs, batch_size=grsba.batch_size, verbose=grsba.verbose, callbacks=[early_stopping])
    return history

def predict(grsba, input_data, model):
    """Predicts the output for the given input data."""
    predictions = model.predict(input_data)
    predicted_numbers = np.argsort(predictions, axis=1)[:, -grsba.num_outputs:]  # Select the 'num_outputs' numbers with highest probability
    return predicted_numbers
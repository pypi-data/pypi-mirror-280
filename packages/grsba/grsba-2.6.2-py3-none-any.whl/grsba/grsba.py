import time
import numpy as np
import tensorflow as tf
from keras.models import Model
from keras.layers import Input, Dense, Lambda
from keras.callbacks import EarlyStopping
import keras.backend as K
import threading

class GRSBA:
    def __init__(self, X, Y, t=None, max_depth=3, units=16, activation='relu', epochs=100, batch_size=32, patience=10, optimizer='adam', loss='mse', verbose=1):
        self.max_depth = max_depth
        self.units = units
        self.activation = activation
        self.epochs = epochs
        self.batch_size = batch_size
        self.patience = patience
        self.optimizer = optimizer
        self.loss = loss
        self.verbose = verbose
        self.y_shape = Y.shape[1]
        self.X = X
        self.t = t if t is not None else (time.time() * 100 % 6000) / 6000  
        self.model = self.create_model()
        self.running = False

    def mod(self, value, modulus):
        return tf.math.floormod(value, modulus)

    def custom_output_layer(self, inputs, depth=0):
        if depth >= self.max_depth:
            return tf.zeros_like(inputs[:, :self.y_shape])

        u, v, w, r, s, a = inputs[:, 0], inputs[:, 1], inputs[:, 2], inputs[:, 3], inputs[:, 4], inputs[:, 5]
        c = 1.0 
        epsilon = 1e-9  

        
        term1_numerator = v + (u - v) / (1 - (u * v) / (c ** 2))
        term1_denominator = 1 + (v * (u * v) / (1 - (u * v) / (c ** 2))) / (c ** 2)
        term1 = term1_numerator / (term1_denominator + epsilon)  
        
        term2_numerator = 4 * w * r
        term2_denominator = np.pi * tf.sqrt(1 - (w * r) ** 2 / (c ** 2))
        term2 = term2_numerator / (term2_denominator + epsilon) 

       
        term_limit = tf.pow(a + epsilon, -1) 

        result = (term1 + term2) * term_limit * self.t  

        new_inputs = tf.stack([u, v, w, r, s, a], axis=1)
        recursive_result = self.custom_output_layer(new_inputs, depth + 1)

        recursive_result = tf.concat([
            tf.expand_dims(self.mod(recursive_result[:, 0] + a, 1.0), axis=1),
            tf.expand_dims(self.mod(recursive_result[:, 1] + s, 1.0), axis=1),
            tf.expand_dims(self.mod(recursive_result[:, 2] + r, 1.0), axis=1),
            tf.expand_dims(self.mod(recursive_result[:, 3] + w, 1.0), axis=1),
            tf.expand_dims(self.mod(recursive_result[:, 4] + v, 1.0), axis=1),
            tf.expand_dims(self.mod(recursive_result[:, 5] + u, 1.0), axis=1)
        ], axis=1)

        combined_result = self.mod(result + recursive_result[:, 0], 1.0)

        x1 = combined_result + a
        y1 = self.mod(combined_result + s, 1.0)
        z1 = self.mod(combined_result + r, 1.0)
        x2 = self.mod(combined_result + w, 1.0)
        y2 = self.mod(combined_result + v, 1.0)
        z2 = self.mod(combined_result + u, 1.0)

        return tf.stack([x1, y1, z1, x2, y2, z2], axis=1)

    def create_model(self):
        input_layer = Input(shape=(self.X,))  
        hidden_layer = Dense(self.units, activation=self.activation)(input_layer)
        hidden_layer = Dense(self.units, activation=self.activation)(hidden_layer)
        output_layer = Lambda(lambda x: self.custom_output_layer(x), output_shape=(self.y_shape,))(hidden_layer)

        model = Model(inputs=input_layer, outputs=output_layer)
        model.compile(optimizer=self.optimizer, loss=self.loss)
        return model

    def train(self, X, y):
        early_stopping = EarlyStopping(monitor='loss', patience=self.patience, restore_best_weights=True)
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose, callbacks=[early_stopping])

    def predict(self, input_data):
        predictions = self.model.predict(input_data)
        predicted_numbers = np.argsort(predictions, axis=1)[:, -self.y_shape:]  # Seleciona os 'num_numbers' números com maior probabilidade
        return predicted_numbers

    def predict_continuously(self, input_data, update_callback, interval=1):
        self.running = True

        def _predict_loop():
            while self.running:
                predictions = self.predict(input_data)
                update_callback(predictions)
                time.sleep(interval)

        threading.Thread(target=_predict_loop, daemon=True).start()

    def stop_predicting(self):
        self.running = False
import tensorflow as tf
import numpy as np
import os
# Generar datos sintéticos
x_train = np.random.rand(1000, 1)
y_train = 2 * x_train + 1 + np.random.randn(1000, 1) * 0.1
# Crear y compilar el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])
model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo
model.fit(x_train, y_train, epochs=100, verbose=0)

# Guardar el modelo en formato SavedModel
model_dir = '/models/my_model/1'
os.makedirs(model_dir, exist_ok=True)
model.save(model_dir)
print(f"Modelo guardado en {model_dir}")
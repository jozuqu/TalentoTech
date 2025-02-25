# Importamos las librerías
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

 # Generar datos sintéticos
np.random.seed(0)

## Funciones de rago una por Nº de pasos y la otra por tamaño de los pasos
## np.linspace(start=0,stop=1,num=5) and np.arange(start=0,stop=1,step=0.25)

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 2 * X + 1 + np.random.randn(100, 1)

# Crear y compilar el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])
model.compile(optimizer='sgd', loss='mse')

# Entrenar el modelo
history = model.fit(X, y, epochs=100, verbose=0)

# Visualizar los resultados
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.title('Regresión Lineal')
plt.xlabel('X')
plt.ylabel('y')
plt.savefig('/app/regression_plot.png')
print("Gráfico guardado como regression_plot.png")

# Imprimir los pesos del modelo
print("Pesos del modelo:", model.get_weights())
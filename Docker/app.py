import tensorflow as tf
import numpy as np

print("Versión de tensorflow: ", np.__version__)
print("Versión de Numpy: ",np__version__)

#Crear un tensor simple
tensor = tf.constant([[1, 2],[3, 4]])
print("Tensor:", tensor)


#Realizar una operación simple
resultado = tf.matmul(tensor, tf.transpose(tensor))

print("Resultado de la multiplicación de matrices:", resultado)
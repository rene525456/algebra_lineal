import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
imagen = cv2.imread('/content/foto.png', 0)

print ('******Imagen Verdadera*****')
print (imagen)
print ('Shape de la imagen:', imagen.shape)

print ('******Imagen Con Brillo*****')
# Aumentar brillo
brillo = imagen * 2
print (brillo)

print ('******Imagen Negativa*****')
# Imagen negativa
negativa = 255 - imagen
print (negativa)

print ('******Imagen Oscurecer*****')
# Oscurecer imagen
oscura = imagen * 0.2
print (oscura)

# Mostrar imágenes
plt.figure(figsize=(10,5))

plt.subplot(1,4,1)
plt.imshow(imagen, cmap='gray')
plt.title("Original")

plt.subplot(1,4,2)
plt.imshow(brillo, cmap='gray')
plt.title("Brillo")

plt.subplot(1,4,3)
plt.imshow(negativa, cmap='gray')
plt.title("Negativa")

plt.subplot(1,4,4)
plt.imshow(oscura, cmap='gray')
plt.title("Oscura")

plt.show()

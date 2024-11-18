import matplotlib.pyplot as plt
import numpy as np
import keras

# Cargar los datos
# data = keras.utils.get_file(origin="http://cseweb.ucsd.edu/~viscomp/projects/LF/papers/ECCV20/nerf/tiny_nerf_data.npz")
# data = np.load(data)
data = np.load("imagenes\\NERF\\NERF.npz")
images = data["images"]
poses = data["poses"]
focal = data["focal"]

# Obtener el número total de imágenes
num_images, H, W, _ = images.shape

# Elegir una imagen aleatoria
index = 15
image = images[index]
pose = poses[index]

# Imprimir los datos de la imagen
print(f"Datos de la imagen {index}:")
print(f"Datos de las imagenes: {images.shape}")
print(f"Dimensiones de la imagen: {image.shape}")
print(f"Valor máximo de la imagen: {np.max(image)}")
print(f"Valor mínimo de la imagen: {np.min(image)}")
print(f"Pose de la cámara (matriz 4x4): \n{pose}")
print(f"Longitud focal: {focal}")

# Mostrar la imagen
plt.imshow(image)
plt.title(f"Imagen {index}")
plt.show()
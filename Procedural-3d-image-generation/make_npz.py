import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd

df = pd.read_json("imagenes\\NERF\\dataset\\transforms_train.json")

images = []
poses = []
focal = 50

for i in df.iloc:
    try:
        # Para la salida del blend CAJITA
        # images.append(np.array(Image.open("imagenes\\NERF\\dataset\\"+i['frames']['file_path']).convert('RGB').resize((100,100)))/255)
        # Para la salida del blend lego
        images.append(np.array(Image.open("imagenes\\NERF\\dataset\\train\\"+i['frames']['file_path'].split('/')[1]+".jpg").convert('RGB'))/255.0)
        poses.append(i['frames']['transform_matrix'])
    except Exception as e:
        print(e)
        break

np.savez("imagenes\\NERF\\NERF.npz", images=images, poses=poses, focal=focal)
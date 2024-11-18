import os
import random
from PIL import Image, ImageFont, ImageDraw

# Ruta donde quieres almacenar las imágenes creadas
file_base_path = "C:\\Users\\Ian\\Desktop\\procedural-3d-image-generation\\imagenes"

# ------------- Pipeline start -------------

damage = True

# Crear directorios si no existen
if not os.path.exists(os.path.join(file_base_path, "NERF")):
    new_dir = os.path.join(file_base_path, "NERF")
    os.makedirs(new_dir)
    print(f"Created directory {new_dir}")

# Listas de números de serie y de lote
serial_numbers = [
    "012345678901",
    "023456789012",
    "034567890123",
    "045678901234",
    "056789012345"
]

batch_numbers = [
    "AB123456-7C",
    "CD234567-8D",
    "EF345678-9E",
    "GH456789-0F",
    "IJ567890-1G"
]

# Generar imágenes dañadas
img = Image.open("./Template.png")
draw = ImageDraw.Draw(img)

serial_number = random.choice(serial_numbers)
prefix = serial_number[:2]
random_suffix = ''.join(random.choices('0123456789', k=10))
serial_number = prefix + random_suffix
batch_number = random.choice(batch_numbers)

font = ImageFont.truetype("./BellGothicStd-Bold.otf", 28)

draw.text((1060, 130), f"SN:              {serial_number}", (0,0,0), font=font)
draw.text((1060, 170), f"Ch.-B.:         {batch_number}", (0,0,0), font=font)
draw.text((1060, 210), f"Verw.bis:     12.2082", (0,0,0), font=font)

img.save('./Wrapping.png')

# Ejecutar comando de Blender para imágenes dañadas
if damage:
    os.system(f"C:\\Users\\Ian\\Desktop\\blender-4.2.0-windows-x64\\blender.exe PackageNERF.blend --python blenderBackgroundTaskNERF.py -- damaged {serial_number} {batch_number} {file_base_path}")
else:
    os.system(f"C:\\Users\\Ian\\Desktop\\blender-4.2.0-windows-x64\\blender.exe PackageNERF.blend --python blenderBackgroundTaskNERF.py -- intact {serial_number} {batch_number} {file_base_path}")
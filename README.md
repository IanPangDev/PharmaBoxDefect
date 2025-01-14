# PharmaBoxDefect

## Descripcion general
<p style="text-align: justify;">Este proyecto busca optimizar el proceso de fabricación de empaques para medicamentos a través de un sistema de control de calidad basado en visión artificial y el uso de modelos avanzados de inteligencia artificial. Se emplearán redes neuronales convolucionales (CNN) para detectar defectos en los empaques y mejorar la precisión en su inspección, asegurando que cumplan con los estándares regulatorios y de seguridad. Además, se planea explorar el uso de un modelo NERF (Neural Radiance Fields) para mejorar el diseño de los empaques, permitiendo una visualización más detallada y realista de los mismos, lo que podría contribuir a un diseño más eficiente y funcional. El proyecto tiene como objetivos reducir defectos, aumentar la satisfacción del cliente, reducir costos por devoluciones y retrabajos, y optimizar la calidad en la fabricación de los empaques.</p>

## Tecnologías
* Python
* Blender

## Estructura del proyecto
* <p style="text-align: justify;"> <b>Procedural-3d-image-generation</b>: Contiene la generacion de los paquetes intactos y dañados.<p>
* <p style="text-align: justify;"><b>NERF</b>: Contiene el modelo de Blender para la generación del modelo NERF.<p>

## Sistema de Clasificación de Empaques Dañados

### Arquitectura de la Red Neuronal Convolucional (CNN)

<p align="center"><img src="imagenes_md\Arquitectura.png" width=500 height=200></img><br>Arquitectura de la CNN</p>

### Grad-Cam de los empaques clasificados
<p align="center"><img src="imagenes_md\GradCAM_CNN.png" width=500 height=200></img><br>Grad-Cam del testeo</p>

## Modelo NERF para el Empaque de Medicamentos

### Gif del entrenamiento
<p align="center"><img src="imagenes_md\training.gif" width=500 height=100></img><br>Gif del entrenamiento</p>

### Gif del resultado
<p align="center"><img src="imagenes_md\rgb_video.gif" width=300 height=300></img><br>Gif del resultado</p>
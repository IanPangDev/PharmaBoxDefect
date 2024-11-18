import bpy
import os
import sys
import math
import random
import numpy as np
import datetime

argv = sys.argv
argv = argv[argv.index("--") + 1:]

package_serial_no = argv[1]
package_batch_no = argv[2]
file_base_path = argv[3]

print(f"Started processing package {package_serial_no} at {datetime.datetime.now()}")

def context_override():
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        return {
                            'window': window,
                            'screen': screen,
                            'area': area,
                            'region': region,
                            'scene': bpy.context.scene
                        } 

# Set the location of the object randomly
def random_location():
    x = random.uniform(-0.04, 0.04)
    y = random.uniform(-0.07, 0.07)
    bpy.data.objects["Package"].location = (x,y,0)

def random_rotation():
    angle = random.randint(-20, 20)
    bpy.data.objects["Package"].rotation_euler[2] = math.radians(angle)

def get_cubic_bezier_points(start, end, c1, c2, num_points=10, z_point=0):
    points = []
    for t in np.arange(0.0, 1.0, 1 / num_points):
        x = (1 - t)**3 * start[0] + 3 * t * (1 - t)**2 * c1[0] + 3 * t**2 * (1 - t) * c2[0] + t**3 * end[0]
        y = (1 - t)**3 * start[1] + 3 * t * (1 - t)**2 * c1[1] + 3 * t**2 * (1 - t) * c2[1] + t**3 * end[1]
        points.append((x, y, z_point))
    return points

def get_points_in_range(min_x, min_y, max_x, max_y, num_points, z_point):
    start_x = random.uniform(min_x, max_x)
    start_y = random.uniform(min_y, max_y)
    c1_x = random.uniform(min_x * 1.5, max_x * 2)
    c1_y = random.uniform(min_y * 1.5, max_y * 1.5)
    c2_x = random.uniform(min_x * 1.5, max_x * 1.5)
    c2_y = random.uniform(min_y * 1.5, max_y * 1.5)
    end_x = random.uniform(min_x, max_x)
    end_y = random.uniform(min_y, max_y)
    points = get_cubic_bezier_points((start_x, start_y), (end_x, end_y), (c1_x, c1_y), (c2_x, c2_y), num_points=num_points, z_point=z_point)
    return points

def sculpt(brush, coordinates, strength=0.5, pen_flip=True):
    if bpy.context.object.mode != 'SCULPT':
        bpy.ops.object.mode_set(mode='SCULPT')

    bpy.ops.paint.brush_select(sculpt_tool=brush)
    bpy.data.brushes["SculptDraw"].strength = strength
    strokes = []
    for i, coordinate in enumerate(coordinates):
        stroke = {
            "name": "stroke",
            "mouse": (0, 0),
            "pen_flip": pen_flip,
            "is_start": i == 0,
            "location": coordinate,
            "size": 50,
            "pressure": 1,
            "time": float(i),
            "mouse_event": (0, 0),
            "x_tilt": 0,
            "y_tilt": 0
        }
        strokes.append(stroke)

    # Usa context override
    override = context_override()
    if override:
        with bpy.context.temp_override(**override):
            bpy.ops.sculpt.brush_stroke(stroke=strokes)
    print("Finished sculpting")

# Change to Blender sculpt mode
bpy.data.objects["Package"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["Package"]
bpy.ops.sculpt.sculptmode_toggle()
bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

package_type = argv[0]
if package_type not in ["damaged", "intact"]:
    raise Exception("First argument must be either 'damaged' or 'intact'")

if package_type == "damaged":
    # If package is damaged, we add 3 pressure strokes with medium strength
    for i in range(0,3):
        strength = np.random.normal(0.35, 0.05)
        points = get_points_in_range(-0.05, -0.025, 0.05, 0.025, 10, 0.015)
        sculpt("DRAW", points, strength)

random_location()
random_rotation()

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_pattern(pattern="Package")
bpy.ops.object.shade_smooth()

frame_no = random.randint(1, 8)
bpy.context.scene.frame_set(frame_no)

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.image_settings.color_mode = 'RGB'
bpy.context.scene.cycles.use_denoising = False
bpy.context.scene.render.resolution_x = 640
bpy.context.scene.render.resolution_y = 360

for cam in bpy.data.objects:
    if cam.type == 'CAMERA':
        bpy.context.scene.camera = cam
        
        cam_name = cam.name.split(".")[1].lower()
        file_path = os.path.join(file_base_path, f'{package_type}/{package_serial_no}_{package_batch_no}_{cam_name}.jpg')
        bpy.context.scene.render.image_settings.file_format = 'JPEG'
        bpy.context.scene.render.filepath = file_path
        bpy.ops.render.render(write_still=True)

print(f"Finished processing package {package_serial_no} at {datetime.datetime.now()}")
bpy.ops.wm.quit_blender()
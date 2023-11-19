import bpy
import random
import os

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
def create_random_objects(num_objects):
    for _ in range(num_objects):
        x, y, z = [random.uniform(-5, 5) for _ in range(3)]
        bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, z))


def setup_scene():
    # Clear existing cameras
    cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']
    for camera in cameras:
        bpy.data.objects.remove(camera, do_unlink=True)

    # Create new camera
    bpy.ops.object.camera_add(location=(0, -10, 10), rotation=(1.1, 0, 0))
    camera = bpy.context.active_object

    # Set the created camera as the active camera for the scene
    bpy.context.scene.camera = camera

    # Setup lighting...
    # (rest of your lighting setup code)

    # Setup lighting
    bpy.ops.object.light_add(type='POINT', radius=1, location=(0, -3, 10))

def render_scene(image_path):
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = image_path
    bpy.ops.render.render(write_still=True)
    
def generate_data(output_folder, num_images=100):
    for i in range(num_images):
        clear_scene()
        num_objects = random.randint(1, 5)  # Random number of objects
        create_random_objects(num_objects)
        setup_scene()
        image_path = os.path.join(output_folder, f"image_{i:03d}.png")
        render_scene(image_path)
        # TODO: Add annotation generation logic here

if __name__ == "__main__":
    output_folder = "path_to_your_output_folder"  # Set this to your desired folder
    generate_data(output_folder)

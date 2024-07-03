import bpy

# assuming objects have same name as materials

# Loop through all objects in the scene
for obj in bpy.context.scene.objects:
    # Check if the material exists
    if obj.name in bpy.data.materials:
        # Get the material
        material = bpy.data.materials[obj.name]
        
        # Assign the material to the object
        if obj.data.materials:
            # If the object already has materials, replace the first one
            obj.data.materials[0] = material
        else:
            # If the object has no materials, append the new material
            obj.data.materials.append(material)

# Print a message when done
print("Materials assigned based on object names.")

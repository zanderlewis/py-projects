# Requirements: Pillow
# Difficulty: VI

from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} tall")

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f"The resized image size is {width} wide x {height} tall")
    resized_image.show()
    resized_image.save(output_image_path)

# Replace 'path_to_your_image.jpg' with the path to your image
resize_image('path_to_your_image.jpg', 'resized_image.jpg', (1920, 1080))
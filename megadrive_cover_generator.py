from PIL import Image, ImageDraw
import sys
import os

"""
1 mm = 11.512 px
Print size for output image: 32cm x 17.5cm
"""

if __name__ == '__main__':
    args = sys.argv
    image_path = args[1]
    image = Image.open(image_path)


    print(f"""I got the image. Image info:
    Filename: {image_path}
    Format: {image.format}
    Mode: {image.mode}
    Image Size: {image.size}""")


    # Create Canvas
    canvas = Image.new('RGB', (3660, 2020), 'black')

    # Resize image
    resized_image = image.resize((3235, 2020))

    # Add image to canvas
    canvas.paste(resized_image)

    # Save image
    canvas.save(os.path.splitext(image_path)[0] + '_generated.png', quality=100)
    print('Cover image created successfully!')
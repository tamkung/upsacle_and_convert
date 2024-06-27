from PIL import Image
import os
import glob
from datetime import datetime

# Function to convert and upscale images
def convert_and_upscale_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get list of all WEBP images in the input folder
    webp_images = glob.glob(os.path.join(input_folder, '*.webp'))
    number = 27
    for webp_image in webp_images:
        # Open the image
        with Image.open(webp_image) as img:
            # Get the original size
            original_size = img.size

            # Calculate new size (2x upscale)
            new_size = (original_size[0] * 3, original_size[1] * 3)

            # Resize the image
            upscaled_img = img.resize(new_size, Image.LANCZOS)

            # Create the output filename
            base_filename = os.path.basename(webp_image)
            output_filename = f"img_{number}.jpg"
            output_path = os.path.join(output_folder, output_filename)

            # Save the image as JPEG
            upscaled_img.save(output_path, 'JPEG', quality=100)
            number += 1
            print(f"Converted and upscaled image saved as: {output_path}")
            

# Example usage
input_folder = 'input'
output_folder = 'output'

convert_and_upscale_images(input_folder, output_folder)

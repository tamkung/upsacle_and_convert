from PIL import Image
import os
import glob

# Function to convert and upscale images with DPI setting
def convert_and_upscale_images(input_folder, output_folder, dpi=(300, 300)):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get list of all WEBP images in the input folder
    webp_images = glob.glob(os.path.join(input_folder, '*.webp'))
    number = 516
    for webp_image in webp_images:
        # Open the image
        with Image.open(webp_image) as img:
            # Get the original size
            original_size = img.size

            # Calculate new size (4x upscale)
            new_size = (original_size[0] * 4, original_size[1] * 4)

            # Resize the image
            upscaled_img = img.resize(new_size, Image.LANCZOS)

            # Create the output filename
            base_filename = os.path.basename(webp_image)
            output_filename = f"img_{number}.jpg"
            output_path = os.path.join(output_folder, output_filename)

            # Save the image as JPEG with specified DPI
            upscaled_img.save(output_path, 'JPEG', quality=100, dpi=dpi)
            number += 1
            print(f"Converted and upscaled image saved as: {output_path}")

# Example usage
input_folder = 'input'
output_folder = 'output'

convert_and_upscale_images(input_folder, output_folder)

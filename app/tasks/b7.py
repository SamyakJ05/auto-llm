from PIL import Image

# Function to resize the image
def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        # Resize the image while maintaining the aspect ratio
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)
        print(f"Image resized and saved at {output_path}")

# Function to compress the image
def compress_image(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        # Save the image with reduced quality (for compression)
        img.save(output_path, quality=quality)
        print(f"Image compressed and saved at {output_path}")

# Example usage
input_image_path = "C:\\Users\\sjsam\\OneDrive\\Documents\\New folder\\download.png"  # Replace with your image file path
output_image_path_resized = "resized_image.jpg"
output_image_path_compressed = "compressed_image.jpg"

# Resize image (e.g., resize to 800x800)
resize_image(input_image_path, output_image_path_resized, (800, 800))

# Compress image (reduce quality to 85%)
compress_image(input_image_path, output_image_path_compressed, quality=85)

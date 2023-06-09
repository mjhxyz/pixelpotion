from PIL import Image
import os


def convert(input_file, output_file, format=None, width=None,
            height=None, quality=80, optimize=True):
    with Image.open(input_file) as img:
        # Check if the output format is one of the supported formats
        if format and format.lower() not in ['jpg', 'jpeg', 'png']:
            raise ValueError(
                f'Unsupported format: {format}. Supported formats are: JPEG, PNG.')

        # Set the output format to the input image's format if none is provided
        if not format:
            format = img.format

        # quality and optimize may be None
        if quality is None:
            quality = 80
        if optimize is None:
            optimize = True

        # If neither width nor height is given, use the original size of the image
        if not width and not height:
            width, height = img.size
        # If only width is given, calculate height automatically
        elif width and not height:
            height = int(width / img.width * img.height)
        # If only height is given, calculate width automatically
        elif height and not width:
            width = int(height / img.height * img.width)
        # If both width and height are given, resize the image to the given dimensions
        else:
            pass

        img = img.resize((width, height))

        if format.lower() == 'jpg':
            format = 'JPEG'

        # Save the image
        img.save(output_file, format=format,
                 quality=quality, optimize=optimize)

    # Get the compressed file size
    compressed_size = os.path.getsize(output_file) / 1024
    print(f'Compressed file size: {compressed_size:.2f} KB')

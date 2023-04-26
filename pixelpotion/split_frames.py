import os

from PIL import Image


def split_frames(input_file, output_dir, prefix='frame'):
    """Split GIF animation into individual frames"""

    # Check if the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f'GIF 文件 "{input_file}" 不存在')

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with Image.open(input_file) as img:
        try:
            while True:
                index = img.tell()
                img.save(output_dir + f'/{prefix}-{index + 1:04}.png')
                img.seek(index + 1)
                print(f'Saved frame {index + 1}.')
        except EOFError:
            pass

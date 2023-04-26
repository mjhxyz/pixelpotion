import os
import shutil
import tempfile
import unittest
from PIL import Image

from pixelpotion.split_frames import split_frames


class TestSplitFrames(unittest.TestCase):

    # Create a temporary directory and a test GIF file before each test
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.img_path = os.path.join(self.temp_dir, 'test.gif')
        self.create_test_gif(self.img_path)

    # Remove the temporary directory and all its contents after each test
    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    # Test if the function can correctly split a GIF file into multiple PNG files
    def test_split_frames(self):
        # Prepare the test data
        output_dir = self.temp_dir

        # Call the function being tested
        split_frames(self.img_path, output_dir)

        # Perform assertions
        num_frames = len(os.listdir(output_dir))
        # Check if the number of output files is correct
        self.assertEqual(num_frames, 3 + 1)

        # Check if the output files exist
        for i in range(1, 4):
            filename = f'frame-{i:04}.png'
            filepath = os.path.join(output_dir, filename)
            self.assertTrue(os.path.exists(filepath))

    # Create a test GIF file with 3 frames
    def create_test_gif(self, img_path):
        # Create a 512x512 RGB image
        img = Image.new('RGB', (512, 512), color='red')
        img2 = Image.new('RGB', (512, 512), color='green')
        img3 = Image.new('RGB', (512, 512), color='blue')

        # Create an ImageSequence object with 3 frames, each frame is the same image
        frames = [img, img2, img3]

        # Save the GIF file
        frames[0].save(img_path, save_all=True, append_images=frames[1:],
                       format='GIF', duration=100, loop=0)


if __name__ == '__main__':
    unittest.main()

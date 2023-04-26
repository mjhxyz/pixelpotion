import unittest
import shutil
import tempfile
import os

from PIL import Image

from pixelpotion.convert import convert


class TestConvert(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.input_file = f'{self.temp_dir}/test_input.png'
        self.output_file = f'{self.temp_dir}/test_output.png'

        # Create a test image
        with Image.new('RGB', (512, 512), color='red') as img:
            img.save(self.input_file)

    def tearDown(self):
        # Remove the test image and output file
        shutil.rmtree(self.temp_dir)

    def test_convert_jpeg(self):
        # Test converting to JPEG
        convert(self.input_file, self.output_file, format='jpeg')
        # Check if the output file format is JPEG
        with Image.open(self.output_file) as img:
            self.assertEqual(img.format, 'JPEG')
        self.assertTrue(os.path.isfile(self.output_file))
        self.assertGreater(os.path.getsize(self.output_file), 0)

    def test_convert_png(self):
        # Test converting to PNG
        convert(self.input_file, self.output_file, format='png')
        # Check if the output file format is PNG
        with Image.open(self.output_file) as img:
            self.assertEqual(img.format, 'PNG')
        self.assertTrue(os.path.isfile(self.output_file))
        self.assertGreater(os.path.getsize(self.output_file), 0)

    def test_convert_no_format(self):
        # Test converting without specifying a format
        convert(self.input_file, self.output_file)
        # Check if the output file format is PNG
        with Image.open(self.output_file) as img:
            self.assertEqual(img.format, 'PNG')
        self.assertTrue(os.path.isfile(self.output_file))
        self.assertGreater(os.path.getsize(self.output_file), 0)

    def test_convert_invalid_format(self):
        # Test converting with an invalid format
        with self.assertRaises(ValueError):
            convert(self.input_file, self.output_file, format='bmp')

    def test_convert_resize(self):
        # Test resizing the image
        convert(self.input_file, self.output_file, width=50, height=50)
        # Check if the output file size is 50x50
        with Image.open(self.output_file) as img:
            self.assertEqual(img.size, (50, 50))


if __name__ == '__main__':
    unittest.main()

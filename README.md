# PixelPotion
PixelPotion is a command line tool based on Pillow for easy processing of PNG, JPG, and GIF images. It provides a simple and intuitive interface for performing common image operations such as resizing, cropping, and retrieving GIF frames.

## Features

- Supports PNG, JPG, and GIF image formats
- `Resize` images to a specified width and height
- `Crop` images to a specified size and position
- `Retrieve` individual frames from animated GIFs
- Save processed images to disk

# Installation
PixelPotion can be installed via pip:

TODO

# Usage
PixelPotion can be used via the command line interface. Here are some examples:

```bash
# Resize an image to 400x400 pixels
pixelpotion resize input.png output.png --width 400 --height 400

# Crop an image to 200x200 pixels
pp convert -f tmp/test.png -t png -w 200 -he 100 -q 300 -o tmp/out.png

# Extract the first frame of an animated GIF
pp gif split -f C:\Users\mjhxy\Desktop\input.gif -o tmp -p qq
```

For a full list of available commands and options, please refer to the Command Line Interface Documentation in the project wiki(TODO).

## API

PixelPotion is built on top of the popular Pillow library and extends its functionality. For more information on the API, please refer to the API Documentation in the project wiki(TODO).

## Contributing

Contributions to PixelPotion are always welcome! If you'd like to contribute, please read the Contributing Guide and submit a pull request(TODO).

## License

PixelPotion is licensed under the MIT License.
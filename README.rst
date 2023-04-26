PixelPotion
===========

PixelPotion is a command line tool based on Pillow for easy processing
of PNG, JPG, and GIF images. It provides a simple and intuitive
interface for performing common image operations such as resizing,
cropping, and retrieving GIF frames.

Features
--------

-  Supports PNG, JPG, and GIF image formats
-  ``Resize`` images to a specified width and height
-  ``Crop`` images to a specified size and position
-  ``Retrieve`` individual frames from animated GIFs
-  Save processed images to disk

Installation
============

PixelPotion can be installed via pip:

.. code:: bash

   pip install pixelpotion

Usage
=====

PixelPotion can be used via the command line interface. Here are some
examples:

**Original image:** |original|

**Resize to 100x100:**

.. code:: bash

   # Resize an image to 400x400 pixels
   pp resize input.png output.png --width 100 --height 100

.. figure:: https://img.mjhxyz.top/outpu.png
   :alt: 100x100

   100x100

**Crop to 200x100 JPEG:**

.. code:: bash

   # Crop an image to 200x100 pixels
   pp convert -f input.png -o outpu.jpg -t jpg --width 200 --height 100

.. figure:: https://img.mjhxyz.top/outpu.jpg
   :alt: 200x100

   200x100

**Extract first frame of animated GIF:**

.. code:: bash

   # Extract the first frame of an animated GIF
   pp gif split -f input.gif -o tmp -p frame

For a full list of available commands and options, please refer to the
Command Line Interface Documentation in the project wiki(TODO).

API
---

PixelPotion is built on top of the popular Pillow library and extends
its functionality. For more information on the API, please refer to the
API Documentation in the project wiki(TODO).

Contributing
------------

Contributions to PixelPotion are always welcome! If you’d like to
contribute, please read the Contributing Guide and submit a pull
request(TODO).

License
-------

PixelPotion is licensed under the MIT License.

.. |original| image:: https://img.mjhxyz.top/00008-624526612.png
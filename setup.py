from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name="pixelpotion",
    version="0.1.1",
    description="An open-source image processing tool based on the Pillow",
    long_description=long_description,
    author="Mao",
    author_email="mjhxyz@foxmail.com",
    url="https://github.com/mjhxyz/pixelpotion",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            'pp = pixelpotion.cli:main'
        ],
    },

    install_requires=[
        "Pillow>=8.2.0",
    ],
)

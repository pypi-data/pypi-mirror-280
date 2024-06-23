import platform
import subprocess
import sys

from setuptools import setup, find_packages
from setuptools.command.install import install


# Define the base dependencies
install_requires = [
    "onnxruntime-gpu",
    "torch",
    "torchvision",
    "transformers",
    "datasets",
    "evaluate",
    "opencv-python",
    "ray[serve]",
    "accelerate",
    "tensorboardX",
    "nltk",
    "python-multipart",
    "augraphy",
    "streamlit==1.30",
    "streamlit-paste-button",
    "shapely",
    "pyclipper",

    "optimum[exporters]",
]

# Add platform-specific dependencies
# if platform.system() != "Darwin":
#     install_requires.append("onnxruntime-gpu")

setup(
    name="texteller",
    version="0.1.1",
    author="OleehyO",
    author_email="1258009915@qq.com",
    description="A meta-package for installing dependencies",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OleehyO/TexTeller",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)

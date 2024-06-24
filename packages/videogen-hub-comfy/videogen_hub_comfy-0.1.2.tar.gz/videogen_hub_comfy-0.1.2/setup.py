from setuptools import setup, find_packages
import os

__version__ = None

# with open('README.md') as f:
#     readme = f.read()

readme = "VideoGenHub is a one-stop library to standardize the inference and evaluation of all the conditional video generation models. (This is a temporary package for Comfy SVD Advanced)"

with open('LICENSE') as f:
    license = f.read()

with open(os.path.join("src", "videogen_hub", "_version.py")) as f:
    exec(f.read(), __version__)

setup(
    name='videogen_hub_comfy',
    version=__version__,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='VideoGenHub is a one-stop library to standardize the inference and evaluation of all the conditional '
                'video generation models. (This is a temporary package for Comfy SVD Advanced)',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='D8ahazard, Max Kueng, and the TIGER-AI Lab team',
    author_email='d8ahazard@gmail.com',
    url='https://github.com/TIGER-AI-Lab/VideoGenHub',
    license=license,
    classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: GPU :: NVIDIA CUDA",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Programming Language :: Python :: 3",
        ]
)

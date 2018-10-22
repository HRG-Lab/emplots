from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='emplots',
    version='0.1.0',
    description='Provides an abstraction for creating several plots common in electromagnetics',
    license='MIT',
    long_description=long_description,
    author='Ryan Campbell',
    author_email='rdcampbell1990@gmail.com',
    packages=['emplots'],
    install_requires=['matplotlib', 'numpy', 'scipy', 'mayavi']
)

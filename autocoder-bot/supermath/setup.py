from setuptools import setup, find_packages

setup(
    name='supermath',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author='Your Name',
    description='A simple math operations package',
    python_requires='>=3.6'
)

from setuptools import setup, find_packages

setup(
    name='butiranx',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            # If you have any console scripts, specify them here
        ],
    },
    url='https://github.com/dudung/granular-system',
    license='MIT',
    author='Sparisoma Viridi',
    author_email='dudung@gmail.com',
    description='python package for simulation of granular system',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

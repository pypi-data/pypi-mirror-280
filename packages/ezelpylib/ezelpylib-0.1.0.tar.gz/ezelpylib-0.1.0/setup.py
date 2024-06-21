# setup.py
from setuptools import setup, find_packages

setup(
    name='ezelpylib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # 'command-name = module:function'
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple example Python library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ezelpylib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

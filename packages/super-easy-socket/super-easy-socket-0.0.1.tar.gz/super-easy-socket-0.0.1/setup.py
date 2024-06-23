from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.txt").read_text()

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='super-easy-socket',
  version='0.0.1',
  description='A Python module designed to simplify the implementation of socket-based server-client communication',
  long_description=long_description,
  long_description_content_type='text/markdown',  # Assuming your README.txt is in Markdown format
  url='',  
  author='Theodor Billek',
  author_email='HilbertLooked@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='super-easy-socket',
  packages={'super_easy_socket': 'src'},  
  install_requires=[''] 
)

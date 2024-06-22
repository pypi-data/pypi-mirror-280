from distutils.core import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
  name = 'PyBetterFileIO',         
  packages = ['PyBetterFileIO'],   
  version = '1.0.4',     
  license='NCSA',        
  description = 'A faster, more efficient Python file input and output framework', 
  long_description = long_description,
  long_description_content_type = 'text/markdown', 
  author = 'Keith Burroughs',                 
  author_email = 'keithburroughs33@gmail.com',      
  url = 'https://github.com/keithhb33/PyBetterFileIO',  
  download_url = 'https://github.com/keithhb33/PyBetterFileIO/archive/refs/tags/v1.0.4.tar.gz',   
  keywords = ['python', 'files', 'file', 'folder', 'folders', 'input', 'output', 'fileio', 'file management', 'script'],  
  install_requires=[            
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',      
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
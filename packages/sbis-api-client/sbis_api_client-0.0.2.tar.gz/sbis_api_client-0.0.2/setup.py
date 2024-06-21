# setup.py

from setuptools import setup, find_packages

def readme():
  with open('readme.md', 'r') as f:
    return f.read()


setup(
  name='sbis-api-client',
  version='0.0.2',
  author='juzyram',
  description='Python библиотека для работы с API СБИС',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/juzyram/sbis-api-client',
  packages=find_packages(),
  install_requires=['requests>=2.32.3'],    
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/juzyram'
  },
  python_requires='>=3.6'
)
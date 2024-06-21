from setuptools import setup
import setuptools

import pdf_ocr_txt

with open('pdf_ocr_txt/requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md", "r") as f:
    long_description = f.read()

version = pdf_ocr_txt.__version__
setup(name='pdf_ocr_txt',
      version=version,
      description='Tool to extract and store sentence embeddings to a fast and scalable vector db',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ptarau/pdf_ocr_txt.git',
      author='Paul Tarau',
      author_email='paul.tarau@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      # packages=['pdf_ocr_txt'],
      package_data={
          'pdf_ocr_txt': [
              'requirements.txt'
          ]
      },
      include_package_data=True,
      install_requires=required,
      zip_safe=False
      )

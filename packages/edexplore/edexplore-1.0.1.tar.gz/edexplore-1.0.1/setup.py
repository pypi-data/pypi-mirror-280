from setuptools import setup, find_namespace_packages
from glob import glob

setup(name='edexplore',
      version="1.0.1",
      description='A simple widget for interactive EDA / QA for those who use Pandas in Jupyter Notebook.',
      install_requires=['numpy>=1.25.2', 'pandas>=2.0.3', 'ipywidgets>=8.1.0', 'notebook>=7.0.2'],
      url='https://github.com/nagaprakashv/edexplore/',
      author='nagaprakash venkatesan',
      author_email='npv3105@outlook.com',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      packages=find_namespace_packages(),
      include_package_data=True,
      zip_safe=False)
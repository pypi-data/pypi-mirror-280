from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        return f.read()
  
setup(
    name='zer',
    version='0.0.6',
    author='ZerProg studio',
    install_requires=['tqdm'],
    long_description=readme(),
    description='Zer is a Python module for code reduction and automation.',
    packages=find_packages()
)
from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        return f.read()
    
setup(
    name='zerru',
    version='0.0.6',
    author='ZerProg studio',
    install_requires=['tqdm'],
    description='Zerru — это модуль zer на русском! Для сокращения и автоматизации кода.',
    long_description=readme(),
    packages=find_packages()
)
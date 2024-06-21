from setuptools import setup, find_packages

setup(
    name='qsreplace',
    version='0.0.1',
    description='A utility to replace query parameters in URLs',
    author='basedygt',
    author_email='basedygt@gmail.com',
    url='https://github.com/basedygt/qsreplace',
    packages=find_packages(),
    keywords=['qsreplace', 'url editor', 'params editor'],
    install_requires=['urllib3'],
)

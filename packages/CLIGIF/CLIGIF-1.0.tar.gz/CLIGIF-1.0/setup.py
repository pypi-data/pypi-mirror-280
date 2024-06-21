from setuptools import setup, find_packages

setup(
    name='CLIGIF',
    version='1.0',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'Pillow>=9.0.0'
    ]
    
)
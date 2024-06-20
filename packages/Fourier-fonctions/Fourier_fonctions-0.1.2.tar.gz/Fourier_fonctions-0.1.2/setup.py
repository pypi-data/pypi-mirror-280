# setup.py

from setuptools import setup, find_packages

setup(
    name='Fourier_fonctions',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    author='Leo leo',
    author_email='no@leo.com',
    description='Un package pour calculer la transformée de Fourier et d\'autres trucs utiles',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votreutilisateur/Fourier_fonctions',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

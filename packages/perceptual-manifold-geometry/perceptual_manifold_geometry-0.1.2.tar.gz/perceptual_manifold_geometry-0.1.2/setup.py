# setup.py

from setuptools import setup, find_packages

setup(
    name='perceptual_manifold_geometry',
    version='0.1.2',  
    author='Yanbiao Ma',
    author_email='ybmamail@stu.xidian.edu.cn',
    description='A package for analyzing the geometry of perceptual manifolds',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mayanbiao1234/Geometric-metrics-for-perceptual-manifolds',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'scikit-learn',
        'scipy',
        'ripser',
        'persim',
        'matplotlib',
        'scikit-dimension',
    ],
)

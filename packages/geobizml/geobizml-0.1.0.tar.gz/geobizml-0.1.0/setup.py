from setuptools import setup, find_packages

setup(
    name='geobizml',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'IPython',
        'geopandas',
        'shapely',
        'scikit-learn',
        'matplotlib',
        'numpy',
        'scipy',
        'cartopy',
        'requests',
    ],
    include_package_data=True,
    description='A package for geospatial data visualization, plotting, analysis, and machine learning.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/geobizml',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

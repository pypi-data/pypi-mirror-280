from setuptools import setup

setup(
    name='gree_air_purifier',
    version='0.0.2',
    description='Gree air purifier controller',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='WindzTrumpet',
    author_email='chinapat.dev@gmail.com',
    url='https://github.com/windztrumpet/GreeAirPurifier',
    packages=[
        'gree_air_purifier',
    ],
    package_dir={'gree_air_purifier': 'gree_air_purifier'},
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
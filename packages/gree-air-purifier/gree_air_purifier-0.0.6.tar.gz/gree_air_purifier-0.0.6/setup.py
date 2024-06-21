from setuptools import setup, find_packages

setup(
    name="gree_air_purifier",
    version="0.0.6",
    author="WindzTrumpet",
    author_email="chinapat.dev@gmail.com",
    description="GREE air purifier controller",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/windztrumpet/gree_air_purifier",
    packages=['gree_air_purifier'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pycryptodome==3.20.0'
    ]
)
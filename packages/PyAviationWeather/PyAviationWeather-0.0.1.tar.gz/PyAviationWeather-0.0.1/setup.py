from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name='PyAviationWeather',
    version='0.0.1',
    author='William Ng',
    author_email='Williamntw.Website@gmail.com',
    description='An aviation weather information python package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # py_modules=['get_METAR'],
    py_modules=[
        'pyaw'
        ],
    package_dir={
        '':'src'
        },
    install_requires=[
        "beautifulsoup4==4.9.3",
        "requests",
        "html5lib==1.1"
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
)
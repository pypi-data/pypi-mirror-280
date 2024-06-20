from setuptools import setup, find_packages

setup(
    name             = 'gifconvert_basic_tomas',
    version          = '1.0.1',
    description      = 'Test package for distribution',
    author           = 'Tomas',
    author_email     = 'tomasjoa21@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['GIFCONVERTER', 'gifconverter', 'pngtogif'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 
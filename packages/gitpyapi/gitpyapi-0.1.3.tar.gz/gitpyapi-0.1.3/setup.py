from setuptools import setup, find_packages
import os as _os

def readme(path: str):
    """
    Get the Content From a README File
    """
    import os as _os
    file = _os.path.basename(path)
    if file in ['README.rst', 'README.md']:
        with open(path, 'r') as f:
            return f.read()
    else:
        raise ValueError("File must named as 'README.md' or 'README.rst'")

setup(
    name='gitpyapi',
    version='0.1.3',
    description='Python GitHub API Client',
    long_description=readme(path='README.rst'),
    author='pyrootcpp',
    author_email='pyrootcpp@outlook.de',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "requests",
        "json5"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)

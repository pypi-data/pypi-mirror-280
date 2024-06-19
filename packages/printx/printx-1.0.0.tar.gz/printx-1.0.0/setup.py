from setuptools import setup, find_packages

setup(
    name='printx',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={},
    author='Javer Valino',
    description='A Python package to log messages using a print-like function.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/phintegrator/printx',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

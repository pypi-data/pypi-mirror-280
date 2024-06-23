from setuptools import setup, find_packages

setup(
    name='rpas_utils_lib',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'geopy==2.3.0',
        'httpx==0.27.0',
        'lxml==4.9.2',
        'numpy==1.24.1',
        'opencv_python==4.8.0.74',
        'pydantic==1.10.4',
        'PyExifTool==0.5.5',
        'pykml==0.2.0',
        'requests==2.32.3',
        'setuptools==70.1.0',
        'Shapely==2.0.4',
        'utm==0.7.0'
    ],
    author='Nuran Elsayed',
    author_email='nuran@esbaar.com',
    description='This library offers some utilities for Remotely Piloted Aircraft Systems (RPAS) services',
    url='https://github.com/your_username/your_package',
    keywords=['kml','visualize','detections','RPAS'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

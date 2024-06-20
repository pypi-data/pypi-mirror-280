from setuptools import setup, find_packages

setup(
    name='bandsplit_tensorflow',
    version='0.1.0',
    description='A non-official implementation of the BandSplit technique as a TensorFlow layer.',
    author='Nicolas Arrieta Larraza',
    author_email='n.arrieta.larraza@gmail.com',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.0.0'
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='opi-rf',
    version='0.9.7',
    author='0xE4s0n',
    author_email='0xE4s0n@gmail.com',
    description='Sending and receiving 433/315MHz signals with low-cost GPIO RF modules on a Orange Pi',
    long_description=long_description,
    url='https://github.com/0xE4s0n/opi-rf',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=[
        'opi',
        'orange pi',
        'rf',
        'gpio',
        'radio',
        '433',
        '433mhz',
        '315',
        '315mhz'
    ],
    install_requires=['wiringpi'],
    scripts=['scripts/opi-rf_send', 'scripts/opi-rf_receive'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)

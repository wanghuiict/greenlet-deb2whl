#! /usr/bin/env python
import setuptools

def readfile(filename):
    f = open(filename)
    try:
        return f.read()
    finally:
        f.close()

setuptools.setup(
    name="greenlet",
    version='0.4.11',
    description='Lightweight in-process concurrent programming',
    long_description=readfile("usr/share/doc/python-greenlet/README.rst"),
    maintainer="Alexey Borzenkov",
    maintainer_email="snaury@gmail.com",
    url="https://github.com/python-greenlet/greenlet",
    license="MIT License",
    platforms=['any'],
    data_files=[
        ('lib/python2.7/site-packages', ['usr/lib/python2.7/dist-packages/greenlet.so'])],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules']
    )

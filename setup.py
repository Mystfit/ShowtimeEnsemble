from setuptools import setup

setup(
    name='ShowtimeEnsemble',
    version='0.1',
    packages=[],
    dependency_links=['https://github.com/nanomsg/nnpy/tarball/master#egg=nnpy-1.3',
                      ],
    install_requires=['nnpy>=1.3', 'msgpack-python', 'enum34'],
    url='',
    license='',
    author='Byron Mallett',
    author_email='byronated@gmail.com',
    description=''
)

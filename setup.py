import setuptools
from numpy.distutils.core import setup, Extension

from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        Extension("one_plus", ["src/one_plus.pyx"]),
        Extension("multiply_two", ["src/multiply_two.f90"])
    ]),
)

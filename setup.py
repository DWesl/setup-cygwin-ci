from setuptools import setup, Extension

from Cython.Build import build_ext, cythonize

setup(
    ext_modules=cythonize([
        Extension("one_plus", ["src/one_plus.pyx"])
    ]),
    cmd_class={"build_ext": build_ext},
)

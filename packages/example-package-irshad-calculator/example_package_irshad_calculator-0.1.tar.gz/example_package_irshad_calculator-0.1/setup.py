from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize
import os

# Custom build_ext command to handle .py files
class build_ext(_build_ext):
    def run(self):
        # Call original build_ext
        _build_ext.run(self)
        # Remove .py files from the build directory after they are compiled
        for ext in self.extensions:
            py_file = ext.sources[0]
            if py_file.endswith('.py'):
                c_file = py_file.replace('.py', '.c')
                os.remove(py_file)  # Remove the .py file
                ext.sources = [c_file]  # Replace with the .c file

# Define your Cython extension
extensions = [
    Extension("example_package_irshad_calculator.add", ["example_package_irshad_calculator/add.py"])
]

setup(
    name="example_package_irshad_calculator",
    version="0.1",
    author="Irshad",
    author_email="",
    description="Packaging concept",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    ext_modules=cythonize(extensions, language_level=3),
    cmdclass={'build_ext': build_ext},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['setuptools>=18.0', 'Cython'],
    install_requires=[],
)

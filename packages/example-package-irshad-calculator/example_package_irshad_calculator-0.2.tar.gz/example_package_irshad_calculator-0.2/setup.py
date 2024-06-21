from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.command.sdist import sdist as _sdist
from Cython.Build import cythonize
import os
import shutil

class build_ext(_build_ext):
    def run(self):
        # Run the original build_ext command to build extensions
        super().run()
        # Remove .py source files after they are compiled to C
        for ext in self.extensions:
            py_file = ext.sources[0]
            if py_file.endswith('.py'):
                c_file = py_file.replace('.py', '.c')
                os.remove(py_file)  # Remove the .py file
                ext.sources = [c_file]  # Replace with the .c file

class clean_build_ext(_build_ext):
    def run(self):
        super().run()
        build_dir = os.path.abspath(self.build_lib)
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                if file.endswith('.py'):
                    os.remove(os.path.join(root, file))

class clean_sdist(_sdist):
    def run(self):
        super().run()
        for root, dirs, files in os.walk(os.path.abspath('my_module')):
            for file in files:
                if file.endswith('.py'):
                    os.remove(os.path.join(root, file))

# Define your Cython extension
extensions = [
    Extension("example_package_irshad_calculator.add", ["example_package_irshad_calculator/add.py"])
]

setup(
    name="example_package_irshad_calculator",
    version="0.2",
    author="Irshad",
    author_email="",
    description="Packaging concept",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(include=["example_package_irshad_calculator"]),
    ext_modules=cythonize(extensions, language_level=3),
    cmdclass={'build_ext': clean_build_ext, 'sdist': clean_sdist},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['setuptools>=18.0', 'Cython'],
    install_requires=[],
)

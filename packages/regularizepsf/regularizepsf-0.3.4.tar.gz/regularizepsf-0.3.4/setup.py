import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

ext_modules = [Extension("regularizepsf.helper",
                         sources=["regularizepsf/helper.pyx"],
                         include_dirs=[np.get_include()])]

setup(
    name="regularizepsf",
    python_requires=">=3.10",
    version="0.3.4",
    description="Point spread function modeling and regularization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["regularizepsf"],
    url="https://github.com/punch-mission/regularizepsf",
    license="MIT",
    author="J. Marcus Hughes",
    author_email="hughes.jmb@gmail.com",
    ext_modules=cythonize(ext_modules, annotate=True, compiler_directives={"language_level": 3}),
    install_requires=["numpy==1.26.4",
                      "dill",
                      "h5py",
                      "lmfit",
                      "sep",
                      "cython",
                      "astropy",
                      "scipy",
                      "scikit-image",
                      "matplotlib",
                      "setuptools"],
    package_data={"regularizepsf": ["helper.pyx"]},
    setup_requires=["cython"],
    extras_require={"test": ["pytest",
                             "pytest-cov",
                             "pytest-runner",
                             "hypothesis",
                             "ruff",
                             "pytest-mpl",
                             "pre-commit"]}
)

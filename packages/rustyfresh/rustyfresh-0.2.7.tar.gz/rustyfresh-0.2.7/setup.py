import os
from setuptools import setup
from setuptools_rust import Binding, RustExtension

try:
    with open(os.path.join(os.path.dirname(__file__), '../README.md'), 'r') as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = ""

cargo_toml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Cargo.toml'))

try:
    setup(
        name="rustyfresh",
        version="0.2.7",
        description="A Rust-based alternative to tsfresh for time series feature extraction.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="ighoshsubho",
        author_email="ighoshsubho@gmail.com",
        url="https://github.com/ighoshsubho/rustyfresh",
        rust_extensions=[RustExtension("rustyfresh", cargo_toml_path, binding=Binding.PyO3)],
        include_package_data=True,
        packages=["rustyfresh"],
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Rust",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            "setuptools>=42",
            "wheel",
            "setuptools_rust",
        ],
        zip_safe=False,
        python_requires='>=3.6',
    )
except Exception as e:
    print(f"Error during setup: {e}")
    raise
from setuptools import setup
from setuptools_rust import Binding, RustExtension

try:
    setup(
        name="rustyfresh",
        version="0.2.0",
        description="A Rust-based alternative to tsfresh for time series feature extraction.",
        long_description=open("../README.md").read(),
        long_description_content_type="text/markdown",
        author="ighoshsubho",
        author_email="ighoshsubho@gmail.com",
        url="https://github.com/ighoshsubho/rustyfresh",
        rust_extensions=[RustExtension("rustyfresh.rustyfresh", "../Cargo.toml", binding=Binding.PyO3)],
        include_package_data=True,
        packages=["rustyfresh"],
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Rust",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        zip_safe=False,
        python_requires='>=3.6',
    )
except Exception as e:
    print(f"Error during setup: {e}")
    raise
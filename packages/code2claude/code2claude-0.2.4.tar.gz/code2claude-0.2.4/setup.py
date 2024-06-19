
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = "0.2.4"

setup(
    name="code2claude",
    version=version,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={"": ["README.md"]},
    python_requires=">=3.6",
    include_package_data=True,
    scripts=[],
    license="BSD",
    url="https://github.com/ad3002/code2claude",
    author="Aleksey Komissarov",
    author_email="ad3002@gmail.com",
    description="A Python tool that consolidates code from a repository into a unified format for AI-assisted analysis and manipulation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        'console_scripts': [
            'code2claude = code2claude.consolidate:main',
        ],
    },
)

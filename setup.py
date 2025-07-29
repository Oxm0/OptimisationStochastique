from setuptools import setup, find_packages

setup(
    name="optimisationstochastique",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "plotly>=5.3.1",
        "scipy>=1.10.0",
        "openpyxl>=3.0.9",
        "streamlit>=1.28.0",
        "PyQt6>=6.1.0",
        "setuptools>=65.0.0",
        "wheel>=0.38.0",
        "xlrd>=2.0.1",
    ],
)

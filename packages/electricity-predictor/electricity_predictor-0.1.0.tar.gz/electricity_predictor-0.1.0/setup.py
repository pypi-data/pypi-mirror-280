from setuptools import setup, find_packages

setup(
    name="electricity_predictor",
    version="0.1.0",
    author="Neeraja Ram Manohar",
    author_email="neeraja.rammanohar@gmail.com",
    description="A package to predict whether electricity consumption is normal or abnormal",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/electricity_predictor",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "numpy",
        "xgboost"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

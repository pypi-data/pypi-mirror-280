from setuptools import setup, find_packages

setup(
    name="micro_ta",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ccxt",
        "pandas",
        "numpy",
        "matplotlib",
        "mplfinance",
        "seaborn",
        "tqdm",
    ],
    author="Burak Ç.",
    author_email="bcivitcioglu@gmail.com",
    description="A micro package for cryptocurrency technical analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bcivitcioglu/micro_ta",  # Replace with your GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discanal", # Replace with your own username
    version="0.0.1",
    author="hyungrae0907",
    author_email="hyungrae0907@gmail.com",
    install_requires=['scikit-learn',],
    description="판별분석",
    url="https://github.com/KHR0907/datamining.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
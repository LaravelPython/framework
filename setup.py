import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Chamak",
    version="0.0.6",
    author="Bedram Tamang",
    author_email="tmgbedu@gmail.com",
    description="A python implementation of laravel framework for machine learning, AI, datascience and data intensive work.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bedus-creation/LaraPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

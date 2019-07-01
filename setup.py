import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="music-festival",
    version="1.0.0",
    author="Sourabh Kumar",
    author_email="author@example.com",
    description="Music Festival challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourabh1983/music-festival",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

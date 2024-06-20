from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="euro_2024_poster_generator",
    version="0.0.1",
    author="Lasha Kajaia",
    author_email="lasha@kajaia.dev",
    description="A Python package to generate Euro 2024 match poster with Pillow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kajaia/euro-2024-poster-generator",
    packages=find_packages(),
    install_requires=[
        "pillow",
        "requests",
        "python-slugify"
    ],
    package_data={
        'euro_2024_poster_generator': ['assets/img/*.jpg', 'assets/fonts/*.ttf'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)

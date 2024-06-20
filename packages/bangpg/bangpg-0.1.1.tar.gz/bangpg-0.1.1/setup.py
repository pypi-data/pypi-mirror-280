from setuptools import setup, find_packages

setup(
    name="bangpg",
    version="0.1.1",
    author="MATHEUS DE SA DE SOUZA",
    author_email="matheusdesa55@gmail.com",
    description="This packeges implements a faster alternative `to_sql()` method for PostgreSQL that support COPY FROM.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/matheus0sa/bangpg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
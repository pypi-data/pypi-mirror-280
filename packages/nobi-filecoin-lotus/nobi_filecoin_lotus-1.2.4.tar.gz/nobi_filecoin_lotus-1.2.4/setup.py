import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="nobi-filecoin-lotus",
    version="1.2.4", # forked_version -> "1.2.1",
    author="Wen",
    author_email="wenqinchao@gmail.com",
    description="A package interact with bitcoin node",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/nobbennob/nobi-filecoin-lotus",  # main_repo -> "https://github.com/wenqinchao/filecoin-lotus",
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=required,
)

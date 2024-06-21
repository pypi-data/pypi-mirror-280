import setuptools

setuptools.setup(
    name="ds-io-utilities",
    version="0.0.31",
    author="Alida research team",
    author_email="engineering-alida-lab@eng.it",
    description="Utils for datasets IO operations in Alida.",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = [
        #"hdfs>=2.0.0",
        "bda-service-utils",
        "s3fs",
        "minio",
        "alida-arg-parser",
        "boto"
        ],
)

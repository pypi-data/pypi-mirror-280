import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyerrormetrics",
    description="pyerrormetrics is a library designed to calculate different error metrics (Error Quotient, Repeated Error Density, Watwin Algorithm, RR Algorithm) for a given set of code executions.",
    version="0.0.1",
    author="Annabell Brocker,"   
           "The Learning Technologies Research Group,"
           "RWTH Aachen University",
    author_email="a.brocker@cs.rwth-aachen.de",
    url="https://git.rwth-aachen.de/learntech-lufgi9/public/pyerrormetrics",
    license="MIT",
    packages=setuptools.find_packages(where="src"),    # List of all python modules to be installed
                                        # Information to filter the project on PyPi website

    package_dir={"": "src"},     # Directory of the source code of the package
    #data_files=[(".", ["LICENSE", "README.md"])],
    install_requires=[
        "Levenshtein",
        "datetime",
        "statistics",
        "pandas"
    ],                     # Install other dependencies if any
    platforms="any",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',                # Minimum version requirement of the package
    zip_safe=False,
    #py_modules = ["errormetrics", "error_quotient", "repeated_error_density", "watwin"]
)

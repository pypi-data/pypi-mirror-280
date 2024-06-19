# This code is part of vulqano.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.


import setuptools
import os
import os.path
import importlib.util

# Parse the version file
spec = importlib.util.spec_from_file_location("vulqano", "./vulqano/version.py")
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)

# Get the readme file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Define requirements
install_requires = [
    "qiskit==0.38.0",
    "qtealeaves>=1.1.10",
    "numpy",
    "matplotlib",
    "tqdm",
    "multiprocess",
]
# only for developers
# "sphinx",
# "sphinx-gallery",
# "sphinx_rtd_theme",
# "pre-commit",


setuptools.setup(
    name="vulqano",
    version=version_module.__version__,
    author=", ".join(
        [
            "Davide Rattacaso",
            "Daniel Jaschke",
            "Marco Ballarin",
        ]
    ),
    author_email="",
    description="Compiler for quantum algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://baltig.infn.it/qpd/vulqano.git",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={
        "vulqano": "vulqano",
        "vulqano/gates": "vulqano.gates",
        "vulqano/states": "vulqano.states",
        "vulqano/rules": "vulqano.rules",
        "vulqano/hamiltonians": "vulqano.hamiltonians",
        "vulqano/hamiltonians": "vulqano.circuit_tester",
        "vulqano/quantummodels": "vulqano.quantummodels",
    },
    packages=[
        "vulqano",
        "vulqano.circuit_tester",
        "vulqano.gates",
        "vulqano.states",
        "vulqano.rules",
        "vulqano.hamiltonians",
        "vulqano.circuit_tester",
        "vulqano.quantummodels",
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
)

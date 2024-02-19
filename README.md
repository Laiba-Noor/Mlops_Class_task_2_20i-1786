Class Activity - StudentsInMLOps Repository
Overview
This repository is part of a class activity for managing and automating operations related to student enrollment in a Machine Learning Operations (MLOps) course. The codebase includes a Python class for student management and a test suite to verify the class functionality.

Repository Structure
The repository contains the following key files:

main.py: Implements the StudentsInMLOps class with methods for enrolling and dropping students, as well as retrieving the total number of students and the class name.

test.py: Contains test cases for the StudentsInMLOps class methods, ensuring that the functionality is reliable and working as expected.

requirements.txt: Lists the pytest package as a dependency for running the test cases.

Makefile: Provides convenient commands for installing dependencies and running tests.

Continuous Integration
A GitHub Actions workflow is configured to run on every push to the repository. The workflow includes the following jobs:

Setting of Runner: Uses the latest Ubuntu runner.
Python Environment Setup: Sets up the specified Python environment.
Dependency Installation: Installs all necessary dependencies from requirements.txt.
Test Execution: Runs the test suite to validate the changes made.
Usage Instructions
To work with this project:

Clone the repository.
To install dependencies, run: make install or pip3 install -r requirements.txt.
To run tests, execute: make test or pytest test.py

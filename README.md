# Python Internship Practice Roadmap

A collection of functional Python programming exercises and utilities designed to build practical software engineering skills. The exercises progress from fundamental language operations to interactive applications, data management, and modular capstone projects.

## Project Structure

The repository is organized sequentially by complexity and domain. Each subdirectory contains standalone, executable scripts.

```text
.
├── beginner/
│   ├── authentication_security/
│   ├── basic_utilities/
│   └── string_processing/
├── intermediate/
│   ├── list_operations/
│   ├── numerical_problems/
│   └── text_analytics/
├── interactive/
├── data_management/
├── capstone/
└── README.md
```

### Modules

1. **Beginner**: Core language features including basic I/O, loops, conditionals, regex patterns, and string manipulation.
2. **Intermediate**: Algorithmic thinking involving list operations, math sequences, text analytics, and data processing.
3. **Interactive**: CLI-based simulations focusing on randomization and application state management.
4. **Data Management**: Object-oriented CRUD operations emphasizing dictionaries, file operations, and in-memory persistence.
5. **Capstone**: Larger multi-component systems (e.g., Banking System, URL Shortener, Payroll Calculator) designed to apply multiple concepts simultaneously.

## Requirements

- Python 3.8+
- Standard Library (No external dependencies required)

## Installation

Clone the repository locally:

```bash
git clone https://github.com/maxplanck100/python-practice-lab.git
cd python-practice-lab
```

## Usage

Each script is designed to run independently. You can execute any file directly via the Python interpreter. The modules include built-in `assert` checks to verify functionality upon execution. 

For example, to run an intermediate list operation:

```bash
python intermediate/list_operations/remove_duplicates.py
```

To run a capstone project:

```bash
python capstone/banking_system.py
```

### Verification

The codebase utilizes standard library assertions for validation. Running a script without encountering an `AssertionError` confirms that the underlying implementation is operating as expected. Some files may print basic output logs.

## Implementation Guidelines

- **Conciseness**: Solutions prioritize readability and avoid overengineering.
- **Dependency-Free**: Implementations rely strictly on the Python Standard Library (`re`, `random`, `datetime`, `collections`, `shutil`, `os`).
- **Test-Driven Design**: Executing a file directly evaluates its functionality via `if __name__ == "__main__":` execution guards. 

## Technical Objectives

This repository serves as a reference for:
- Writing idiomatic and minimal Python code.
- Mastering fundamental standard libraries.
- Applying basic OOP principles for state management and encapsulation.
- Formatting, filtering, and sanitizing data structures without external libraries.

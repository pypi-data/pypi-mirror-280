# Hello World Library
A simple Python library that provides a "Hello, World!" function.

## Installation
pip install hello-world-lib

## Usage
```python
from hello_world_lib import hello_world

print(hello_world())  # Output: Hello, World!
print(hello_world("Alice"))  # Output: Hello, Alice!
```

## Development
To set up the development environment:
1. Clone the repository
2. Install the package in editable mode with development dependencies:
```shell
pip install -e .[dev]
```
3. Run tests:
```shell
pytest
```

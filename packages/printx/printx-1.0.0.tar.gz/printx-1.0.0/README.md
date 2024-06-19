# printx

printx is a Python package that provides a print-like function for logging messages.

## Installation

You can install printx via pip:

```sql
pip install printx
```

## Usage

```python
from printx import printx_configure, printx

# Configure logging (optional: specify a custom log filename)
printx_configure()

# Use the printx function
printx("This is a default info message")
printx("This is a debug message", log_level='debug')
printx("This is an info message", log_level='info')
printx("This is a warning message", log_level='warning')
printx("This is an error message", log_level='error')
printx("This is a critical message", log_level='critical')

def example_function():
    try:
        printx("Starting the function")
        printx("Performing an action")
        error_condition = True  # Simulate an error condition
        if error_condition:
            raise ValueError("An error occurred")
        printx("Function finished")
    except Exception as e:
        printx(f"Exception occurred: {e}", log_level='error')

example_function()
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

[Javer Valino](https://github.com/phintegrator)

## Acknowledgments

- Thanks to the open-source community for providing the tools and inspiration for this project.
- Special thanks to all contributors and users of the package.
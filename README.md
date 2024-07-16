# Pizza Menu Project

This project implements a pizza ordering system with menu management, order processing, and daily sales summary functionality.

## Features

- Menu management with different types of menu items (e.g., Pizza, Drinks)
- Order processing with pricing, discounts, and tax calculations
- Daily sales summary generation

## Project Structure

- `main.py`: Main entry point of the application
- `menu_class.py`: Defines menu item classes
- `process_order_class.py`: Handles order processing
- `summary_class.py`: Generates daily sales summaries
- `ui_class.py`: handles user interface through CLI
- `test_classes.py`: Contains unit tests for the project

- `makefile`: contains all the commands i sued for automation in the project for dev
- `archive folder`: contains old unused code
- `draft folder`: contains ideas of code not fully implemented

## Run the program

- you can run using the main.py module or through the `make run` command

## Development

- Use `make format` to format the code
- Use `make check` for quick code checks (formatting, linting, type checking, and unit testing)
- Use `make full` for a comprehensive code check which includes pylint
- use `make unittest` for a basic unittest
- use `make pytest` for a full test using pytest framework
- use `make install` to install 3rd party for the GUI and testing

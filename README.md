# calculator

Sure, here's a README file for your calculator app:

---

# Calculator App

This is a simple calculator application built using Python and PyQt5. It supports basic arithmetic operations like addition, subtraction, multiplication, and division. 

## Features

- **Basic Arithmetic Operations**: Perform addition, subtraction, multiplication, and division.
- **Clear Button**: Clears the entire input.
- **Delete Button**: Deletes the last character from the input.
- **Error Handling**: Displays an error message for invalid operations.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/calculator-app.git
    cd calculator-app
    ```

2. **Install the required dependencies:**

    ```sh
    pip install PyQt5
    ```

## Usage

1. **Run the application:**

    ```sh
    python calculator_app.py
    ```

2. **Use the calculator:**

    - Click the buttons to perform arithmetic operations.
    - Click the `clear` button to reset the input.
    - Click the `<` button to delete the last character from the input.
    - Click the `=` button to calculate the result.

## Code Overview

- `CalculatorApp(QWidget)`: The main class for the calculator app.
- `__init__()`: Sets up the app window.
- `init_ui()`: Initializes the UI components.
- `on_button_click(text)`: Handles button click events.

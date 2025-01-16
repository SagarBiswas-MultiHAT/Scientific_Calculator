

### README:

```markdown
# Scientific Calculator

This Python application is a scientific calculator built using Tkinter. It supports various mathematical operations, including basic arithmetic (addition, subtraction, multiplication, division), trigonometric functions (sin, cos, tan), square root, exponentiation, and more.

## Features:
- Basic arithmetic operations (+, -, *, /)
- Trigonometric functions (sin, cos, tan) in radians
- Square root and exponentiation (^)
- Clear display (C) and backspace (⌫)
- Responsive grid layout

## Requirements:
- **Python 3.x**
- **Tkinter** (included with Python)

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

### Running the Script

To run the script, follow these steps:

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the following command:

   python3 scientific_calculator.py
   ```

### Example Usage:
1. **Basic Operations**: Enter the numbers and operations, and click "=" to evaluate.
2. **Trigonometric Functions**: Enter the angle in degrees, then click "sin", "cos", or "tan" to get the result.
3. **Square Root**: Click "sqrt" to compute the square root of the displayed number.
4. **Exponentiation**: Use "^" to compute powers.

### Example Output:
```bash
![](https://scontent.fdac178-1.fna.fbcdn.net/v/t39.30808-6/473619514_122136009782552158_767090033486993121_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=127cfc&_nc_ohc=RvnAq2LPOw8Q7kNvgFVbaBm&_nc_zt=23&_nc_ht=scontent.fdac178-1.fna&_nc_gid=AcBfKUTTM7Cm2xx33xdoqKq&oh=00_AYALlDqMGtk3Atq1cFFqQ9OEvP1qpyQThr0KwH-r6n4iTw&oe=678EA0E4)
```

## Code Explanation

### Main Script

- **GUI Layout**: The calculator uses a responsive grid layout. Each button is assigned to a grid cell, and the buttons are dynamically created using a loop.
- **Operations**: The calculator supports basic arithmetic, trigonometric functions, square root, and exponentiation. The user input is evaluated dynamically using Python's `eval()` function.
- **Error Handling**: When an invalid operation is performed (e.g., dividing by zero or invalid input), the calculator displays "Error".

### Error Handling
- **Invalid Operations**: If the input is invalid (e.g., dividing by zero or using invalid characters), the calculator displays "Error".
- **Trigonometric Functions**: If the user enters an invalid value for trigonometric functions, the calculator catches the error and displays "Error".

## Contributing

Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. This license permits anyone to use, modify, and distribute the software with minimal restrictions, ensuring flexibility for open-source development. See the [LICENSE](LICENSE) file for details.

---

**Note**: This script is designed for educational purposes and personal use.
```

---

This repository setup provides a clean and clear structure for your scientific calculator application. Let me know if you'd like to make any adjustments!

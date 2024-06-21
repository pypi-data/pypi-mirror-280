# valid_input

valid_input is a lightweight Python library for performing commonly used input checks like make the user inputs a valid int or float or an especific option

## Installation

You can install input_tools using pip:

```bash
pip install valid_input
```

## Usage

```
from valid_input import input_int, input_float, input_option

age = input_int("Introduce your age: ")
height = input_float("What's your height? (in meters): ")
sex = input_option("What's your sex? (male/female/other)", ["male", "female", "other"])

# At this point, you can be sure that:
#  age variable is an integer
#  height variable is a float
#  sex variable is one of three options on the list
```

## License

valid_input is distributed under the MIT License.
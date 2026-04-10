# Robotic Package Sorting System

A Python-based package sorting system that classifies packages into three categories (STANDARD, SPECIAL, or REJECTED) based on their physical dimensions and mass.

## Overview

This project implements an automated sorting algorithm for a robotic package handling system. Packages are evaluated against specific criteria to determine which sorting stack they should be routed to.

## Sorting Criteria

Packages are classified using the following rules:

### Bulky Packages
A package is considered **bulky** if:
- Its volume is greater than or equal to 1,000,000 cm³, OR
- Any single dimension (width, height, or length) is greater than or equal to 150 cm

### Heavy Packages
A package is considered **heavy** if:
- Its mass is greater than or equal to 20 kg

### Classification Logic

| Condition | Result |
|-----------|--------|
| Neither bulky nor heavy | **STANDARD** |
| Either bulky OR heavy (but not both) | **SPECIAL** |
| Both bulky AND heavy | **REJECTED** |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smarter-technologies-coding-hallenge.git
cd smarter-technologies-coding-hallenge
```

2. Ensure you have Python 3.x installed:
```bash
python --version
```

No external dependencies are required for the core functionality.

## Usage

### Basic Example

```python
from robotic_package_sort import sort

# Standard package (small and light)
result = sort(10, 10, 10, 10)
print(result)  # Output: STANDARD

# Special package (heavy but not bulky)
result = sort(10, 10, 10, 20)
print(result)  # Output: SPECIAL

# Rejected package (both bulky and heavy)
result = sort(150, 20, 20, 25)
print(result)  # Output: REJECTED
```

### API Reference

#### `sort(width, height, length, mass)`

Sorts a package based on its dimensions and mass.

**Parameters:**
- `width` (int/float): Width of the package in centimeters
- `height` (int/float): Height of the package in centimeters
- `length` (int/float): Length of the package in centimeters
- `mass` (int/float): Mass of the package in kilograms

**Returns:**
- `"STANDARD"`: Small and light package that requires standard handling
- `"SPECIAL"`: Package that requires special handling (either bulky or heavy)
- `"REJECTED"`: Package that cannot be handled (both bulky and heavy)

**Examples:**
```python
sort(100, 100, 100, 10)   # Returns "SPECIAL" (bulky by volume)
sort(150, 10, 10, 5)      # Returns "SPECIAL" (bulky by dimension)
sort(10, 10, 10, 20)      # Returns "SPECIAL" (heavy)
sort(100, 100, 100, 20)   # Returns "REJECTED" (both bulky and heavy)
sort(1, 1, 1, 1)          # Returns "STANDARD" (minimum values)
```

## Running Tests

The project includes comprehensive unit tests covering all sorting scenarios.

### Run All Tests

```bash
python -m unittest robotic_package_sort_test.py
```

### Run Tests with Verbose Output

```bash
python -m unittest robotic_package_sort_test.py -v
```

### Test Coverage

The test suite includes:
- **STANDARD Stack Tests**: Validates packages that are neither bulky nor heavy
- **SPECIAL Stack Tests (Bulky Only)**: Tests packages that are bulky but not heavy
- **SPECIAL Stack Tests (Heavy Only)**: Tests packages that are heavy but not bulky
- **REJECTED Stack Tests**: Validates packages that are both bulky and heavy
- **Edge Cases**: Tests with minimum and boundary values

## Project Structure

```
smarter-technologies-coding-hallenge/
├── README.md                          # This file
├── robotic_package_sort.py            # Core sorting algorithm
└── robotic_package_sort_test.py       # Unit tests
```

## License

This project is provided as-is for educational and commercial use.
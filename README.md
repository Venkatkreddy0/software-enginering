# software-enginering
# Fermat's Last Theorem Near Misses Finder

This program finds "near misses" for Fermat's Last Theorem for the equation \( x^n + y^n \neq z^n \). It systematically searches for x, y combinations, computes \( x^n + y^n \), and looks for z and z+1 that bracket \( x^n + y^n \). The program calculates the actual miss and the relative miss, printing out the smallest relative miss.

## Installation

1. **Clone the repository**:
    ```bash
    git clone 
    ```

2. **(Optional) Create an executable**:
    If you want to create an executable file from the Python script, you can use `PyInstaller`:
    ```bash
    pip install pyinstaller
    pyinstaller --onefile fermat_near_misses.py
    ```

## Usage

1. **Run the script**:
    ```bash
    python fermat_near_misses.py
    ```

2. **Enter the values**:
    - Enter the value for \( n \) (2 < n < 12).
    - Enter the value for \( k \) (k > 10).

3. **Example**:
    ```
    Fermat's Last Theorem Near Misses Finder
    Enter the value for n (2 < n < 12): 3
    Enter the value for k (k > 10): 15
    ```


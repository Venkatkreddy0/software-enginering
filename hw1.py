# Title: Fermat's Last Theorem Near Misses Finder
# File: fermat_near_misses.py
# External Files Required: None
# External Files Created: None
# Programmers: [Venkat Reddy Kusukuntla], [Aravind Pedavalli]
# Emails: [VenkatReddyKusukun@lewisu.edu], [  ]
# Course: [SU24-CPSC-60500-001] 
# Date: [28/7/2024]
# Description: This program finds "near misses" for Fermat's Last Theorem for the equation x^n + y^n != z^n
#              It systematically searches for x, y combinations, computes x^n + y^n, and looks for z and z+1 
#              that bracket x^n + y^n. The program calculates the actual miss and the relative miss, printing 
#              out the smallest relative miss.

import math
def find_near_misses(n, k):
    """
    Finds and prints the near misses for Fermat's Last Theorem for given n and k. 
    Args:
    n (int): The power to use in the equation (2 < n < 12).
    k (int): The upper limit for the range of x and y values (k > 10).
    """
    smallest_relative_miss = float('inf')  #Initialize the smallest relative miss to infinity
    best_x = best_y = best_z = 0           #Initialize the best x, y, z values
    best_actual_miss = 0                   #Initialize the best actual miss

    #Iterate over all possible values of x and y within the range 10 to k (inclusive)
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            x_n = x ** n
            y_n = y ** n
            sum_x_y_n = x_n + y_n

            z = int(sum_x_y_n ** (1/n))
            z_n = z ** n
            z1_n = (z + 1) ** n

            miss1 = abs(sum_x_y_n - z_n)   #Calculate the miss for z
            miss2 = abs(z1_n - sum_x_y_n)  #Calculate the miss for z+1

            actual_miss = min(miss1, miss2)  #Find the smallest actual miss
            relative_miss = actual_miss / sum_x_y_n  #Calculate the relative miss

            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z = x, y, z
                best_actual_miss = actual_miss

                print(f"New best near miss found:")
                print(f"x = {best_x}, y = {best_y}, z = {best_z}")
                print(f"Actual miss: {best_actual_miss}")
                print(f"Relative miss: {smallest_relative_miss:.6f}")

    print("\nSmallest relative miss found:")
    print(f"x = {best_x}, y = {best_y}, z = {best_z}")
    print(f"Actual miss: {best_actual_miss}")
    print(f"Relative miss: {smallest_relative_miss:.6f}")

def main():
    """
    Main function to execute the program. It takes user input for n and k and calls the find_near_misses function.
    """
    print("Fermat's Last Theorem Near Misses Finder")
    n = int(input("Enter the value for n (2 < n < 12): "))
    if n <= 2 or n >= 12:
        print("n must be between 2 and 12 (exclusive).")
        return

    k = int(input("Enter the value for k (k > 10): "))
    if k <= 10:
        print("k must be greater than 10.")
        return

    find_near_misses(n, k)

    Exit = input("Press Enter to exit")

if __name__ == "__main__":
    main()

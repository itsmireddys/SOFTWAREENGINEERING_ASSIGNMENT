import itertools  # Import itertools for count function

import sys
# Program Title: Fermat's Last Theorem Near Misses
# File Name: fermat_near_misses.py
# External Files Needed: itertools
# External Files Created: None
# Programmers: Vidya Sagar Reddy Mukkala, sai krishna
# Course: Software Engineering 001
# Date Completed: 2023-09-24
# Program Explanation: This program searches for near misses of Fermat's Last Theorem for given n and k values.
# It calculates and displays the smallest relative miss and related information.
# Resources Used: None


def calculate_relative_miss(x, y, z, n):
    # Calculate (xn + yn)
    xn_yn = x ** n + y ** n

    # Find zn and (z+1)n
    zn = int(xn_yn ** (1/n))
    zn_plus_1 = zn + 1

    # Calculate the misses
    miss_zn = abs(xn_yn - zn ** n)
    miss_zn_plus_1 = abs(zn_plus_1 ** n - xn_yn)

    # Determine the smallest miss
    if miss_zn < miss_zn_plus_1:
        smallest_miss = miss_zn
        closest_z = zn
    else:
        smallest_miss = miss_zn_plus_1
        closest_z = zn_plus_1

    # Calculate the relative miss as a percentage
    relative_miss = (smallest_miss / xn_yn) * 100

    return closest_z, smallest_miss, relative_miss

def main():
    print("Fermat's Last Theorem Near Miss Finder")
    print("--------------------------------------")

    # Get user input for n and k
    try:
        n = int(input("Enter the power (n) for xn + yn = zn (2 < n < 12): "))
        if n <= 2 or n >= 12:
            print("Invalid value for n. It must be between 2 and 12.")
            sys.exit(1)

        k = int(input("Enter the limit (k) for x and y (k >= 10): "))
        if k < 10:
            print("Invalid value for k. It must be greater than or equal to 10.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        sys.exit(1)

    smallest_relative_miss = float('inf')
    best_x, best_y, best_z = 0, 0, 0

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            closest_z, miss, relative_miss = calculate_relative_miss(x, y, 0, n)

            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z = x, y, closest_z

                print(f"X= {best_x}, y= {best_y}, relative diff= {smallest_relative_miss / 100:.6f}")

    print("\nSmallest relative miss found:")
    print(f"X= {best_x}, y= {best_y}, relative diff= {smallest_relative_miss / 100:.6f}%")


if __name__ == "__main__":
    main()

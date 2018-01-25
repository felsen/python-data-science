"""
About Matplotlib Library.
"""

import matplotlib.pyplot as plt


def simple_square():

    # Specifying the input values.
    input_values = [1, 2, 3, 4, 5]

    squares = [1, 4, 9, 16, 25]

    # plt.plot(squares)
    # plt.show()

    # Set chart title and x,y label.
    plt.plot(input_values, squares, linewidth=5)
    plt.title("Square Number", fontsize=24)
    plt.xlabel("Value", fontsize=24)
    plt.ylabel("Sqaure of Value", fontsize=14)

    # Set the size of the tick label.
    plt.tick_params(axis="both", labelsize=14)
    
    plt.scatter(2, 4)
    plt.show()


# This is a sample Python script.

import numpy as np

x_values = np.array([1,2,3,4,5,6,7,8,9,10])
y_values = np.array([1,4,1,6,4,7,4,6,10,8])

#within this project, we are using the slope-equation to be able to plot what is known as linear regression

def line_of_best_fit(x_values, y_values):
    m = (((x_values.mean() * y_values.mean()) - (x_values * y_values).mean()) / ( (x_values.mean()) ** 2 - (x_values ** 2).mean()))
    b = y_values.mean() - m * x_values.mean()

    return m, b



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    print(line_of_best_fit(x_values, y_values))
    # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

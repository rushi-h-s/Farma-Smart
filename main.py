import os

# Define the directory structure
directories = [
    'pharmacyStore',
    'pharmacyStore/connector',
    'pharmacyStore/main',
    'pharmacyStore/connector/ConnectionProvider',
    'pharmacyStore/subpackage2/module2'
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

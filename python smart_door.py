# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Staff:
    # Constructor
    def __init__(self, s_name, access_code):
        self.s_name = s_name               # public attribute
        self.__access_code = access_code   # private attribute

    # Property to view access code
    @property
    def access_code(self):
        return self.__access_code

    # Property setter to update access code
    @access_code.setter
    def access_code(self, new_code):
        if len(new_code) >= 6:
            self.__access_code = new_code
            print("Access code updated successfully.")
        else:
            print("Access code must be at least 6 characters long.")

    # Display staff information
    def display_info(self):
        print(f"Staff Name: {self.s_name}")
        print(f"Access Code: {self.__access_code}")


# Creating a Staff object
staff1 = Staff("Reginald Nhyiraba Mensah", "UMAT123")

# Display initial information
print("Initial Staff Information")
staff1.display_info()

# Viewing access code
print("\nViewing Access Code")
print(staff1.access_code)

# Updating with a valid code
print("\nUpdating Access Code")
staff1.access_code = "ORIC2026"

# Updating with an invalid code
print("\nTrying Invalid Update")
staff1.access_code = "123"

# Final information
print("\nFinal Staff Information")
staff1.display_info()
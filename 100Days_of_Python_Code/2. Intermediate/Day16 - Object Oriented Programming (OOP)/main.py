# import anaother_module

# print(anaother_module.another_variable)


# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy) # object being printed
# timmy.color('coral')
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.right(100)


# # car.speed > car is object and speed is attribute

# my_screen = Screen()
# print(my_screen.canvheight)

# # object methods
# my_screen.exitonclick()

# Python Packages

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = (["SrNo","Name", "Place", "JirsyNo"])
table.add_row([1, "Rohit", "MI", 45])
table.add_row([2, "Virat", "DL", 18])
table.add_rows([
    [3, "Jaspreet", "MI", 91],
    [4,"Hardik", "MI", 33],
    [5, "Surya", "MI", 63]]
)
print(table)


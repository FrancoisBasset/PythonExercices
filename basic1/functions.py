"""Methods for the part1 of Basic."""

from basic1 import utils

def exo1():
    """Print a short text with indentation."""
    print(utils.get_twinkle_text())

def exo2():
    """Print the Python version."""
    print(utils.get_python_version())

def exo3():
    """Print a formatted date."""
    print(utils.get_formatted_date())

def exo4():
    """Print the circle area."""
    print(utils.get_circle_area(1.1))

def exo5():
    """Print the firstname and lastname in reverse order."""
    print(utils.get_reverse_names("Victor", "Hugo"))
    print(utils.get_reverse_names("Jean-Jacques", "Rousseau"))

def exo6():
    """Print list and tuple from string sequence."""
    first = utils.get_list_and_tuple("1,2,3,4")
    print(f"List : {first['list']}\nTuple : {first['tuple']}\n")

    second = utils.get_list_and_tuple("a,b,c,d,e,f")
    print(f"List : {second['list']}\nTuple : {second['tuple']}")

def exo7():
    """Print file extension"""
    file_name = "test_python.py"
    print(f"{file_name} => {utils.get_extension(file_name)}")

    file_name = "abc.java"
    print(f"{file_name} => {utils.get_extension(file_name)}")

def exo8():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0], color_list[-1])

def exo9():
    print("The examination will start from :", utils.get_date(25, 12, 2023))

def exo10():
    print(utils.n_nn_nnn(5))

def exo11():
    print(utils.get_doc("abs"))

def exo12():
    print(utils.get_calendar(6, 2023))

def exo13():
    print("""\
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example\
""")

def exo14():
    print(utils.get_diff_date((2023, 2, 25), (2023, 6, 4)), "days")

def exo15():
    print("Radius 6cm :", utils.get_sphere_area(6))

def exo16():
    print(utils.get_absolute_twice(8, 30))

def exo17():
    print(900, utils.near_thousand(900))
    print(800, utils.near_thousand(800))
    print(900, utils.near_thousand(2050))

def exo18():
    print(2, 4, 6, utils.sum_three_times(2, 4, 6))
    print(4, 4, 4, utils.sum_three_times(4, 4, 4))

def exo19():
    s = "lsdebian"
    if s.startswith("ls"):
        print(s)
    else:
        print("ls" + s)

def exo20():
    pass

def exo21():
    pass
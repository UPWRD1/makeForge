"""
Makefile Generator.
"""
import os

args = []
libs = []

def user_i(message):
    """ I was lazy, so here's a quick solution to replace 2 lines."""
    print(message)
    user_input = input("y/n: ")
    return user_input

def gen_file():
    """ Main function to generate the makefile """

    file = open("makefile", "x", encoding="utf-8")
    ## Compiler
    if user_i("Use GCC for compilation?") == "y":
        file.write("CC = GCC\n")
    ## -Wall Flag
    if user_i("Use the -Wall flag? (Recomended)") == "y":
        file.write("CFLAGS = -WALL")
    ## Library Options
    if user_i("Include Libraries?") == "y":
        print("Type the libraries you would like to use, seperated by commas")
        new_libs = input()
        for i in new_libs:
            libs.append(new_libs)



def menu():
    """ Menu function, runs on start."""
    os.system('clear')
    print("Welcome to MakeGen.")
    print("Select an Option:")
    print("     1. Generate Makefile")
    print("     2. Quit MakeGen")

    main_menu = input("Choose:")

    if main_menu == "1":
        gen_file()
    elif main_menu == "2":
        exit()
    else:
        menu()

menu()

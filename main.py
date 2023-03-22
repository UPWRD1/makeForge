"""
Makefile Generator.
"""
import os
import time

libs = []
flags = []
deps = []
cfiles = []


def user_i(message):
    """ I was lazy, so here's a quick solution to replace 2 lines."""
    print(message)
    user_input = input("y/n: ")
    return user_input


def gen_file():
    """ Main function to generate the makefile """
    global flags
    global deps
    global cfiles

    file = open("makefile", "w", encoding="utf-8")

    # Compiler
    if user_i("Use GCC for compilation?") == "y":
        file.write("CC = GCC\n")

    # Flags
    if user_i("Use compiler flags? (Recomended)") == "y":
        print("Type the flags you would like to use, seperated by a space")
        new_flags = input("Flags: ")
        flags = new_flags.split()

    # Dependancies
    if user_i("Include header (.h) files") == "y":
        print("Type the filenames of the header (.h) files, seperated by a space")
        new_deps = input("Headers: ")
        deps = new_deps.split()

    # C files
    print("Type the filenames of the c (.c) files, seperated by a space")
    new_files = input("Files: ")
    cfiles = new_files.split()
    out_cfiles = [sub.replace('.c', '.o') for sub in cfiles]

    # Name the executable
    print("What do you want to name the executable?")
    exe_name = input("Name: ")

    # CLS
    os.system('clear')

    ##########################
    # Begin Makefile Creation
    ##########################

    # Flags
    file.write("CFLAGS = ")
    for i in flags:
        file.write(i + " ")
    file.write("\n")

    os.system('clear')
    print("- Forging [==        ]")
    time.sleep(0.5)

    # Dependancies
    file.write("DEPS = ")
    for j in deps:
        file.write(j + " ")
    file.write("\n")

    # .o files (OBJ)
    file.write("OBJ = ")
    for i in out_cfiles:
        file.write(i + " ")
    file.write("\n")
    file.write("\n")

    os.system('clear')
    print("\\ Forging [====      ]")
    time.sleep(0.5)

    # Rule: Output file instructions
    file.write("%.o: %.c $(DEPS)\n")
    file.write("\t")
    file.write("$(CC) -c -o $@ $< $(CFLAGS)")
    file.write("\n")
    file.write("\n")

    # Rule: Target
    file.write(exe_name + ": $(OBJ)")
    file.write("\n")
    file.write("\t")
    file.write("$(CC) -o $@ $^ $(CFLAGS)")

### MENU ###

def menu():
    """ Menu function, runs on start."""
    os.system('clear')
    print("Welcome to makeForge.")
    print("Select an Option:")
    print("     1. Generate Makefile")
    print("     2. Quit makeForge")

    main_menu = input("Choose: ")

    if main_menu == "1":
        gen_file()
    elif main_menu == "2":
        exit()
    else:
        menu()

menu()

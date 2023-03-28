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
    """ A quick solution to replace 2 lines."""
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
        file.write("CC = gcc\n")

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

    # Cosmetics
    os.system('clear')
    print("- Forging [=     ]")
    time.sleep(0.2)

    # Dependancies
    file.write("DEPS = ")
    for j in deps:
        file.write(j + " ")
    file.write("\n")

    ## Cosmetics
    os.system('clear')
    print("\\ Forging [==    ]")
    time.sleep(0.2)

    # Source Files
    file.write("SOURCE = ")
    for i in cfiles:
        file.write(i +" ")
    file.write("\n")
    
    # Cosmetics
    os.system('clear')
    print("| Forging [===   ]")
    time.sleep(0.2)

    # .o files (OBJ)
    file.write("OBJ = ")
    for i in out_cfiles:
        file.write(i + " ")
    file.write("\n")
    file.write("\n")

    # Cosmetics
    os.system('clear')
    print("/ Forging [====  ]")
    time.sleep(0.2)

    # Rule: Target
    file.write(exe_name + ": $(OBJ)")
    file.write("\n")
    file.write("\t")
    file.write("$(CC) $(OBJ) $(CFLAGS) -o " + exe_name)
    file.write("\n")
    file.write("\n")

    # Cosmetics
    os.system('clear')
    print("- Forging [===== ]")
    time.sleep(0.2)

    # Rule: Output file instructions
    file.write("$(OBJ): $(SOURCE) $(DEPS)\n")
    file.write("\t")
    file.write("$(CC) $(SOURCE) $(CFLAGS) -c")
    file.write("\n")

    # Rule: Depandancies
    file.write("$(DEPS): $(SOURCE)")
    file.write("\n")
    file.write("\t")
    file.write("$(CC) -MM $(CFLAGS) -o $@ $<")
    file.write("\n")
    file.write("\n")
    file.write("-include")

    # Cosmetics
    os.system('clear')
    print("\\ Forging [======]")
    time.sleep(0.2)

    print("Forge Successful")
    time.sleep(1)

# Optional Make
def opt_make():
    """Optional make command after generation"""
    if user_i("Make executable?") == "y":
        os.system("make")
        print("Makefile complete, executable compiled.")
        time.sleep(2)
    menu()

##  MENU  ##

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
        opt_make()
    elif main_menu == "2":
        exit()
    else:
        menu()

menu()

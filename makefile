CC = gcc
CFLAGS = -Wall -g 
DEPS = 
SOURCE = main.c thing.c 
OBJ = main.o thing.o 

Output: $(OBJ)
	$(CC) $(OBJ) $(CFLAGS) -o Output

$(OBJ): $(SOURCE) $(DEPS)
	$(CC) $(SOURCE) $(CFLAGS) -c
$(DEPS): $(SOURCE)
	$(CC) -MM $(CFLAGS) -o $@ $<

-include
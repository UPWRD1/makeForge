CC = gcc
CFLAGS = -Wall -g 
DEPS = thing.h 
SOURCE = thing.c 
OBJ = thing.o 
output: $(OBJ)
	$(CC) $(OBJ) $(CFLAGS) -o output

$(OBJ): $(SOURCE) $(DEPS)
	$(CC) $(SOURCE) $(CFLAGS) -c
$(DEPS): $(SOURCE)
	$(CC) -MM $(CFLAGS) -o $@ $<

-include
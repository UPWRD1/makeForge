CC = gcc
CFLAGS = -Wall -g 
DEPS = common.h thing.h 
SOURCE = main.c thing.c 
OBJ = main.o thing.o 

output: $(OBJ)
	$(CC) $(OBJ) $(CFLAGS) -o output

$(OBJ): $(SOURCE) $(DEPS)
	$(CC) $(SOURCE) $(CFLAGS) -c
$(DEPS): $(SOURCE)
	$(CC) -MM $(CFLAGS) -o $@ $<

-include
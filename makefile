CC = GCC
CFLAGS = -Wall -g 
DEPS = common.h thing.h 
OBJ = main.o thing.o common.o 

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

output: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
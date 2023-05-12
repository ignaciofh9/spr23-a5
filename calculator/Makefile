CC = gcc
CFLAGS = -Wall -Werror

TARGET = calculator

all: $(TARGET)

$(TARGET): main.o addition.o subtraction.o multiplication.o division.o
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o $(TARGET)
.PHONY: clean

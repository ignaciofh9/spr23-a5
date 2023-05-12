objects = addition.o subtraction.o multiplication.o division.o
sample: $(objects)
 cc -o sample $(objects)
$(objects): %.o:%.c
 cc -c $< -o $@
clean:
 rm -f sample $(objects)
.PHONY: clean

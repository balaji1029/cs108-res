main: maximum.o minimum.o main.o
	g++ -o $@ $^

%.o: src/%.cpp
	g++ -c $< -o $@

.PHONY: clean

clean:
	rm -rf *.o main 
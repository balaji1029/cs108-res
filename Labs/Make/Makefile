OBJ1 := comp.o find.o ops.o
OBJ2 := add.o rem.o
MAIN := main1 main2 main3 main4 main5 main6 main7 main8 main9
FlAGS := -Wall --std=c++17

all: $(MAIN) $(OBJ1) $(OBJ2)

%.o: src/src1/%.cpp
	g++ $(FlAGS) -c $< -o $@

%.o: src/src2/%.cpp
	g++ $(FlAGS) -c $< -o $@
    
%: $(OBJ1) $(OBJ2) ./main/%.cpp
	g++ $(FlAGS) main/$@.cpp $(OBJ1) $(OBJ2) -o $@

.PHONY: clean

clean:
	rm -f *.o main*
CC=g++ --std=c++11

all: Main.o
	
Particle.o: Particle.cpp
	$(CC) -c Particle.cpp
Vector.o: Vector.cpp
	$(CC) -c Vector.cpp

Main.o: main.cpp Particle.cpp Vector.cpp MatPoint.cpp 
	$(CC) -o main main.cpp Vector.cpp MatPoint.cpp Particle.cpp 
	./main
 

clean:
	rm *.o
	
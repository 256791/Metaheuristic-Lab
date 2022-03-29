g++ -c -fPIC nearest_neighbour.cpp -o nearest_neighbour.o
g++ -shared -o nearest_neighbour.so  nearest_neighbour.o
rm nearest_neighbour.o
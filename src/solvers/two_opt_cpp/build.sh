g++ -c -fPIC two_opt.cpp -o two_opt.o
g++ -shared -Wl,-soname,two_opt.so -o two_opt.so  two_opt.o
rm two_opt.o
# data.make

Manager : Manager.o LinkedList.o ArrayList.o
	g++ -o Manager LinkedList.o ArrayList.o

Manager.o : Manager.cpp
	g++ -c Manager.cpp

LinkedList.o : LinkedList.cpp
	g++ -c LinkedList.cpp

ArrayList.o : ArrayList.cpp
	g++ -c ArrayList.cpp

clean :
	@rm Manager LinkedList.o ArrayList.o

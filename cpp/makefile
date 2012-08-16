# data.make

BUILD_DIR = build

Manager : Manager.o LinkedList.o ArrayList.o
	g++ -o Manager $(BUILD_DIR)/Manager.o $(BUILD_DIR)/LinkedList.o $(BUILD_DIR)/ArrayList.o

Manager.o : Manager.cpp
	g++ -o $(BUILD_DIR)/Manager.o -c Manager.cpp

LinkedList.o : LinkedList.cpp
	g++ -o $(BUILD_DIR)/LinkedList.o -c LinkedList.cpp

ArrayList.o : ArrayList.cpp
	g++ -o $(BUILD_DIR)/ArrayList.o -c ArrayList.cpp

clean :
	@rm Manager $(BUILD_DIR)/* 

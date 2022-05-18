CC = g++
CPPFLAGS = -Wall -std=c++17 -pthread -O3

SRC_DIR = src
OBJ_DIR = build

TARGET = tabu

SRC := $(wildcard $(SRC_DIR)/*.cpp)
OBJ := $(SRC:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CPPFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp | $(OBJ_DIR)
	$(CC) $(CPPFLAGS) -c $< -o $@

clean:
	$(RM) -rv $(OBJ_DIR)
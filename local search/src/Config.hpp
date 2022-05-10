#ifndef CONFIG_HPP
#define CONFIG_HPP
#include <string>
using namespace std;

enum Mode
{
  invert,
  swap,
  insert
};

class Config
{
public:
  Mode mode = Mode::invert;
  int max_tabu = 1000;
  int max_iter = 10000;
  int max_depth = 1000;
  int threads = 4;
  string input = "";
  bool clearTabu = false;

  string parse(int argc, char **argv);
};
#endif
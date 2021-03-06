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
  int max_imp_iter = 1000;
  int threads = 4;
  string input = "";
  string path_input = "";
  bool clearTabu = false;
  bool printDebug = false;

  string parse(int argc, char **argv);
};
#endif
#ifndef CONFIG_HPP
#define CONFIG_HPP
#include <string>
using namespace std;

enum Mode
{
  invert,
  swap
};

class Config
{
public:
  Mode mode = Mode::invert;
  int max_tabu = 1000;
  int max_iter = 10000;
  int max_iter_imp = 1000;
  string input = "";

  string parse(int argc, char **argv);
};
#endif
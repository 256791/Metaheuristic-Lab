#include "Config.hpp"
#include <cstring>

using namespace std;

string Config::parse(int argc, char **argv)
{
  for (int i = 1; i < argc; i++)
  {
    if (strcmp(argv[i], "-max_iter") == 0)
    {
      if (++i == argc)
        return "missing value for -max_iter";
      max_iter = atoi(argv[i]);
      if (max_iter < 10)
        return "-max_iter should be at least 10";
    }
    else if (strcmp(argv[i], "-max_iter_imp") == 0)
    {
      if (++i == argc)
        return "missing value for -max_iter_imp";
      max_iter_imp = atoi(argv[i]);
      if (max_iter_imp < 10)
        return "-max_iter_imp should be at least 10";
    }
    else if (strcmp(argv[i], "-max_tabu") == 0)
    {
      if (++i == argc)
        return "missing value for -max_tabu";
      max_tabu = atoi(argv[i]);
      if (max_tabu < 5)
        return "-max_tabu should be at least 5";
    }
    else if (strcmp(argv[i], "-mode") == 0)
    {
      if (++i == argc)
        return "missing value for -mode";
      if (strcmp(argv[i], "invert") == 0)
        mode = Mode::invert;
      else if (strcmp(argv[i], "swap") == 0)
        mode = Mode::swap;
      else
        return "unrecognized value for -mode";
    }
    else if (strcmp(argv[i], "-input") == 0)
    {
      if (++i == argc)
        return "missing value for -input";
      input = argv[i];
    }
    else
      return "unrecognized argument";
  }

  if (input == "")
    return "missing input filename";

  return "";
}
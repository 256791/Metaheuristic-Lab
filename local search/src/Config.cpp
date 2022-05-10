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
      if (max_iter < 1)
        return "-max_iter should be at least 1";
    }
    else if (strcmp(argv[i], "-max_depth") == 0)
    {
      if (++i == argc)
        return "missing value for -max_depth";
      max_depth = atoi(argv[i]);
      if (max_depth < 1)
        return "-max_depth should be at least 1";
    }
    else if (strcmp(argv[i], "-max_tabu") == 0)
    {
      if (++i == argc)
        return "missing value for -max_tabu";
      max_tabu = atoi(argv[i]);
      if (max_tabu < 1)
        return "-max_tabu should be at least 1";
    }
    else if (strcmp(argv[i], "-threads") == 0)
    {
      if (++i == argc)
        return "missing value for -threads";
      threads = atoi(argv[i]);
      if (threads < 1)
        return "-threads should be at least 1";
    }
    else if (strcmp(argv[i], "-mode") == 0)
    {
      if (++i == argc)
        return "missing value for -mode";
      if (strcmp(argv[i], "invert") == 0)
        mode = Mode::invert;
      else if (strcmp(argv[i], "swap") == 0)
        mode = Mode::swap;
      else if (strcmp(argv[i], "insert") == 0)
        mode = Mode::insert;
      else
        return "unrecognized value for -mode";
    }
    else if (strcmp(argv[i], "-input") == 0)
    {
      if (++i == argc)
        return "missing value for -input";
      input = argv[i];
    }
    else if (strcmp(argv[i], "-clear_tabu") == 0)
    {
      clearTabu = true;
    }
    else
      return "unrecognized argument";
  }

  if (input == "")
    return "missing input filename";

  return "";
}
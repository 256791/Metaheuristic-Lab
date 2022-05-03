#ifndef TWO_OPT_H
#define TWO_OPT_H
#include "TSPTabu.hpp"
#include <algorithm>
#include <iostream>

class TwoOptSolution : public TSPSolution
{
public:
  TSPSolution *parrent;
  pair<int, int> invert;

  TwoOptSolution(TSPSolution *parrent, pair<int, int> invert, double cost);

  pair<int, int> tabu() override;

  vector<int> getPath();
  static vector<Solution *> twoOptNeighbourhood(Problem *p, Solution *s);
};


#endif
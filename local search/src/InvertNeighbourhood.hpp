#ifndef INVERT_NEIGHBOURHOOD_H
#define INVERT_NEIGHBOURHOOD_H
#include "TSPTabu.hpp"
#include <algorithm>
#include <iostream>

class InvertNeighbourhood : public TSPSolution
{
public:
  TSPSolution *parrent;
  pair<int, int> invert;

  InvertNeighbourhood(TSPSolution *parrent, pair<int, int> invert, double cost);

  pair<int, int> tabu() override;

  vector<int> getPath();
  static vector<Solution *> twoOptNeighbourhood(Problem *p, Solution *s);
};


#endif
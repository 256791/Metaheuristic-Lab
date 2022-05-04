#ifndef SWAP_NEIGHBOURHOOD_H
#define SWAP_NEIGHBOURHOOD_H
#include "TSPTabu.hpp"
#include <algorithm>
#include <iostream>

class SwapNeighbourhood : public TSPSolution
{
public:
  TSPSolution *parrent;
  pair<int, int> swap;

  SwapNeighbourhood(TSPSolution *parrent, pair<int, int> swap, double cost);

  pair<int, int> tabu() override;

  vector<int> getPath();
  static vector<Solution *> swapNeighbourhood(Problem *p, Solution *s);
};


#endif
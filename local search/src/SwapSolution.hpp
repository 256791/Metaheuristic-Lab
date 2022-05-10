#ifndef SWAP_SOLUTION_H
#define SWAP_SOLUTION_H
#include "TSPTabu.hpp"
#include <iostream>

class SwapSolution: public TSPSolution
{
public:
  SwapSolution(TSPProblem *problem);
  SwapSolution(TSPSolution *parrent, pair<int, int> t, double cost);

  vector<int> getPath() override;
  static void neighbourhood(NeighbourhoodParams p);
  // static vector<Solution *> neighbourhood(Problem *p, Solution *s);
};


#endif
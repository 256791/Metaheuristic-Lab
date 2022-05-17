#ifndef INVERT_SOLUTION_H
#define INVERT_SOLUTION_H
#include "TSPTabu.hpp"
#include <algorithm>
#include <iostream>

class InvertSolution : public TSPSolution
{
public:
  InvertSolution(TSPProblem *problem);
  InvertSolution(TSPSolution *parrent, pair<int, int> t, double cost);

  vector<int> getPath() override;
  static void neighbourhood(NeighbourhoodParams p);
  // static vector<Solution *> neighbourhood(Problem *p, Solution *s);
  ~InvertSolution() = default;
};
#endif
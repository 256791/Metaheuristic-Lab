#ifndef INSERT_SOLUTION_H
#define INSERT_SOLUTION_H
#include "TSPTabu.hpp"
#include <iostream>

class InsertSolution : public TSPSolution
{
public:
  InsertSolution(TSPProblem *problem);
  InsertSolution(TSPSolution *parrent, pair<int, int> t, double cost);

  vector<int> getPath() override;
  static void neighbourhood(NeighbourhoodParams p);
  // static vector<Solution *> neighbourhood(Problem *p, Solution *s);
};
#endif
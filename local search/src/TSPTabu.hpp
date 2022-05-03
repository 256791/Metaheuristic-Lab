#ifndef TSP_TABU_H
#define TSP_TABU_H
#include "TabuSearch.hpp"
#include <stdexcept>

class TSPSolution : public Solution
{
public:
  bool cached = false;
  double cost = 0.0;
  int size = 0;
  vector<int> path;

  // COPY?
  vector<int> getPath();
  pair<int, int> tabu() override;
};

class TSPProblem : public Problem
{
private:
  vector<vector<double>> matrix;

public:
  TSPProblem(vector<vector<double>> mat);

  double cost(int a, int b);

  int size();

  double eval(Solution *s) override;
};
#endif
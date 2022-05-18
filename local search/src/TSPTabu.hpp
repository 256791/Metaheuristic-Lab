#ifndef TSP_TABU_H
#define TSP_TABU_H
#include "TabuSearch.hpp"
#include <stdexcept>
class TSPProblem;
class TSPSolution;
struct NeighbourhoodParams
{
  TSPProblem *problem;
  TSPSolution *solution;
  double cost;
  vector<int> path;
  int start;
  int end;
  vector<Solution *> *ret;
};

class TSPProblem : public Problem
{
public:
  vector<vector<double>> matrix;
  TSPProblem() = default;
  TSPProblem(vector<vector<double>> mat);

  bool fromFile(string filename);

  double cost(int a, int b);
  int size();
  double eval(Solution *s) override;
};

class TSPSolution : public Solution
{
public:
  bool cached = false;
  double cost = 0.0;
  int size = 0;
  vector<int> path;
  TSPSolution *parrent;
  pair<int, int> t;

  TSPSolution(TSPProblem *problem);
  TSPSolution(TSPProblem *problem, vector<int> initial);
  TSPSolution(TSPSolution *parrent, pair<int, int> swap, double cost);

  pair<int, int> tabu() override;

  virtual vector<int> getPath();

  virtual bool match(Solution *rhs) override;

  static vector<Solution *> neighbourhoodThreaded(Problem *problem, Solution *solution, void(*neighbourhood)(NeighbourhoodParams), int threads);
  // static vector<Solution *> neighbourhoodThreaded(Problem *problem, Solution *solution, function<vector<Solution *>(NeighbourhoodParams *)> neighbourhood, int threads);

};
#endif
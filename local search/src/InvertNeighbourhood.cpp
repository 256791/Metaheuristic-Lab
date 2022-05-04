#include "InvertNeighbourhood.hpp"
InvertNeighbourhood::InvertNeighbourhood(TSPSolution *parrent, pair<int, int> invert, double cost)
{
  this->parrent = parrent;
  this->size = parrent->size;
  this->invert = invert;
  this->cached = true;
  this->cost = cost;
}

pair<int, int> InvertNeighbourhood::tabu()
{
  return this->invert;
}

vector<int> InvertNeighbourhood::getPath()
{
  if (path.size() == size)
    return path;

  // COPY?
  path = parrent->getPath();
  reverse(path.begin() + invert.first, path.begin() + invert.second);
  return path;
}

vector<Solution *> InvertNeighbourhood::twoOptNeighbourhood(Problem *p, Solution *s)
{
  TSPProblem *problem;
  if (!(problem = dynamic_cast<TSPProblem *>(p)))
    throw runtime_error("Trying to find two opt neighborhood from non tsp problem");

  InvertNeighbourhood *solution;
  if (!(solution = dynamic_cast<InvertNeighbourhood *>(s)))
  {
    throw runtime_error("Trying to find two opt neighborhood from non two opt solution");
  }
  vector<int> path = solution->getPath();

  vector<Solution *> solutions;

  for (int i = 0; i < problem->size() - 1; i++)
  {
    for (int j = i + 1; j < problem->size(); j++)
    {
      // optimize form O(n) to O(1) for non directional graphs
      vector<int> npath(path);
      reverse(npath.begin() + i, npath.begin() + j);
      double cost = 0.0;
      for (int i = 0; i < npath.size() - 1; i++)
      {
        cost += problem->cost(npath[i], npath[i + 1]);
      }
      cost += problem->cost(npath[npath.size() - 1], npath[0]);
      solutions.push_back(new InvertNeighbourhood(solution, pair<int, int>(i, j), cost));
    }
  }

  return solutions;
}

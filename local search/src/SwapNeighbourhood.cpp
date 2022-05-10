#include "SwapNeighbourhood.hpp"

SwapNeighbourhood::SwapNeighbourhood(TSPProblem *problem)
{
  this->size = problem->size();
  for (int i = 0; i < problem->matrix.size(); i++)
    this->path.push_back(i);
  problem->eval(this);
}

SwapNeighbourhood::SwapNeighbourhood(TSPSolution *parrent, pair<int, int> swap, double cost)
{
  this->parrent = parrent;
  this->size = parrent->size;
  this->swap = swap;
  this->cached = true;
  this->cost = cost;
}

pair<int, int> SwapNeighbourhood::tabu()
{
  return this->swap;
}

vector<int> SwapNeighbourhood::getPath()
{
  if (path.size() == size)
    return path;

  path = parrent->getPath();
  int temp = path[swap.first];
  path[swap.first] = path[swap.second];
  path[swap.second] = temp;
  return path;
}

vector<Solution *> SwapNeighbourhood::neighbourhood(Problem *p, Solution *s)
{
  TSPProblem *problem;
  if (!(problem = dynamic_cast<TSPProblem *>(p)))
    throw runtime_error("Trying to find two opt neighborhood from non tsp problem");

  SwapNeighbourhood *solution;
  if (!(solution = dynamic_cast<SwapNeighbourhood *>(s)))
    throw runtime_error("Trying to find two opt neighborhood from non two opt solution");

  vector<int> path = solution->getPath();

  vector<Solution *> solutions;

  for (int i = 0; i < problem->size() - 1; i++)
  {
    for (int j = i + 1; j < problem->size(); j++)
    {
      vector<int> npath(path);

      int temp = npath[i];
      npath[i] = npath[j];
      npath[j] = temp;

      double cost = solution->cost;

      cost -= problem->cost(path[i == 0 ? path.size() - 1 : i - 1], path[i]);
      cost -= problem->cost(path[i], path[i + 1]);
      cost -= problem->cost(path[j - 1], path[j]);
      cost -= problem->cost(path[j], path[j == path.size() - 1 ? 0 : j + 1]);

      cost += problem->cost(npath[i == 0 ? npath.size() - 1 : i - 1], npath[i]);
      cost += problem->cost(npath[i], npath[i + 1]);
      cost += problem->cost(npath[j - 1], npath[j]);
      cost += problem->cost(npath[j], npath[j == npath.size() - 1 ? 0 : j + 1]);

      solutions.push_back(new SwapNeighbourhood(solution, pair<int, int>(i, j), cost));
    }
  }

  return solutions;
}
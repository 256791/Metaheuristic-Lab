#include "InvertSolution.hpp"
#include <thread>

InvertSolution::InvertSolution(TSPProblem *problem) : TSPSolution(problem) {}
InvertSolution::InvertSolution(TSPSolution *parrent, pair<int, int> t, double cost) : TSPSolution(parrent, t, cost) {}

vector<int> InvertSolution::getPath()
{
  if (path.size() == size)
    return path;

  path = parrent->getPath();
  reverse(path.begin() + t.first, path.begin() + t.second);
  return path;
}

void InvertSolution::neighbourhood(NeighbourhoodParams p)
{
  InvertSolution *solution;
  if (!(solution = dynamic_cast<InvertSolution *>(p.solution)))
    throw runtime_error("Trying to find two opt neighborhood from non two opt solution");

  for (int i = p.start; i < p.end - 1; i++)
  {
    for (int j = i + 1; j < p.problem->size(); j++)
    {
      vector<int> npath = p.path;
      reverse(npath.begin() + i, npath.begin() + j);
      double cost = 0.0;
      for (int k = 0; k < npath.size() - 1; k++)
      {
        cost += p.problem->cost(npath[k], npath[k + 1]);
      }
      cost += p.problem->cost(npath[npath.size() - 1], npath[0]);
      p.ret->push_back(new InvertSolution(solution, pair<int, int>(i, j), cost));
    }
  }
}

// vector<Solution *> InvertSolution::neighbourhood(Problem *p, Solution *s)
// {
//   TSPProblem *problem;
//   if (!(problem = dynamic_cast<TSPProblem *>(p)))
//     throw runtime_error("Trying to find two opt neighborhood from non tsp problem");

//   InvertSolution *solution;
//   if (!(solution = dynamic_cast<InvertSolution *>(s)))
//   {
//     throw runtime_error("Trying to find two opt neighborhood from non two opt solution");
//   }
//   vector<int> path = solution->getPath();
//   vector<Solution *> solutions;

//   for (int i = 0; i < problem->size() - 1; i++)
//   {
//     for (int j = i + 1; j < problem->size(); j++)
//     {
//       // optimize form O(n) to O(1) for non directional graphs
//       vector<int> npath(path);
//       reverse(npath.begin() + i, npath.begin() + j);
//       double cost = 0.0;
//       for (int k = 0; k < npath.size() - 1; k++)
//       {
//         cost += problem->cost(npath[k], npath[k + 1]);
//       }
//       cost += problem->cost(npath[npath.size() - 1], npath[0]);
//       solutions.push_back(new InvertSolution(solution, pair<int, int>(i, j), cost));
//     }
//   }
//   return solutions;
// }

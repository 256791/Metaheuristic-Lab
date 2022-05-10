#include "InsertSolution.hpp"

InsertSolution::InsertSolution(TSPProblem *problem) : TSPSolution(problem) {}
InsertSolution::InsertSolution(TSPSolution *parrent, pair<int, int> t, double cost) : TSPSolution(parrent, t, cost) {}

vector<int> InsertSolution::getPath()
{
  if (path.size() == size)
    return path;

  path = parrent->getPath();


  // int tmp = path[t.first];
  // for(int i=t.first;i<=t.second;i++){
  //   path[i] = path[i+1];
  // }
  // path[t.second] = tmp;

  int temp = path[t.second];
  for (int i = t.second; i > t.first; i--)
    path[i] = path[i-1];
  path[t.first] = temp;

  return path;
}

void InsertSolution::neighbourhood(NeighbourhoodParams p)
{
  InsertSolution *solution;
  if (!(solution = dynamic_cast<InsertSolution *>(p.solution)))
    throw runtime_error("Trying to find two opt neighborhood from non two opt solution");

  for (int i = p.start; i < p.end - 1; i++)
  {
    for (int j = i + 1; j < p.problem->size(); j++)
    {
      vector<int> npath(p.path);
      
      int temp = npath[j];
      for (int k = j; k > i; k--)
        npath[k] = npath[k-1];
      npath[i] = temp;
    // int tmp = npath[i];
    // for(int k=i;k<=j;k++){
    //     npath[k] = npath[k+1];
    // }
    // npath[j] = tmp;
      double cost = 0.0;
      for (int k = 0; k < npath.size() - 1; k++)
      {
        cost += p.problem->cost(npath[k], npath[k + 1]);
      }
      cost += p.problem->cost(npath[npath.size() - 1], npath[0]);
    //   double cost = solution->cost;
    //   cost -= p.problem->cost(p.path[i == 0 ? p.path.size() - 1 : i - 1], p.path[i]);
    // //   cost -= p.problem->cost(p.path[i], p.path[i + 1]);
    //   cost -= p.problem->cost(p.path[j - 1], p.path[j]);
    //   cost -= p.problem->cost(p.path[j], p.path[j == p.path.size() - 1 ? 0 : j + 1]);

    //   cost += p.problem->cost(npath[i == 0 ? npath.size() - 1 : i - 1], npath[i]);
    // //   cost += p.problem->cost(npath[i], npath[i + 1]);
    //   cost += p.problem->cost(npath[j - 1], npath[j]);
    //   cost += p.problem->cost(npath[j], npath[j == npath.size() - 1 ? 0 : j + 1]);
     
      p.ret->push_back(new InsertSolution(solution, pair<int, int>(i, j), cost));
    }
  }
}

// vector<Solution *> InsertSolution::neighbourhood(Problem *p, Solution *s)
// {
//   TSPProblem *problem;
//   if (!(problem = dynamic_cast<TSPProblem *>(p)))
//     throw runtime_error("Trying to find two opt neighborhood from non tsp problem");

//   InsertSolution *solution;
//   if (!(solution = dynamic_cast<InsertSolution *>(s)))
//   {
//     throw runtime_error("Trying to find two opt neighborhood from non two opt solution");
//   }
//   vector<int> path = solution->getPath();

//   vector<Solution *> solutions;

//   for (int i = 0; i < problem->size() - 1; i++)
//   {
//     for (int j = i + 1; j < problem->size(); j++)
//     {
//       vector<int> npath(path);
//       int temp = path[j];

//       for (int k = i; k < j; k++)
//         path[k + 1] = path[k];
//       path[i] = temp;

//       double cost = solution->cost;
//       cost -= problem->cost(path[i == 0 ? path.size() - 1 : i - 1], path[i]);
//       cost -= problem->cost(path[i], path[i + 1]);
//       cost -= problem->cost(path[j - 1], path[j]);
//       cost -= problem->cost(path[j], path[j == path.size() - 1 ? 0 : j + 1]);

//       cost += problem->cost(npath[i == 0 ? npath.size() - 1 : i - 1], npath[i]);
//       cost += problem->cost(npath[i], npath[i + 1]);
//       cost += problem->cost(npath[j - 1], npath[j]);
//       cost += problem->cost(npath[j], npath[j == npath.size() - 1 ? 0 : j + 1]);
     
//       solutions.push_back(new InsertSolution(solution, pair<int, int>(i, j), cost));
//     }
//   }

//   return solutions;
// }

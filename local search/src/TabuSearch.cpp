#include "TabuSearch.hpp"
#include <iostream>

Solution::Solution() {}

Problem::Problem() {}

TabuSearch::TabuSearch(Problem *problem, function<vector<Solution *>(Solution *)> neighbourhood, long unsigned int maxTabuSize)
{
  this->neighbourhood = neighbourhood;
  this->problem = problem;
}

bool TabuSearch::checkTabu(Solution *solution)
{
  return (tabuList.find(solution->tabu()) == tabuList.end());
}

void TabuSearch::addTabu(Solution *solution)
{
  tabuList[solution->tabu()] = tabuId;
  tabuQueue.push(solution->tabu());
  tabuId++;

  if (tabuQueue.size() > maxTabuSize)
  {
    tabuList.erase(tabuQueue.front());
    tabuQueue.pop();
  }
}

Solution *TabuSearch::search(Solution *initial, long unsigned int maxIter)
{
  solution = initial;
  best = problem->eval(solution);
  Solution *current = initial;
  long unsigned int iter = 0;
  do
  {
    vector<Solution *> solutions = neighbourhood(current);
    Solution *next = nullptr;
    double nextBest = numeric_limits<double>::infinity();
    for (auto el : solutions)
    {
      if (nextBest > problem->eval(el))
      {
        if (checkTabu(el) || problem->eval(el) < best)
        {
          next = el;
          nextBest = problem->eval(el);
        }
      }
    }
    if (next == nullptr)
    {
      cout << "tabu clear\n";
      tabuList.clear();
      while(!tabuQueue.empty())
        tabuQueue.pop();
    }else{
      current = next;
      addTabu(current);
      if (nextBest < best)
      {
        solution = next;
        best = nextBest;
      }
      iter++;
    }
  } while (iter < maxIter);

  return solution;
}
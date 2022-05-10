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
  bool found = false;
  for (auto el : visited)
  {
    if (el->match(solution))
    {
      // cout << ":)\n";
      found = true;
      break;
    }
  }

  return (!found && tabuList.find(solution->tabu()) == tabuList.end());
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

void TabuSearch::clearTabu()
{
  tabuList.clear();
  while (!tabuQueue.empty())
    tabuQueue.pop();
}

Solution *TabuSearch::search(Solution *initial, long unsigned int maxIter, int max_depth, bool clear)
{
  solution = initial;
  best = problem->eval(solution);

  Solution *current = initial;
  long unsigned int iter = 0;
  long unsigned int impiter = 0;
  bool improved = false;
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
      clearTabu();
    }
    else
    {
      current = next;
      addTabu(current);
      if (improved)
      {
        visited.push_back(next);
        improved = false;
      }
      else if (impiter == max_depth)
      {
        if(clear)
          clearTabu();
        current = solution;
        impiter = 0;
        improved = true;
      }
      if (nextBest < best)
      {
        improved = true;
        solution = next;
        best = nextBest;
        visited.clear();
        impiter = 0;
      }
    }
    iter++;
    impiter++;
  } while (iter < maxIter);
  return solution;
}
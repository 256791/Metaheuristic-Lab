#include "TSPTabu.hpp"
#include <iostream>
#include <fstream>
#include <thread>

TSPSolution::TSPSolution(TSPProblem *problem)
{
  this->size = problem->size();
  for (int i = 0; i < problem->matrix.size(); i++)
    this->path.push_back(i);
  problem->eval(this);
}

TSPSolution::TSPSolution(TSPSolution *parrent, pair<int, int> t, double cost)
{
  this->parrent = parrent;
  this->size = parrent->size;
  this->t = t;
  this->cached = true;
  this->cost = cost;
}

vector<int> TSPSolution::getPath()
{
  return path;
}
pair<int, int> TSPSolution::tabu()
{
  return this->t;
}

TSPProblem::TSPProblem(vector<vector<double>> mat)
{
  matrix = mat;
}

double TSPProblem::cost(int a, int b)
{
  return matrix[a][b];
}

int TSPProblem::size()
{
  return matrix.size();
};

double TSPProblem::eval(Solution *s)
{
  TSPSolution *solution;
  if (!(solution = dynamic_cast<TSPSolution *>(s)))
    throw runtime_error("Trying to evaluate Non TSP solution");

  if (solution->cached)
    return solution->cost;
  else
  {
    vector<int> path = solution->getPath();
    if (path.size() != matrix.size())
      throw logic_error("Wrong path WIP");

    double cost = 0.0;
    for (int i = 0; i < path.size() - 1; i++)
      cost += matrix[path[i]][path[i + 1]];

    cost += matrix[path[path.size() - 1]][path[0]];
    solution->cached = true;
    solution->cost = cost;
    return cost;
  }
}

bool TSPProblem::fromFile(string filename)
{
  system(("python3 convert.py " + filename).c_str());
  fstream in("data/" + filename);
  matrix.clear();

  int size, val;
  if (!(in >> size))
    return false;

  for (int i = 0; i < size; i++)
  {
    vector<double> row;
    for (int j = 0; j < size; j++)
    {
      if (!(in >> val))
        return false;

      row.push_back(val);
    }
    matrix.push_back(row);
  }
  return true;
}

bool TSPSolution::match(Solution *rhs)
{
  TSPSolution *solution;
  if (!(solution = dynamic_cast<TSPSolution *>(rhs)))
    return false;

  if (this->parrent != solution->parrent && this->cached && solution->cached)
    return this->getPath() == solution->getPath();

  return (this->parrent == solution->parrent && this->t == solution->t);
}
// function<vector<Solution *>(NeighbourhoodParams *)> neighbourhood
vector<Solution *> TSPSolution::neighbourhoodThreaded(Problem *p, Solution *s, void (*neighbourhood)(NeighbourhoodParams), int threads)
{
  TSPProblem *problem;
  if (!(problem = dynamic_cast<TSPProblem *>(p)))
    throw runtime_error("Trying to find two opt neighborhood from non tsp problem");

  TSPSolution *solution;
  if (!(solution = dynamic_cast<TSPSolution *>(s)))
    throw runtime_error("Trying to find two opt neighborhood from non two opt solution");

  vector<Solution *> *ret = new vector<Solution *>[threads];
  NeighbourhoodParams *params = new NeighbourhoodParams[threads];
  thread **tr = new thread *[threads];

  int range = 0;
  for (int i = 0; i < threads; i++)
  {
    params[i].problem = problem;
    params[i].solution = solution;
    params[i].path = solution->getPath();
    params[i].start = range;
    if (i == threads - 1)
      range = problem->size() - 1;
    else
      range += problem->size() / threads;
    params[i].end = range + 1;
    params[i].ret = &ret[i];
    tr[i] = new thread(neighbourhood, params[i]);
  }
  int allocsize = 0;
  for (int i = 0; i < threads; i++)
  {
    tr[i]->join();
    delete tr[i];
    allocsize += ret[i].size();
  }
  delete[] tr;

  vector<Solution *> solutions;
  solutions.reserve(allocsize);
  for (int i = 0; i < threads; i++)
    solutions.insert(solutions.end(), ret[i].begin(), ret[i].end());
  delete[] params;
  delete[] ret;
  return solutions;
}

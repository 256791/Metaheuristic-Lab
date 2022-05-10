#include "TSPTabu.hpp"
#include <iostream>
#include <fstream>

vector<int> TSPSolution::getPath()
{
  return path;
}
pair<int, int> TSPSolution::tabu()
{
  return pair<int, int>(0, 0);
}

TSPProblem::TSPProblem(vector<vector<double>> mat)
{
  matrix = mat;
}

double TSPProblem::cost(int a, int b)
{
  return matrix[a][b];
}

int TSPProblem::size(){
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

bool TSPProblem::fromFile(string filename){
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
};
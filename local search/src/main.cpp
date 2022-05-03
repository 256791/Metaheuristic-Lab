#include "TabuSearch.hpp"
#include "TSPTabu.hpp"
#include "TwoOpt.hpp"
#include "mat.hpp"
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
  if (argc > 1)
  {
    fstream in(argv[1]);
    int size, val;
    in >> size;
    cout << "Problem size " << size << endl;
    vector<vector<double>> mat;
    for (int i = 0; i < size; i++)
    {
      vector<double> row;
      for (int j = 0; j < size; j++){
        in >> val;
        row.push_back(val);
      }
      mat.push_back(row);
    }

    TSPProblem problem(mat);
    TSPSolution s;
    for (int i = 0; i < size; i++)
      s.path.push_back(i);
    problem.eval(&s);
    s.size = size;
    TwoOptSolution initial(&s, pair<int, int>(0, 0), s.cost);

    using std::placeholders::_1;
    function<vector<Solution *>(Solution *)> neighbourhood = bind(&TwoOptSolution::twoOptNeighbourhood, &problem, _1);

    TabuSearch ts(&problem, neighbourhood, 100);
    Solution *sol = ts.search(&initial, 10000);

    TSPSolution *solution = dynamic_cast<TSPSolution *>(sol);

    cout << solution->cost << '\n';
  }
  return 0;
}
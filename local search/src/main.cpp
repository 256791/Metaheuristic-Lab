#include "TabuSearch.hpp"
#include "TSPTabu.hpp"
#include "SwapNeighbourhood.hpp"
#include "InvertNeighbourhood.hpp"
#include "Config.hpp"
#include <iostream>
#include <climits>

using namespace std;

int main(int argc, char **argv)
{
  Config cnf;
  string err = cnf.parse(argc, argv);
  if (err != "")
  {
    cerr << err << endl;
    return 0;
  }

  TSPProblem *problem = new TSPProblem();
  if (!problem->fromFile(cnf.input))
  {
    cerr << "Problem loading error" << endl;
    return 0;
  }

  function<vector<Solution *>(Solution *)> neighbourhood;
  TSPSolution *initial;
  if (cnf.mode == Mode::invert)
  {
    initial = new InvertNeighbourhood(problem);
    using std::placeholders::_1;
    neighbourhood = bind(&InvertNeighbourhood::neighbourhood, problem, _1);
  }
  else if (cnf.mode == Mode::swap)
  {
    initial = new SwapNeighbourhood(problem);
    using std::placeholders::_1;
    neighbourhood = bind(&SwapNeighbourhood::neighbourhood, problem, _1);
  }

  TabuSearch ts(problem, neighbourhood, cnf.max_tabu);
  Solution *sol = ts.search(initial, cnf.max_iter);
  TSPSolution *solution = dynamic_cast<TSPSolution *>(sol);
  cout << solution->cost << '\n';

  return 0;
}
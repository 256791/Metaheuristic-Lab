#include "TabuSearch.hpp"
#include "TSPTabu.hpp"
#include "SwapSolution.hpp"
#include "InvertSolution.hpp"
#include "InsertSolution.hpp"
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
  // cout << "Problem size: " << problem->size() << '\n';

  function<vector<Solution *>(Solution *)> neighbourhood;
  TSPSolution *initial;
  
  if (cnf.mode == Mode::invert)
  {
    initial = new InvertSolution(problem);
    using std::placeholders::_1;
    neighbourhood = bind(&TSPSolution::neighbourhoodThreaded, problem, _1, &InvertSolution::neighbourhood, cnf.threads);
  }
  else if (cnf.mode == Mode::swap)
  {
    initial = new SwapSolution(problem);
    using std::placeholders::_1;
    neighbourhood = bind(&TSPSolution::neighbourhoodThreaded, problem, _1, &SwapSolution::neighbourhood, cnf.threads);
  }
  else if (cnf.mode == Mode::insert)
  {
    initial = new InsertSolution(problem);
    using std::placeholders::_1;
    neighbourhood = bind(&TSPSolution::neighbourhoodThreaded, problem, _1, &InsertSolution::neighbourhood, cnf.threads);
  }

  TabuSearch ts(problem, neighbourhood, cnf.max_tabu);
  Solution *sol = ts.search(initial, cnf.max_iter, cnf.max_depth, cnf.max_imp_iter, cnf.clearTabu);
  TSPSolution *solution = dynamic_cast<TSPSolution *>(sol);
  // cout << "Cost: " << solution->cost << '\n';

  //DEBUG ONLY
  solution->cached = false;
  problem->eval(solution);
  // cout << solution->path.size() << '\n';

  // cout << "Path:\n";
  for(auto el : solution->getPath()){
    cout << el << ' ';
  }
  cout << endl;
  cout << solution->cost << '\n';

  return 0;
}
#ifndef TABU_SEARCH_H
#define TABU_SEARCH_H
#include <map>
#include <queue>
#include <vector>
#include <functional>
#include <limits>

using namespace std;

class Solution
{
public:
  Solution();
  virtual pair<int, int> tabu() = 0;
};

class Problem
{
public:
  Problem();
  virtual double eval(Solution *) = 0;
};

class TabuSearch
{
private:
  int tabuId = 0;
  long unsigned int maxTabuSize;
  map<pair<int, int>, int> tabuList;
  queue<pair<int, int>> tabuQueue;

  Problem *problem;

  Solution *solution;
  double best;

  function<vector<Solution *>(Solution *)> neighbourhood;

public:
  TabuSearch(Problem *problem, function<vector<Solution *>(Solution *)> neighbourhood, long unsigned int maxTabuSize = 1000);

  bool checkTabu(Solution *solution);

  void addTabu(Solution *solution);

  Solution *search(Solution *initial, long unsigned int maxIter = 1000);
};
#endif
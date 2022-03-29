#include <vector>
#include <algorithm>

extern "C" {
    int *nearest_neighbour(double **edges, int size, int vertex) {
        std::vector<bool> visited(size, false);
        visited[vertex] = true;

        std::vector<int> path;
        path.push_back(vertex);

        while (std::count(visited.begin(), visited.end(), false)) {
            int cost = (1 << 16);
            int nextVertex;
            for (int i = 0; i < size; i++) {
                if (vertex == i || visited[i])
                    continue;
                double curCost = edges[vertex][i];
                if (cost > curCost) {
                    cost = curCost;
                    nextVertex = i;
                }     
            }
            
            path.push_back(nextVertex);
            vertex = nextVertex;
            visited[vertex] = true;
        }
            
        int *pathData = path.data();
        return pathData;
    }
}
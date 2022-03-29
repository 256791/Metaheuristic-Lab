// double evalSwap(double **edges, int n, int m, int s)
// {
// }

int *toswap(int *path, int n, int m, int size)
{
    int *npath = new int[size];
    int j = 0;

    for (int i = 0; i < n; i++)
    {
        npath[j] = path[i];
        j++;
    }

    for (int i = m - 1; i >= n; i--)
    {
        npath[j] = path[i];
        j++;
    }

    for (int i = m; i < size; i++)
    {
        npath[j] = path[i];
        j++;
    }

    return npath;
}

double eval(double **edges, int *path, int size)
{
    double cost = 0;
    for (int i = 0; i < size - 1; i++)
        cost += edges[path[i]][path[(i + 1)]];
    cost += edges[path[size - 1]][path[0]];

    return cost;
}

extern "C"
{
    int *two_opt(double **edges, int *initialPath, int size)
    {
        
        int *path = new int[size];
        for (int i = 0; i < size; i++)
            path[i] = initialPath[i];
        

        double cost = eval(edges, path, size);

        int *npath = nullptr;
        double ncost = cost;

        while (true)
        {
            for (int i = 0; i < size - 1; i++)
            {
                for (int j = i + 1; j < size; j++)
                {
                    int *spath = toswap(path, i, j, size);
                    double scost = eval(edges, spath, size);
                    if (scost < ncost)
                    {
                        ncost = scost;
                        delete[] npath;
                        npath = spath;
                    }
                    else
                    {
                        delete[] spath;
                    }
                }
            }
            if (ncost < cost)
            {
                cost = ncost;
                delete[] path;
                path = npath;
                npath = nullptr;
            }
            else
            {
                delete[] npath;
                break;
            }
        }
        return path;
    }
}
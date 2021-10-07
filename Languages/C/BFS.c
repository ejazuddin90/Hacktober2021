#include <stdio.h>
#define MAX 50


int f = -1, r = -1;
void bfs(int arr[MAX][MAX], int *v, int *q, int n, int s)
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (arr[s][i] && !v[i])
        {
            q[++r] = i;
            v[i] = 1;
            char w=i+64;
            printf("%c ",w );
        }
    }
    if (f <= r)
        bfs(arr, v, q, n, q[++f]);
}
int main()
{
    int n, i, j,arr[MAX][MAX], q[MAX], v[MAX], s;
    printf("Enter the number of vertices  : ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        q[i] = 0;
        v[i] = 0;
    }
    printf(" Adjacency matrix:\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &arr[i][j]);
    printf(" Start Vertex ::\n");
    scanf("%d", &s);
    f=r=0;
    q[r]=s;
    printf("BFS Tree is:\n");
    v[s]=1;
    printf("A ");
    bfs(arr, v, q, n, s);
    if(r!=n-1)
        printf("\n BFS is not possible! for this graph\n");
    return 0;
}
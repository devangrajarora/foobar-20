import java.util.*;

public class PrepareTheBunniesEscape {

    static class Node {
        int i;
        int j;
        int dist;
        int pass;

        Node(int x, int y, int d, int p) {
            i = x;
            j = y;
            dist = d;
            pass = p;
        }
    }

    static Boolean safe(int x, int y, int n, int m) {
        return (x >= 0 && x < n && y >= 0 && y < m);
    }

    public static int solution(int[][] map) {
        int n = map.length;
        int m = map[0].length;

        int dx[] = new int[]{1,0,-1,0};
        int dy[] = new int[]{0,1,0,-1};

        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0,0,1,1));

        int vis[][] = new int[n][m];
        vis[0][0] = 1;

        while(q.size() > 0) {

            Node x = q.remove();
            // System.out.println("dist: "+x.dist);

            if(x.i == n-1 && x.j == m-1) {
                return x.dist;
            }


            for(int i = 0 ; i < 4 ; i++) {

                int nx = x.i + dx[i];
                int ny = x.j + dy[i];
                
                // System.out.println(nx + " " + ny);

                if(safe(nx,ny,n,m) && vis[nx][ny] == 0) {

                    if(map[nx][ny] == 0) {
                        vis[nx][ny] = 1;
                        q.add(new Node(nx,ny,x.dist+1,x.pass));
                    }

                    if(map[nx][ny] == 1 && x.pass == 1) {
                        vis[nx][ny] = 1;
                        q.add(new Node(nx,ny,x.dist+1,0));
                    }
                }
            }

        }

        return -1;

    }

    public static void main(String[] args) {
        // int a[][] = new int[][] {{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}};
    	int a[][] = new int[][] {{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}};

    	int ans = solution(a);
        System.out.println(ans);
    }
}
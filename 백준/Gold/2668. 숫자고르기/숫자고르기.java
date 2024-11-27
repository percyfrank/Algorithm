import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int n;
    static int[] nums;
    static boolean[] visited;
    static int target;
    static List<Integer> ans = new ArrayList<>();
    
    public static void main(String[] args) throws IOException {
       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        nums = new int[n+1];
        visited = new boolean[n+1];
        
        for (int i = 1; i <= n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }
        
        for (int i = 1; i <= n; i++) {
            visited[i] = true;
            target = i;
            dfs(i);
            visited[i] = false;
        }
        
        Collections.sort(ans);
        sb.append(ans.size()).append("\n");
        for (int i = 0; i < ans.size(); i++) {
            sb.append(ans.get(i)).append("\n");
        }
        System.out.println(sb);        
    }
    
    public static void dfs(int start) {
        
        int next = nums[start];
        if(next == target) {
            ans.add(start);
            return;
        }
        
        if(!visited[next]) {
            visited[next] = true;
            dfs(next);
            visited[next] = false;
        }
    }
}
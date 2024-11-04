import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        LinkedList<Integer> list = new LinkedList<>();
        for (int i=1; i<=n; i++) {
            list.add(i);
        }

        StringBuilder ans = new StringBuilder();
        ans.append("<");

        int idx = 0;
        while (!list.isEmpty()) {
            idx = (idx + k - 1) % list.size();
            ans.append(list.remove(idx));
            if (!list.isEmpty()) {
                ans.append(", ");
            }
        }

        ans.append(">");
        System.out.println(ans);
        
    }
}
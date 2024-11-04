import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.util.Collections.max;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            Queue<Integer> q = new LinkedList<>();
            Queue<Integer> idx = new LinkedList<>();

            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                q.add(Integer.parseInt(st.nextToken()));
                idx.add(j);
            }

            int cnt = 1;
            while (!q.isEmpty()) {
                int max =  Collections.max(q);
                int curr = q.poll();
                int curr_idx = idx.poll();

                if(curr == max) {
                    if(curr_idx == m) {
                        System.out.println(cnt);
                        break;
                    } else {
                        cnt++;
                    }
                } else {
                    q.add(curr);
                    idx.add(curr_idx);
                }
            }
        }
    }
}

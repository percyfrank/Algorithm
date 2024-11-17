import java.io.*;
import java.util.*;

public class Main {

    static StringBuilder sb;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            String w = br.readLine();
            int k = Integer.parseInt(br.readLine());

            if (k == 1) {
                sb.append(1).append(" ").append(1).append("\n");
                continue;
            }

            Map<Character, Integer> maps = new HashMap<>();
            for (int j = 0; j < w.length(); j++) {
                maps.put(w.charAt(j), maps.getOrDefault(w.charAt(j), 0) + 1);
            }
            
            int min_len = Integer.MAX_VALUE;
            int max_len = 0;
            for (int j = 0; j < w.length(); j++) {
                if (maps.get(w.charAt(j)) < k) continue;
                int cnt = 1;
                for (int m = j + 1; m < w.length(); m++) {
                    if (w.charAt(j) == w.charAt(m)) {
                        cnt += 1;
                    }
                    if (cnt == k) {
                        min_len = Math.min(min_len, m - j + 1);
                        max_len = Math.max(max_len, m - j + 1);
                        break;
                    }
                }
            }

            if (min_len == Integer.MAX_VALUE || max_len == -1) {
                sb.append(-1).append("\n");
                continue;
            }
            sb.append(min_len).append(" ").append(max_len).append("\n");
        }
        System.out.println(sb.toString());
    }
}
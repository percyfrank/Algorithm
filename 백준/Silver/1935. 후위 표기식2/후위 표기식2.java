import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        Map<Character, Double> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put((char) (65 + i), Double.parseDouble(br.readLine()));
        }

        Deque<Double> q = new ArrayDeque();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isAlphabetic(c)) {
                q.addLast((Double)(map.get(c)));
            } else {
                double b = q.pollLast();
                double a = q.pollLast();
                switch (c) {
                    case '*':
                        q.addLast(a * b);
                        break;
                    case '/':
                        q.addLast(a / b);
                        break;
                    case '+':
                        q.addLast(a + b);
                        break;
                    case '-':
                        q.addLast(a - b);
                        break;
                }
            }
        }
        System.out.printf("%.2f", q.pollFirst());
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        Stack<Character> stack = new Stack<>();
        int cnt = 0;
        stack.add('(');
        for (int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.add(c);
            } else {
                if (s.charAt(i - 1) == '(') {
                    stack.pop();
                    cnt += stack.size();
                } else {
                    cnt += 1;
                    stack.pop();
                }

            }
        }
        System.out.println(cnt);
    }
}
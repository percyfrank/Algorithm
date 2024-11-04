import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        String[] value = new String[n];
        for (int i = 0; i < n; i++) {
            value[i] = br.readLine();
        }

        Stack<Double> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isAlphabetic(c)) {
                stack.add(Double.parseDouble(value[c - 'A']));
            } else {
                double b = stack.pop();
                double a = stack.pop();
                switch (c) {
                    case '*':
                        stack.add(a * b);
                        break;
                    case '/':
                        stack.add(a / b);
                        break;
                    case '+':
                        stack.add(a + b);
                        break;
                    case '-':
                        stack.add(a - b);
                        break;
                }
            }
        }
        System.out.printf("%.2f", stack.pop());
    }
}
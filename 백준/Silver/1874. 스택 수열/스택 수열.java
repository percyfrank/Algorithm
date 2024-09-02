import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        Stack<Integer> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int start = 1;
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            while (start <= num) {
                stack.add(start);
                sb.append("+").append("\n");
                start += 1;
            }
            if(stack.peek() == num) {
                stack.pop();
                sb.append("-").append("\n");
            } else {
                flag = false;
                break;
            }
        }

        if(flag) {
            System.out.println(sb.toString());
        } else {
            System.out.println("NO");
        }
    }
}
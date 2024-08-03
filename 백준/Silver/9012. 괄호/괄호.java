import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {

        Stack<String> stack;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++) {
            String[] s = br.readLine().split("");
            boolean flag = true;
            stack = new Stack<>();
            for (int j=0; j<s.length; j++) {
                if(stack.isEmpty() && s[j].equals(")")) {
                    flag = false;
                    break;
                }
                if(s[j].equals("(")) {
                    stack.push(s[j]);
                } else if (s[j].equals(")")){
                    if (stack.peek().equals("(")) {
                        stack.pop();
                    }
                }
            }

            if (flag && stack.isEmpty()) {
                System.out.println("YES");
            } else if(!flag || !stack.isEmpty()) {
                System.out.println("NO");
            }

        }

    }
}
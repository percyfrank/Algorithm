import java.io.*;
import java.util.*;

public class Main {
    
    static StringBuilder sb;
    
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        sb = new StringBuilder();
        boolean tag = false;
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<word.length(); i++){
            if(word.charAt(i) == '<') {
                if(!stack.empty()) {
                    while(!stack.empty()) {
                        sb.append(stack.pop());
                    }
                }
                sb.append(word.charAt(i));
                tag = true;
                continue;
            }
            if (tag) {
                sb.append(word.charAt(i));
                if(word.charAt(i) == '>') {
                    tag = false;
                }
            } else {
                if(word.charAt(i) == ' ') {
                    while(!stack.empty()) {
                        sb.append(stack.pop());
                    }
                    sb.append(" ");
                } else {
                    stack.push(word.charAt(i));
                }
            }
        }
        if(!stack.empty()) {
            while(!stack.empty()) {
                sb.append(stack.pop());
            }
        }
        System.out.println(sb.toString());
    }
}
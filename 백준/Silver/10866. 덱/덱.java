import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        Deque<Integer> list = new ArrayDeque<>();
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            if (st.countTokens() == 1) {
                String command = st.nextToken();
                if (command.equals("front")) {
                    System.out.println(list.isEmpty() ? -1 : list.peekFirst());
                } else if (command.equals("back")) {
                    System.out.println(list.isEmpty() ? -1 : list.peekLast());
                } else if (command.equals("empty")) {
                    System.out.println(list.isEmpty() ? 1 : 0);
                } else if (command.equals("size")) {
                    System.out.println(list.size());
                } else if (command.equals("pop_front")) {
                    System.out.println(list.isEmpty() ? -1 : list.pollFirst());
                } else if (command.equals("pop_back")) {
                    System.out.println(list.isEmpty() ? -1 : list.pollLast());
                }
            } else {
                String command = st.nextToken();
                int cnt = Integer.parseInt(st.nextToken());
                if(command.equals("push_front")) {
                    list.offerFirst(cnt);
                } else if(command.equals("push_back")) {
                    list.offerLast(cnt);
                }
            }

        }

    }
}
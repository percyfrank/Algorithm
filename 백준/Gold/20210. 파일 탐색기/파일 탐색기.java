import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Value> q = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            q.add(new Value(br.readLine()));
        }

        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()) {
            sb.append(q.poll().value).append("\n");
        }
        System.out.println(sb.toString());
    }
}

class Value implements Comparable<Value> {

    String value;
    ArrayList<String> splittedValue;

    public Value(String value) {
        this.value = value;
        this.splittedValue = splitValue(value);
    }

    public ArrayList<String> splitValue(String value) {

        splittedValue = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < value.length(); i++) {
            char c = value.charAt(i);
            if (Character.isDigit(c)) {
                sb.append(c);
                continue;
            } else {
                if (sb.length() > 0) {
                    splittedValue.add(sb.toString());
                    sb = new StringBuilder();
                }
                splittedValue.add(String.valueOf(c));
            }
        }
        if (sb.length() > 0) {
            splittedValue.add(sb.toString());
        }
        return splittedValue;
    }

    @Override
    public int compareTo(Value other) {

        ArrayList<String> splittedOtherValue = other.splittedValue;
        int limit = Math.min(this.splittedValue.size(), splittedOtherValue.size());
        for (int i = 0; i < limit; i++) {
            String value = this.splittedValue.get(i);
            String otherValue = splittedOtherValue.get(i);
            boolean valueCheck = checkValue(value.charAt(0));
            boolean otherValueCheck = checkValue(otherValue.charAt(0));

            // 숫자&숫자
            if(valueCheck && otherValueCheck) {
                BigDecimal valueDecimal = toDecimal(value);
                BigDecimal otherValueDecimal = toDecimal(otherValue);
                if(valueDecimal.equals(otherValueDecimal)) {
                    if(value.length() == otherValue.length()) {
                        continue;
                    }
                    return value.length() - otherValue.length();
                }
                return valueDecimal.compareTo(otherValueDecimal);
            }

            // 숫자&문자
            else if((valueCheck && !otherValueCheck) || (!valueCheck && otherValueCheck)) {
                return valueCheck ? -1 : 1;
            }

            // 문자&문자
            else {
                if(value.equals(otherValue)) {
                    continue;
                }
                if(value.equalsIgnoreCase(otherValue)) {
                    if(Character.isUpperCase(value.charAt(0))) {
                        return -1;
                    }
                    return 1;
                }
                return value.compareToIgnoreCase(otherValue);
            }
        }
        return this.value.length() - other.value.length();
    }

    public boolean checkValue(char value) {
        return Character.isDigit(value);
    }

    public BigDecimal toDecimal(String value) {
        return new BigDecimal(value);
    }
}
import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Value> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(new Value(br.readLine()));
        }

        Collections.sort(list);
        StringBuilder sb = new StringBuilder();
        for (Value v : list) {
            sb.append(v.value).append("\n");
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

        this.splittedValue = new ArrayList<>();
        int idx = 0;
        for (int i = 0; i < value.length(); i++) {
            char c = value.charAt(i);
            if (Character.isDigit(c)) {
                continue;
            } else {
                if (idx < i) {
                    splittedValue.add(value.substring(idx,i));
                }
                splittedValue.add(String.valueOf(c));
                idx = i+1;
            }
        }
        
        if (idx < value.length()) {
            splittedValue.add(value.substring(idx));    
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
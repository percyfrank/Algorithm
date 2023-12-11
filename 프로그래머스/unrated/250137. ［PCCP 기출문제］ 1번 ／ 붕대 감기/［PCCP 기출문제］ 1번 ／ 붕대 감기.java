import java.util.*;

class Solution {

    public int solution(int[] bandage, int health, int[][] attacks) {

        int curr = health;
        int attackIdx = 0;
        int healTime = 0;

        for (int i = 1; i <= attacks[attacks.length - 1][0]; i++) {
            // 공격받지 않은 경우
            if (i != attacks[attackIdx][0]) {
                curr += bandage[1];
                healTime += 1;
                if (healTime == bandage[0]) {
                    curr += bandage[2];
                    healTime = 0;
                }
                if (curr > health) {
                    curr = health;
                }
            } else { // 공격받은 경우
                curr -= attacks[attackIdx][1];
                healTime = 0;
                attackIdx += 1;
                if (curr <= 0) {
                    curr = -1;
                    break;
                }
            }
        }

        return curr;

    }
}

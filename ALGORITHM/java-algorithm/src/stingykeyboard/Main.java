package stingykeyboard;

import java.util.HashMap;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
      int[] answer = new int[targets.length];
      HashMap<Character, Integer> keypad = new HashMap<>();
      int minCount = 100;
      for (int i = 0; i < keymap.length; i++) {
        String keys = keymap[i];
        int count = 0;
        for (int j = 0; j< keys.length(); j++){
          char target = targets[0].charAt(0);
          char key = keys.charAt(j);
          if (key != target){
            count += 1;
          } else {
            if (count <= minCount) {

            minCount = count;
            }
          }


        }

      }
      return answer;
    }
}
public class Main{
  public static void main(String[] args) {

  }
}


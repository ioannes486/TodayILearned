package stingykeyboard.answer;

import java.util.HashMap;

class Solution {

  public int[] solution(String[] keymap, String[] targets) {
    int[] answer = new int[targets.length];
    HashMap<Character, Integer> keypad = new HashMap<>();

    // keymap의 전체 키를 돌면서
    for (int i = 0; i < keymap.length; i++) {
      // keymap의 하나의 클래스를 돌면서
      for (int j = 0; j < keymap[i].length(); i++) {
        // 키의 알파벳 중 하나를 꺼내기
        char cur = keymap[i].charAt(j);

        // 꺼낸 알파벳이 해쉬맵 키값에 있으면
        if (keypad.containsKey(cur)) {
          // 그 키를 누르는 횟수와 기존에 있던 수를 비교해서 할당하기
          int idx = keypad.get(cur);
          keypad.put(cur, Math.min(idx, j + 1));
        } else {
          keypad.put(cur, j + 1);
        }
      }
    }

    for (int i = 0; i < targets.length; i++) {

      String target = targets[i];
      int count = 0;
       
      boolean flag = true;

      for (char cur : target.toCharArray()) {
        if (keypad.containsKey(cur)) {
          count += keypad.get(cur);
        } else {
          flag = false;
          break;
        }
        answer[i] = flag == false ? -1 : count;
      }
      return answer;
    }
  }
}

public class MessyKeyboardAnswer {

  public static void main(String[] args) {

  }
}

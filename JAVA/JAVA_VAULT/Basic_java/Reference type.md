# 1. 배열
---
동일한 자료형의 연속적인 집합체
자료형이 동일하기 때문에 동일한 코드패턴을 적용하기 쉽다.
# Array 클래스

---

### 배열이란?

자료형이 같은 변수들의 집합

### 배열을 사용하는 이유

배열을 사용해서 동일한 자료형에 동일한 연산을 수행하기 쉽다.

```java
package com.in28minutes.reftype;

public class ArrayAndArrayList {
    public static void main(String[] args) {
    
    // 배열 선언
    int[] numbers = new int[] {33,14,15,34,6,3,4,53,14,3,435};  
    
		// 합 초기화
    int sum = 0;
		
		// 반복문으로 배열의 값들 더하기
    for (int number:numbers){  // 다음 과 같이 [[for each]]문을 사용해서 읽을 수도 있다.
        sum += number;
    }
        System.out.println("the sum of numbers is " + sum);
    }
}
```

### 배열을 선언하고 초기화하는 방법

```java
    int[] numbers0 = new int[9] // 다음과 같이 크기를 지정해서 선언하는 것이 기본!
    int[] numbers1 = new int[] {33,14,15,34,6,3,4,53,14,3,435};  
    int[] numbers2 = {34,34,21,43,14,34,34};  // 이런 형식으로 생성자 없이 생성할 수도 있다.
    int[] numbers3 = {} // 배열은 비어있을 수도 있다.
```

### 배열을 이용해서 문자열 한글자씩 출력하기
```java
package com.in28minutes.reftype;

public class StringIndexing {
    public static void main(String[] args) {

        /*TO DO
        일정 길이의 문자열을 한번에 char하나씩 출력하기
        오늘 배운 배열을 이용해보셈
        char 배열의 크기를 문자열의 길이로 설정하기
        * */
        String str = "Hello My Name Is Andy. Take Care Guys~!";
        int sentenceLength = str.length();
        char[] chars = new char[sentenceLength];

        for (int i = 0; i < sentenceLength; i++){
            chars[i] = str.charAt(i);
        }

        for (int i = 0; i < chars.length; i++){  // 중요포인트! 배열의 length는 속성이지 메서드가 아니다.
             System.out.println(chars[i]);
        }
    }
}
```
### 배열의 특징
서로다른 두 객체가 같은 배열을 참조하고 있을 때 원본 배열이 바뀌면 두 객체가 모두 바뀐다.

# 2. String 클래스
---
### String 클래스
### String클래스의 특징 
1. 한번 정의된 문자열은 변경할 수 없다. 문자열의 내용을 변경하면 자바가상머신은 기존의 문자열을 수정하는 것이 아니라 새로운 문자열을 포함하고 있는 객체를 생성해 사용하고 기존의 객체는 버린다
2. 문자열 리터럴을 바로 입력해 객체를 생성할 때 같은 문자열끼리 객체를 공유한다.
```

String str1 = new String("안녕");  // 이렇게 생성하면 새로운 객체를 공유한다.
System.out.println(str1); // 변수명을 인자로 넣어도 heap에 있는 값을 호출해준다.
System.out.println(str1.toString());
System.out.println(str1.hashCode()); // 변수명을
```

package com.in28minutes.textcases;

public class TestCase {
    public static void main(String[] args) {
        int i = 23;
        if (i == 25){ // 조건 자리에는 정수형을 사용할 수 없다.
            System.out.println("i = 25");
        } else if (i == 24) {  // 1. 헷갈리지 않기 위해 항상 블록을 사용할것,
            // 2. 블록을 사용하지 않으면 한줄만 if문 안에 종속된다.
            System.out.println("i = 24");
        } else {
            System.out.println("i is non of both");
        }
    }
}

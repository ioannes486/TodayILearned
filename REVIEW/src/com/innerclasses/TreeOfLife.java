package com.innerclasses;

public class TreeOfLife {
    int a = 1000000000;

    void yel (){

    }
    void yell(){
        final int a = 3;
        final int b =6;
        class Animal {
            void bark(){
                System.out.println(TreeOfLife.this.a);  // outer클래스의 필드 호출
                System.out.println(b);
                TreeOfLife.this.yel();
                yel();
                b =7;  // 지역 이너클래스에서는 메소드에 정의된 지역변수를 변경 불가한다.
                a = 8;
            }
        }
    }
}

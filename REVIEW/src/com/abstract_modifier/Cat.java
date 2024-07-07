package com.abstract_modifier;

public class Cat implements Animal {

    int numberOfLegs = 4;
//    Animal.numberOfFinger 상위 인터페이스의 필드는 하위 클래스에서 사용할 수 없다.
    public class Flea {
        int numberOfLegs = 6;

        void attach() {
            System.out.println(Cat.this.numberOfLegs+"개의 다리에 착! 달라붙기");  // outer클래스의 필드 사용하기
        }

        static void hop(){
            System.out.println("폴짝!");
        }
    }

    @Override
    public void cry(){
        // 디폴트 메서드를 오버라이딩 해서 안에 아무것도 안적어주면 아무일도 발생하지 않는다.
        Animal.super.cry();  // 상위 인터페이스의 디폴트메소드 사용하기

        // 디폴트 메서드 구현 시 부모클래스를 적어주는 이유는 인터페이스가 다중 구현을 할 수 있기 때문이다.
    }
}

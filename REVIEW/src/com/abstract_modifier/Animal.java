package com.abstract_modifier;
/*
* abstract메서드는 abstract클래스에 담아라
* 추상 클래스는 객체를 직접 생성할 수 없다.
* */
interface Animal {
    public static final int numberOfFinger = 5;
    public static final int numberOfLegs = 4;

    public default void cry(){
        System.out.println("고양이는 멍멍, 강아지는 삐약삐약");
    }

    // 인터페이스의 신기능 1 : default메서드
    public default String son(){
        return "쳇 간식을 얻으려면 어쩔 수 없다.";  // 인터페이스의 디폴트 메서드는 상속을 안하고도 사용이 가능하다.
    }


    // 인터페이스의 신기능 1 : static메서드
    public static int getNumberOfFinger(){
        return numberOfFinger;
    }

}


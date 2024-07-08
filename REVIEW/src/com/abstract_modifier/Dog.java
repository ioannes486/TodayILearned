package com.abstract_modifier;

public class Dog implements Animal {
    static int numberOfFingers = 4;
    static class Flea{
        int numberOfFingers = 6;
        void attach(){
            System.out.println(Dog.numberOfFingers + "개의 다리에 착! 달라붙기");
        }
    }

    @Override
    public void cry() {
        System.out.println("워워워워워워워워워워어오오오오");
    }

    @Override
    public String son(){
//        return "근데 간식은 왜 이렇게 맛있냐";
        return Animal.super.son();  // 하위 클래스에서 메서드를 선언할 때는 이렇게 선언한다.
    }

public class Dog extends Animal {
    public void cry(){

    }
}


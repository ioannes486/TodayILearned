package com.in28minutes.oops;

public class MotorBike {
    //state
    private int speed;  // member variable
    // ^접근 제어자 private을 줌으로써 외부 클래스에서 이 인스턴스 변수를 함부로 바꾸지 못하게 한다.


    //behaviour
    int getSpeed(){
        return this.speed;
    }

    void setSpeed(int speed) {
        this.speed = speed;
    }

    void start(){
        System.out.println("Bike Started");
    }
}

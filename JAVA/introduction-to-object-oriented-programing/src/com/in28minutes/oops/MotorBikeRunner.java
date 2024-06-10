package com.in28minutes.oops;

public class MotorBikeRunner {
    public static void main(String[] args) {
        MotorBike ducati = new MotorBike();
        MotorBike honda = new MotorBike();

        ducati.start();
        honda.start();

//        ducati.speed = 10;
//        honda.speed = 1000;
        // 위 방법대로 방법대로 하면 MotorBikerunner에서 직접 ducati안의 멤버 변수를 할당 할 수 있는 상태가 된다.
        // 이는 자바의 모듈화에 위배된다.
        // 따라서 멤버변수를 private으로 접근 지정자를 설정 후 MotorBike클래스의 메서드를 이용해서 변수를 통제할 수 있게 만든다.
        // 변수 직접할당 -> 메서드를 통한 할당
        ducati.setSpeed(100);
        honda.setSpeed(80);

        System.out.println(ducati.getSpeed());
    }
}

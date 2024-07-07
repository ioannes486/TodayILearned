package com.abstract_modifier;

public class ZooKeeper {
    public static void main(String[] args) {
        // 생성자 생성
        Animal cat = new Cat();
        Animal dog = new Dog();

        // public static final 필드
        System.out.println("-Animal 인터페이스의 public static final필드값 : "+Animal.numberOfFinger);
//        Animal.numberOfFinger = 4;  public abstract final필드이기 때문에 필드값을 바꾸지 못한다.
        System.out.println();

        // void 메서드
        System.out.println("-void 메서드-");
        cat.cry();
        dog.cry();
        System.out.println();

        // 리턴값이 있는 메서드
        System.out.println("-리턴값이 있는 메서드-");
        System.out.println(cat.son());
        System.out.println(dog.son());
        System.out.println(Animal.getNumberOfFinger());

        // Cat, Dog의 이너 클래스 : 동물 몸에 있는 벼룩
        Cat cat2 = new Cat();  // 인터페이스의 타입으로 생성하면 생성이 안된다. Flea는 Cat의 이너클래스이므로
        Cat.Flea flea = cat2.new Flea();

        // Cat > Flea 인스턴스에 접근하기
        System.out.println("벼룩의 다리 수는 : " + flea.numberOfLegs);
        System.out.println("고양이의 다리 수는 : " + cat2.numberOfLegs);

        //Cat > Flea 의 인스턴스 메서드
        Cat.Flea.hop();  // 이너클래스의 static메서드
        flea.attach();

        // static 이너클래스
        Dog.Flea dogFlea = new Dog.Flea();
        dogFlea.attach();




    }
}

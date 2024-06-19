package com.abstract_modifier;

public class ZooKeeper {
    public static void main(String[] args) {
        Animal cat = new Cat();
        Animal dog = new Dog();
        cat.cry();
        dog.cry();
    }
}

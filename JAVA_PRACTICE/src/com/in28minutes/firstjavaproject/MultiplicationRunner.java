package com.in28minutes.firstjavaproject;

public class MultiplicationRunner {

    public static void main(String[] args) {
        MultiplicationTable table = new MultiplicationTable();
        table.print();
        table.print(1);
        table.print(1,20, 30);
    }
}

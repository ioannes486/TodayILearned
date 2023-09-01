package com.in28minutes.firstjavaproject;

public class MultiplicationTable {
    void print() {
        print(5,1,10);
    }
    void print(int table){
        print(table, 1, 10);
        }
    void print(int table, int from, int to) {
        for (from = 1; from <= to; from++) {
            System.out.printf("%d * %d = %d", table, from , table * from).println();
        }
    }
}

package com.in28minutes.oops;

public class Book {
    //state
    private int noOfCopies;
    public void setNoOfCopies(int noOfCopies) {
        this.noOfCopies = noOfCopies;
    }
    //behaviour
    void flip() {
        System.out.println("im flipped");
    }
}

package com.in28minutes.character;

public class CharRunner {
    public static void main(String[] args) {
        MyChar myChar = new MyChar('a');
        System.out.println(myChar.isVowel());
        System.out.println(myChar.isDigit());
        MyChar.printLowercaseAlphabet();
        MyChar.printUppercaseAlphabet();
    }
}

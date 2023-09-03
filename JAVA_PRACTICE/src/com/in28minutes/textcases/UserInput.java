package com.in28minutes.textcases;

import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner scanner  = new Scanner(System.in);
        System.out.println("Enter Number1 : ");
        int number1 = scanner.nextInt();
        System.out.println("Enter Number2 : ");
        int number2 = scanner.nextInt();
        System.out.println("Number1 is - "+ number1);  // 문자열에 int를 덧붙이면 문자열로 읽힌다.
        System.out.println("Number2 is - "+ number2);  // 문자열에 int를 덧붙이면 문자열로 읽힌다.

        System.out.println("Choices Available are");  // 문자열에 int를 덧붙이면 문자열로 읽힌다.
        System.out.println("1 - add");  // 문자열에 int를 덧붙이면 문자열로 읽힌다.
        System.out.println("2 - Substract");  // 문자열에 int를 덧붙이면 문자열로 읽힌다.
        System.out.println("3 - Divide");  // 문자열에 int를 덧붙이면 문자열로 읽힌다.
        System.out.println("4 - Multiply");  // 문자열에 int를 덧붙이면 문자열로 읽힌다.

        System.out.println("Enter choice");  // 문자열에 int를 덧붙이면 문자열로 읽힌다.
        int choice = scanner.nextInt();
        System.out.println("choice your chices are :" + choice);

        performOperationUsingSwitch(choice, number1, number2);

    }

    private static void perfromOperationUsingNestedIfElse(int choice, int number1, int number2) {
        int result = 0;
        if (choice ==1){
            result = number1 + number2;
        } else if (choice ==2) {
            result = number1 - number2;
        } else if (choice ==3) {
            result = number1 / number2;
        } else if (choice ==4) {
            result = number1 * number2;
        } else
            System.out.println("You've written wrong number");
        System.out.println("Result : " + result);
    }
    private static void performOperationUsingSwitch(int choice, int number1, int number2) {
        switch (choice) {  // int, char,short, short, byte, enum,string만 허용
            case 1 -> System.out.println("Result : " + (number1 + number2));  // case안에는 조건으 줄 수 없다.
            case 2 -> System.out.println("Result : " + (number1 - number2));
            case 3 -> System.out.println("Result : " + (number1 / number2));
            case 4 -> System.out.println("Result : " + (number1 * number2));
            default -> System.out.println("invalid Operations detected");
            //default문은 어디든 놓을 수 있다. 해당 변수가 default조건을 만족할 경우 default에 break이 없으면 아래 구문으로 fall through된다.

        }


    }

}

package com.in28minutes.switchexercise;

import java.util.Scanner;

public class WeekDays {
    public static Scanner scanner = new Scanner(System.in);

    public static String determineNameOfDay(int dayNumber){
        System.out.println("input day code : ");
        int input = scanner.nextInt();

        switch (input){
            case 0 :
                return "Sunday";
            case 1 :
                return "Monday";
            case 2 :
                return "Tuesday";
            case 3 :
                return "Wednesday";
            case 4 :
                return "Thursday";
            case 5 :
                return "Friday";
            case 6 :
                return "Saturday";
            default:
                return "Invalid Input";
        }
    }
    public static boolean isWeekDay(int dayNumber){
        System.out.println("input day code : ");
        int input = scanner.nextInt();

        switch (input){
            case 0 :
                return false;
            case 1 :
                return true;
            case 2 :
                return true;
            case 3 :
                return true;
            case 4 :
                return true;
            case 5 :
                return true;
            case 6 :
                return false;
            default:
                return false;



        }

    }
}

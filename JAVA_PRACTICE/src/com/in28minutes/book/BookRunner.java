package com.in28minutes.book;

public class BookRunner {
    public static void main(String[] args) {
        Book cleanCode = new Book(100);
        Book insideSoTong = new Book(200);



        cleanCode.setPages(110);
        insideSoTong.setPages(730);

        int c = cleanCode.getPages();
        c+=100;
        cleanCode.setPages(c);
        cleanCode.increasePage(100);
        insideSoTong.increasePage(100);
        System.out.println(cleanCode.getPages());
//        System.out.printf("clea code has %d pages",cleanCode.pages).println();
//        System.out.println(insideSoTong.pages);

    }
}

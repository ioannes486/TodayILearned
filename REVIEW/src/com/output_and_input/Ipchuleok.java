package com.output_and_input;

import java.io.File;

public class Ipchuleok {
    public static void main(String[] args) {
       File newFile = new File("./ipchuleok.txt");
       File newFile2 = new File("C:\\dev\\workspace\\javadev\\src\\oop24\\io");  // 경로작성은 파이선이랑 똑같이 하면 될듯
//        System.out.println(System.getProperty("user.dir"));
//        System.out.println(System.getProperty("java.version"));
//        System.out.println(System.getProperty("java.vendor"));
//        System.out.println(System.getProperty("file.separator"));
        System.out.println(newFile.getAbsoluteFile());
        System.out.println(newFile2.isDirectory());
        System.out.println(newFile2.isFile());
        System.out.println(newFile2.getName());
        System.out.println(newFile2.getParent());  // ./와 같이 현재 폴더부터 추적하는 경로를 적으면 부모폴더의 이름이 .으로 나온다.
        File newDir = new File("C:");
        String[] list = newDir.list();

        System.out.println(list.length);

    }
}

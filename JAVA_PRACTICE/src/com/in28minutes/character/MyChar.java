package com.in28minutes.character;

public class MyChar {
    private char character;

    public MyChar(char character){this.character = character;}

public static void printUppercaseAlphabet(){
        for (char i='A'; i<='Z' ; i++)
            System.out.println((char)i);
}

public static void printLowercaseAlphabet(){
        for (char i='a'; i<='z' ; i++)
            System.out.println((char)i);
    }

    public boolean isVowel(){
        if (character =='a' || character =='e' || character =='i' || character =='o' || character =='u'||
                character =='A' ||character =='E' ||character =='I' ||character =='O' ||character =='U')
            return true;
        return false;
    }

public boolean isDigit() {
    if ((int) character >= 48 && (int) character<=57)
        return true;
    return false;
}

public boolean isConsonant() {
    return isAlpha() && !isVowel();

}

public boolean isAlpha(){
        if ((int) character >= 97 &&(int) character >= 122)
            return true;
        if ((int) character >= 65 &&(int) character >= 90)
            return true;
        return false;


}


}

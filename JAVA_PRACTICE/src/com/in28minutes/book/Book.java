package com.in28minutes.book;

public class Book {
    //state
    private int pages;
    public Book(){  // 멤버변수에 기본값 주기 : 파이선이랑은 다르게 함수를 한번 더 코딩해줘야함 파이선은 func(arg=0):형태로 =다음에 기본값주기가 가능한데 자바는 안됨
        this(5);
//        this.pages = 5;
    }
    public Book(int pages){  // 클래스 생성자 : 클래스를 생성할 때 데이터(멤버변수)에 인스턴스마다 서로 다른 값을 주고 싶을 때 사용
        this.pages = pages;
    }

    //behaviour
    public int getPages() {
        return this.pages;  //인스턴스의 페이지 호출
    }
    public void setPages(int pages) {
        if (pages > 0)  // setter 캡슐화를 함으로써 데이터 유효성검사를 할 수 있따.
            this.pages = pages;

    }
    public void increasePage(int howMuch){
        setPages(this.pages + howMuch);
    }

}

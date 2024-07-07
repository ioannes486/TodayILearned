package com.generic;

public class GenericMethods {
    public <T> T method(T t) {
        return t;
    }

    public <T>  boolean method2(T t1, T t2) {
        return t1.equals(t2);
    }
}

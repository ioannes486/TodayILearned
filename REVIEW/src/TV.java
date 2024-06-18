public interface TV extends Machine, Thing{
    public static int numberOfChannel = 3;
    public abstract void turnOn();  // pulbic abstract자동으로 붙는다.

    //default 메서드 : 인터페이스에 메소드를 추가할 때 인터페이스에 한번만 메소드를 정의하면 되므로 쉽게 만들어 준다.
    public default void hitTV(){
        System.out.println("기계는 때려야 말을 듣지");
    } //
}

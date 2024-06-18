
public class TVOperator {
    public static void main(String[] args) {
        // 인터페이스의 필드는 바꿀 수 없다.
        System.out.println(TV.numberOfChannel);
//        TV.numberOfChannel = 4;

        // 인터페이스 객체 생성법
        TV tv = new SamsungTV();
        TV tv2 = new TV(){
            public void turnOn() {
            }
        };

        // 디폴트 메서드 호출
        tv.hitTV(); // 별도로 클래스에서 오버라이딩 후 재정의를 안해줘도 돌아간다.
    }
}

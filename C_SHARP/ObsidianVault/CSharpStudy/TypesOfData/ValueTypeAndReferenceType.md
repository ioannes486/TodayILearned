자료의 타입에는 값 타입과 참조타입이 존재한다. 
# 1. 값타입(Value Type)
* `int`, `float`, `long`, `double`, `char`, `bool`, `decimal`, `struct`, `enum`등의 type이 해당한다
* 값을 메모리에 직접 저장한다.
* Null값이 가능하다 (Nullable 버전의 경우 int?, double?과 같이 나타낸다.)
* 주로 stack메모리에 저장된다.
* 값 타입이 레퍼런스타입의 일부일 경우 heap메모리에 저장이 가능하다.

# 2. 참조타입(Reference Type)
* 값을 직접 저장하는 것이 아니라 `값의 위치를 저장한다`.
* 값을 복사할 경우 값 자체를 복사하는 것이 아닌 `16진수 주소를 저장`한다.
* [[HexadecimalAddress]]의 예 : 0x23671245
* `string`, `class`, `Array` 등이 해당한다.
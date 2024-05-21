
// See https://aka.ms/new-console-template for more information
// 출력함수
Console.WriteLine("Enter something!");

//사용자 인풋 받기
string userInput = Console.ReadLine();
Console.WriteLine("You've entered " + userInput);
Console.ReadKey();  // 아무키나 누를 때까지 콘솔을 대기하게 하는 역할

// 여러 값타입들
byte age = 255; // 0~ 255 2^8개의 숫자를 표현할 수 있다. 1byte = 8bit
sbyte age2 = 255; // 이렇게 실행하면 오류가 난다.
sbyte age3 = -128;

/*byte는 signed byte와 그냥 byte로 나누어진다. 기본값이 byte이고 byte는 양수만을 나타낸다
 다른 데이터 타입은 그냥 data type과 unsigned data type으로 나누어진다. unsigned data type은
양수만을 나타낼 수 있다. signed 
byte : unsigned가 기본
others : signed가 기본*/

int myage = -128; // 32비트의 숫자
uint myage2 = -128; // u int는 음수를 표기하지 못하므로 오류가 난다.
uint myage3 = 4000000000; // 일반 int 보다 높은 양수를 표현가능하다.

short freindsNumber = 32767; // 16비트의 숫자
ushort freindsNumber2 = 65535; //링크드인 친구수랑 같다

long phonenumber = 01034938220;
ulong phonenumber2 = 19191993939;

float pi = 3.141592f; // 사용하는 메모리가 적다.
double dbl = 3.3434f;

// 여러 참조타입들
string myName = "Denis";

// 변수 정의
string petsName;

// 변수 초기화
petsName = "Daisy";
Console.WriteLine($"my pet is {petsName}");  // 파이선의 f스트링이랑 똑같다.

// 변수 재할당
petsName = "Barky";
Console.WriteLine($"my pet is {petsName}");


// 키입력 대기함수
Console.ReadKey();
// '디버그 완료 시 콘솔 종료 설정을 적용 후 '코드를 빼고 실행시킬 경우
// Console.WriteLine을 실행시킨다음 바로 종료된다.

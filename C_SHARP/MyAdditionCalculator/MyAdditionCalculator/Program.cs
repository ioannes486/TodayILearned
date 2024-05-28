/*모든 값타임에 parse메소드가 존재하지만 enum, struct에는 존재 x*/
double myNumber1 = 0.0;
double myNumber2 = 0.0;

Console.WriteLine("Enter a number you want to add");
string userInput = Console.ReadLine();
myNumber1 = double.Parse(userInput); // read only struct

Console.WriteLine("Enter a number you want to add");
userInput = Console.ReadLine();
myNumber2 = double.Parse(userInput); // read only struct

double result = myNumber1 + myNumber2;
result = Math.Round(result, 2);
Console.WriteLine($"the result is {myNumber1 + myNumber2}");

Console.ReadKey();
//implicit conversion
/* 암시적 형변환 : 크기가 작은 타입에서 크기가 큰 타입으로 형변환을 할 경우 
 정상적으로 형변환이 된다 
 */
double mydouble1;
int myint1 = 12;
mydouble1 = myint1;

double mydouble2;
float myfloat1 = 13.5f;
mydouble2 = myfloat1;

// explicit conversion
/*하지만 크기가 큰 타입에서 크기가 작은 타입으로 형변환을 하는 것은 기본적으로 불가능하다.
 하지만 괄호를 씌우면 가능하다. 이떄의 형변환을 명시적 형변환이라고 한다. 
명시적 형변환을 할 때 큰 타입에 저장된 값이 작은 타입에 저장 할 수 없을 정도로 크다면 
일부를 버리고 변환이 된다.*/
int myInt2;
double mydouble3 = 13.5;
myInt2 = (int)mydouble3;

float myfloat2;
double mydouble4 = 13.232323232323232323;
myfloat2 = (int)mydouble4;


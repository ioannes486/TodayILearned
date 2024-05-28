//implicit conversion
/* 암시적 형변환 : 크기가 작은 타입에서 크기가 큰 타입으로 형변환을 할 경우 
 정상적으로 형변환이 된다 
 */
Console.WriteLine("암시적 형변환");
double mydouble1;
int myint1 = 12;
mydouble1 = myint1;
Console.WriteLine($"원래 값 int : {myint1} \n변환 값 double {mydouble1}");

double mydouble2;
float myfloat1 = 13.5f;
mydouble2 = myfloat1;
Console.WriteLine($"원래 값 float : {myfloat1} \n변환 값 double {mydouble2}");
Console.WriteLine();
// explicit conversion
/*하지만 크기가 큰 타입에서 크기가 작은 타입으로 형변환을 하는 것은 기본적으로 불가능하다.
 하지만 괄호를 씌우면 가능하다. 이떄의 형변환을 명시적 형변환이라고 한다. 
명시적 형변환을 할 때 큰 타입에 저장된 값이 작은 타입에 저장 할 수 없을 정도로 크다면 
일부를 버리고 변환이 된다.*/
Console.WriteLine("명시적 형변환");

int myInt2;
double mydouble3 = 13.1122217232323;
myInt2 = (int)mydouble3;
Console.WriteLine($"원래 값 double : {mydouble3} \n변환 값 int {myInt2}");

float myfloat2;
double mydouble4 = -13.1259723094853443443;
myfloat2 = (float)mydouble4;
Console.WriteLine($"원래 값 double : {mydouble4} \n변환 값 float {myfloat2}");


//Conversion Helpers Parse and Convert
string numberString = "123";
int result  = int.Parse( numberString );

string myBoolString = "true";
bool myBool = Convert.ToBoolean(myBoolString);



//암시적 형변수(var)
var myNumber = "13";
var myNumber2 = 135;
var sumOfMyNumbers = myNumber + myNumber2;



Console.WriteLine("the result is " + sumOfMyNumbers);
Console.WriteLine("the type of myNumber is " + myNumber.GetType());
Console.WriteLine("the type of myNumber2 is " + myNumber2.GetType());
Console.WriteLine("the type of sumOfMyNumbers is " + sumOfMyNumbers.GetType());

Console.ReadKey();
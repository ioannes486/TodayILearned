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
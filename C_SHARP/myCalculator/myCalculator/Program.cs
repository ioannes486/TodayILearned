// accepting user input
//Console.WriteLine("plz input whole number");
//int userInput1 = int.Parse(Console.ReadLine());
//Console.WriteLine("plz input next whole number");
//int userInput2  = int.Parse(Console.ReadLine());
Random random = new Random();
int randomNumber = random.Next(101);
bool isGuessedCorrectly = false;

Console.WriteLine("input a number");
for (int i = 19; i > -2; i--)
{
        int userInput = int.Parse(Console.ReadLine());

        if (userInput > randomNumber)
            Console.WriteLine($"{userInput} is larger than the result. chances left : {i}");
        else if (userInput == randomNumber)
        {
            Console.WriteLine("Those are same");
            isGuessedCorrectly = true;
            break;
        }
        else
            Console.WriteLine($"{userInput}  is smaller than the result. chances left : {i}");
}

if (isGuessedCorrectly == false)
{
    Console.WriteLine("U R dumb");
}


Console.ReadKey();

// See https://aka.ms/new-console-template for more information

//출력함수
Console.WriteLine("Enter something!");

//사용자 인풋 받기

string userInput = Console.ReadLine();
Console.WriteLine("You've entered " + userInput);
Console.ReadKey();  // 아무키나 누를 때까지 콘솔을 대기하게 하는 역할

// '디버그 완료 시 콘솔 종료 설정을 적용 후 '코드를 빼고 실행시킬 경우
// Console.WriteLine을 실행시킨다음 바로 종료된다.
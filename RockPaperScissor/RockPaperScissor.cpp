#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

enum Choice
{
    ROCK,
    PAPER,
    SCISSORS
};

Choice getComputerChoice()
{
    return static_cast<Choice>(rand() % 3); // Type casting
}

Choice getUserChoice()
{
    int userChoice;
    cout << "Enter your choice (0 :rock, 1: paper, or 2: scissors)" << endl;
    cin >> userChoice;
    if (userChoice < 0 || userChoice > 2)
    {
        cout << "Invalid choice! Default choice is rock." << endl;
        return ROCK;
    }
    return static_cast<Choice>(userChoice);
}

string determineWinner(Choice userChoice, Choice computerChoice)
{
    if (userChoice == computerChoice)
        return "It is a tie🫤";
    else if ((userChoice == ROCK && computerChoice == SCISSORS) || (userChoice == PAPER && computerChoice == ROCK) || (userChoice == SCISSORS && computerChoice == PAPER))
    {
        return "You are a winner🏆";
    }
    else if ((userChoice == ROCK && computerChoice == PAPER) || (userChoice == PAPER && computerChoice == SCISSORS) || (userChoice == SCISSORS && computerChoice == ROCK))
    {
        return "You are a loser😭";
    }
    else
        return "Invalid input.";
}

int main()
{
    srand(time(0));
    Choice userChoice = getUserChoice();
    Choice computerChoice = getComputerChoice();
    string result = determineWinner(userChoice, computerChoice);
    cout << result << endl;
}
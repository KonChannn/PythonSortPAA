#include <iostream>
#include <fstream>
#include <cstdlib> // Include the necessary header file for rand()
using namespace std;

int main() {
    int value;
    ofstream outputFile("case5.txt");

    if (outputFile.is_open()) {
        int i = 0;
        int number = 5000;

        // Seed the random number generator
        srand(time(NULL));

        outputFile << number << "\n";

        while (i < number) {
            value = rand() % number;
            outputFile << value << "\n";
            i++;
        }
        outputFile.close();
    }
    return 0;
}

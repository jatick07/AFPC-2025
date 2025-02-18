#include <iostream>
#include <string>
#include <map>

std::map<char, int> LettersCount(const std::string& str) {
    std::map<char, int> letterCount;
    for (char ch : str) {
        ++letterCount[ch]; }
    return letterCount; }

int main() {
    std::string input;
    
    std::getline(std::cin, input);

    std::map<char, int> output = LettersCount(input);

    for (const auto& pair : output) {
        std::cout << pair.first << ": " << pair.second << std::endl; } }

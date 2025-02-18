#include <iostream>

void PrintEven(int start, int end) {
    for (int i = start; i < end + 1; ++i) {
        if (i % 2 == 0) {
            std::cout << i << ' '; } } }

int main() {
    int start, end;
    std::cin >> start >> end;
    PrintEven(start, end); }

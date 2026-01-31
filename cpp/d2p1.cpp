#include <iostream>
#include <string>
#include <fstream>

int sum_false_range(int start, int end);

int main() {
    std::string filename = "./Inputs/day2_input.txt";

    // Open and read file
    std::ifstream file(filename);
    if (!file) {
        std::cout << "Could not open file '" << filename << "'\n";
        return 1;
    }
    
    file.close();

    int t1 = 11, t2 = 22;
    int x = sum_false_range(11, 22);
    std::cout << "Sum of invalid IDs from " << t1 << " to " << t2 << " = " << x << "\n";

    return 0;
}


int sum_false_range(int start, int end) {
    for (int i = start; i <= end; i++) {
        std::cout << "ID: " << i << "\n";
    }


    return 0;
}
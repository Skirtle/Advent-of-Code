#include <iostream>
#include <string>
#include <fstream>

int main() {
    std::string filename = "day1_input.txt";
    int dial = 50;
    int times_at_0 = 0;
    int times_passed_0 = 0;

    // Open and read file
    std::ifstream file(filename);
    if (!file) {
        std::cout << "Could not open file" << filename << "\n";
        return 1;
    }
    std::string line;
    while (getline(file, line)) {
        int old_dial = dial;
        std::string orig_line = line;

        // Get dircetion
        int mult = line[0] == 'R' ? 1 : -1;

        // Get rotations
        line.erase(0, 1);
        int effective_rotations = stoi(line) % 100;
        int full_rotations = int((stoi(line) - effective_rotations) / 100);

        // Pass 0?
        bool overflow = false;
        if (mult == -1 && dial - effective_rotations < 0 && dial != 0) {
            overflow = true;
        }
        else if (mult == 1 && dial + effective_rotations > 100 && dial != 0) {
            overflow = true;
        }

        // Rotate dial
        dial += mult * effective_rotations;
        dial %= 100;
        if (dial < 0) dial += 100;

        // Count 0s
        if (dial == 0) times_at_0++;
        times_passed_0 += full_rotations + overflow;


        /*std::cout << old_dial << ", dial rotated " << orig_line << " to point at " << dial;
        if (full_rotations > 0) std::cout << ", did " << full_rotations << " full rotations";
        if (overflow) std::cout << " and passed 0";
        std::cout << "\n";*/

    }


    file.close();
    std::cout << "Dial: " << dial << "\n";
    std::cout << "Times landed at 0: " << times_at_0 << "\n";
    std::cout << "Times passed 0: " << times_passed_0 << "\n";
    std::cout << "Sum: " << times_at_0 + times_passed_0 << "\n";

    return 0;
}
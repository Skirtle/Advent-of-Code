#include <iostream>
#include <string>
#include <fstream>

long sum_false_range(long start, long end);
bool isdigit(char c);
long* get_factors(long num);

int main() {
    long invalid_sum = 0;
    std::string filename = "../Inputs/day2_input.txt";

    // Open and read file
    std::ifstream file(filename);
    if (!file) {
        std::cout << "Could not open file '" << filename << "'\n";
        return 1;
    }

    std::string line;
    getline(file, line);
    long start_id = 0, end_id = 0;
    bool found_sep = false;
    for (int i = 0; i < line.length(); i++) {
        char c = line[i];
        
        // char is not a digit (should only be , and -)
        if (!isdigit(c)) {
            if (c == '-') found_sep = true;
            else if (c == ',') {
                invalid_sum += sum_false_range(start_id, end_id);
                start_id = 0;
                end_id = 0;
                found_sep = false;
            }
            else continue; // Ignore illegal chars
        }
        else {
            if (found_sep) {

                end_id = end_id * 10 + (c - '0');
            }
            else {

                start_id = start_id * 10 + (c - '0');
            } // Check if we are at the end of the line
            if (i == line.length() - 1) {
                std::cout << start_id << " " << end_id << "\n";
                invalid_sum += sum_false_range(start_id, end_id);
            }
        }


    }
    
    file.close();

    // Show results
    std::cout << "Sum of invalid IDs: " << invalid_sum << "\n";

    return 0;
}


long sum_false_range(long start, long end) {
    std::cout << start << "-" << end << "\n";
    if (end < start) return -1;
    long sum = 0;
    for (long id = start; id <= end; id++) {
        std::string id_str = std::to_string(id);

        // The invlaid IDs are now any ID that are ALL repeated sequeneces
        // 1212121212 is invalid due to 5 repeated 12s
        // We need to get the length of the ID and, for each factor, split it that many times and check if each sequence matches (including splitting each character by itself, but excluding the entire number by itself)
    }


    return sum;
}

bool isdigit(char c) {
    return c >= '0' && c <= '9';
}
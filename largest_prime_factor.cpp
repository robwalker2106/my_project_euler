/*
This script is to find the largest prime factor from a number.
This is promblem 3 on www.ProjectEular.net.
*/

#include <iostream>

int main(){

    std::cout << "Input an integer to determine its largest prime: ";
    long int num {0};
    std::cin >> num;

    long int i {num};
    int x {2};
    while (x < i) {
        if (i % x == 0){
            i /= x;
        }
        else {
            x += 1;
        }
    }
    std::cout << "The largest prime factor of " << num << " is " << x << "." << std::endl; 

}
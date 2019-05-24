/*
This script is to find the largest prime factor from the number
600851475143.  This is promblem 3 on www.ProjectEular.net.
*/

#include <iostream>

int main(){
    int x = 2;
    int64_t num;
   
    std::cout << "Input an integer to determine its largest prime: ";
    std::cin >> num;

    int64_t i = num;
    while (x < i) {
        if (i % x == 0){
            i = i / x;
        }
        else{
            x = x + 1;
        }
    }
    std::cout << "The largest prime factor of " << num << " is " << x << "." << std::endl; 

}
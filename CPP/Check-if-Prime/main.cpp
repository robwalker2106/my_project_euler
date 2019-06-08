
/*
 * This is a simple program that will be used to check if
 * an inputed number is a prime number.
 */


#include <iostream>
#include <math.h>

int main(){
    std::cout << "Enter an number to check if it is a prime number: ";
    
    int num{0};
    std::cin >> num;
    int r = floor(sqrt(num));
    int f{5};
    bool prime{true};
    char notPrime{' is not a prime number.'};
    char isPrime{' is a prime number.'};
    
    if (num == 1){
        std::cout << num << notPrime << std::endl;
    } else if (num == 2 || num == 3) {
        std::cout << "Of course " << num << isPrime << std::endl;
    } else if (num < 4) {
        std::cout << num << notPrime << std::endl;
    } else if (num % 2 == 0){
        std::cout << num << notPrime << std::endl;
    } else if (num < 9){
        std::cout << num << isPrime << std::endl;
    } else if (num % 3 == 0){
        std::cout << num << notPrime << std::endl;
    } else {
        while (f <= r){
            if (num % f == 0){
                std::cout << num << notPrime << std::endl;
                prime = false;
                break;
            } else if (num % (f+2) == 0){
                std::cout << num << notPrime << std::endl;
                prime = false;
                break;
            }
            f += 6;
        }
    }
    if (prime){
        std::cout << num << isPrime << std::endl;
    }
    
    return 0;
}

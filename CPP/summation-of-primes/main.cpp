#include <iostream>

#include <iostream>
#include <math.h>

using std::cout;
using std::cin;
using std::endl;



int main(){
    cout << "Enter an number to check if it is a prime number: ";
    
    int num{0};
    cin >> num;
    cout << isPrime(num)
    
    
    return 0;
}

bool isPrime(num){
    
    int r = floor(sqrt(num));
    int f{5};

    if (num == 1){
        return false;
    } else if (num == 2 || num == 3) {
        return true;
    } else if (num < 4) {
        return false;
    } else if (num % 2 == 0){
        return false;
    } else if (num < 9){
        return true;
    } else if (num % 3 == 0){
        return false;
    } else {
        while (f <= r){
            if (num % f == 0){
                return false;
            } else if (num % (f+2) == 0){
                return false;
            }
            f += 6;
        }
        return true;
    }
}


/*
 * This is a simple program that will be used to check if
 * an inputed number is a prime number.
 */


#include <iostream>
#include <math.h>

using std::cout;
using std::cin;
using std::endl;


int main(){
    cout << "Enter an number to check if it is a prime number: ";
    
    int num{0};
    cin >> num;
    int r = floor(sqrt(num));
    int f{5};
    bool prime{true};
    std::string notPrime {" is not a prime number."};
    std::string isPrime {" is a prime number."};
    
    if (num == 1){
        cout << num << notPrime << endl;
    } else if (num == 2 || num == 3) {
        cout << "Of course " << num << isPrime << endl;
    } else if (num < 4) {
        cout << num << notPrime << endl;
    } else if (num % 2 == 0){
        cout << num << notPrime << endl;
    } else if (num < 9){
        cout << num << isPrime << endl;
    } else if (num % 3 == 0){
        cout << num << notPrime << endl;
    } else {
        while (f <= r){
            if (num % f == 0){
                cout << num << notPrime << endl;
                prime = false;
                break;
            } else if (num % (f+2) == 0){
                cout << num << notPrime << endl;
                prime = false;
                break;
            }
            f += 6;
        }
    }
    if (prime){
        cout << num << isPrime << endl;
    }
    
    return 0;
}

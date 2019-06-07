#include <iostream>
/*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
 * get 3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of all the 
 * multiples of 3 or 5 below 1000.
 * 
 */

int main(){
    std::cout << "Enter a number to add up the multiples of 3 and 5 below the given number: " << std::endl;
    int num {0};
    std::cin >> num;
    int ans {0};
    for (int i{num -1}; i >= 0; --i){
        if(i % 15 == 0 || i % 3 == 0 || i % 5 == 0)
            ans += i;
    }
    std::cout << ans << std::endl;
    return 0;
}

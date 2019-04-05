#include <iostream>
#include <ctime>
#include <string>

using namespace std;

int squareDigit(int& number){
    int newNumber = 0;
    while (number > 0){
        newNumber += (number%10)*(number%10);
        number /= 10;
    } 
    return newNumber;
}

int getStuck(int number, int cache[]){
    number = squareDigit(number);
    int ogNumber = number;
    
    while (1){
        if (!cache[number]){ // not in the cache
            number = squareDigit(number);
            if (number == 1 || number == 89){
                cache[ogNumber] == number;
                return number;
            }
        }
        
        else{
            cache[ogNumber] == cache[number];
            return number;
        }
    
    }
    
}


int main(){
    
    clock_t start = clock();
    
    int cache[600] = {0};

    int  count = 0;
    for (int i = 1; i < 10000000; i++){
        if (getStuck(i, cache) == 89)
            count++;
    }
    
    
    cout << count << endl;
    cout << (double)(clock() - start)/CLOCKS_PER_SEC << endl;
    return 0;
}
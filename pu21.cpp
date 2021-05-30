/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

#include <iostream>

int main()
{
    int sum_A,sum_B,final_Sum;

    final_Sum = 0;

    for(int i = 1; i<10000; i++)
    {
        sum_A = 0;
        for(int a = 1; a<i; a++)
        {
            if(i%a == 0)
            {
                sum_A += a;
            }
        }
        sum_B = 0;
        for(int b = 1; b<sum_A; b++)
        {
            if(sum_A%b == 0)
            {
                sum_B += b;
            }
        }
        if(sum_B == i && sum_A != sum_B)
        {
            final_Sum += i;
        }
    }
    std::cout << final_Sum << "\n";;
    return 0;
}

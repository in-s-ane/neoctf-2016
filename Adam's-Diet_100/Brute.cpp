#include <iostream>

int main()
{
    int a = 1,
        c = 2,
        d = 3;
    int target = 13333337;
    for (int rb = 0; rb < 100000; rb++)
    {
        int b = rb;
        int n = 0;
        if (d % 3 == 2)
        {
            for (int i=0;i<d/3;i++)
            {
                n += i/2;
            }
        }
        for (int i=0;a<b;a++)
        {
            n += 1;
        }
        while (c>1)
        {
            n += c;
            c -= 20;
        }
        n += a == b;
        while (c<5)
        {
            for (int i = 0;d<b;i++)
            {
                n += b;
                for (int e = 0;a==b;i++)
                {
                    n--;
                    b--;
                }
                b--;
                a--;
            }
            c++; //C++ :D
        }
        if (n >= 2689)
            n -= 2689;
        if (a+b+c+d > 50)
            n=0;
        if (rb % 1000 == 0) std::cout << rb << "\n";
        if (n == target)
        {
            std::cout << "Found! " << rb << "\n";
            return 0;
        }
    }
    std::cout << "Found nothing\n";
    return 0;
}

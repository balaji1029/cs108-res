/*

This program implements binary search.

It takes as input a number n (the number of elements to be considered).
It then takes in n numbers in sorted order. It then takes as input the number to be found, k.
If the element is found, it outputs the position of the first occurrence of the item in the list,
else the program outputs 0.

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef int64_t ll;

int main()
{

    ll n;

    cin >> n;
    ll a[n];
    for (ll i = 0; i < n; i++)
    {

        cin >> a[i];
    }

    ll k;
    cin >> k;

    ll st = 0, end = n - 1;
    int c=0;

    while (end > st)
    {

        ll mid = (st) / 2 + (end) / 2;

        if (a[mid] < k)
        {

            st = mid + 1;
        }
        else if (a[mid] == k)
        {
            end = mid;
            if (st == end)
                break;
        }
        else
        {

            end = mid - 1;
        }
        c++;
        if(c>n)
        break;
    }
    int p = st + 1;
    if (a[st] == k)
    {

        cout << p << "\n";
    }
    else
    {

        cout << 0 << "\n";
    }

    return 0;
}
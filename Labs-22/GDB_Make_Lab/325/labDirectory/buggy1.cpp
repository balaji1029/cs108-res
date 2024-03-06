/*
This program takes as input a number n (the number of elements to be considered >=1).
It then takes in n numbers and finds out the maximum and minimum of those numbers.

(Assume no number larger than 10^18 or smaller than -10^18 is given)

*/

#include <iostream>
#include <vector>

using namespace std;

typedef int64_t ll;

int main(){



    ll n;
    cin>>n;
      ll a[n];

    ll maxi=-1e18;
    ll mini=1e18;

    for(ll i=0;i<n;i++){

        cin>>a[i];

        if(a[i]-maxi>0){

            maxi=a[i];
        }else{

            mini=a[i];
        }
    }

    cout<<"Maximum: "<<maxi<<"\n"<<"Minimum: "<<mini<<"\n";

    return 0;
}
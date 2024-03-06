/*
This program takes as input a number n (the number of elements to be considered).
It then takes in n numbers. Then it takes as input a number k (<=n).

It then outputs the sum of all contiguous subarrays having size = k

(Each subarray sum is printed in a newline)

(Assume no number larger than 10^18 or smaller than -10^18 is given)

*/

#include <iostream>
#include <vector>

using namespace std;

typedef uint64_t ll;

int main(){

    ll n,k;
    cin>>n;

    vector<ll> a(n);

    for(ll i=0;i<n;i++){

        cin>>a[i];
    }

    cin>>k;

    for(ll i=0;i+k<n;i++){
        
        ll sum=0;

        for(ll j=i;j<=i+k;j++){

            sum+=a[i];
        }

        cout<<sum<<"\n";
    }
    
    return 0;
}
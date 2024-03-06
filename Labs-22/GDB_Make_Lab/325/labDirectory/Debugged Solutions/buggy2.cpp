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

int main(){

    ll n;
    cin>>n;
    vector<ll> a(n);

    for(ll i=0;i<n;i++){

        cin>>a[i];
    }

    ll k;
    cin>>k;

    ll st=0,end=n-1, mid;

    while((end-st)>1){

        mid=(end+st)/2;

        if(a[mid]<k){

            st=mid;
        }else if(a[mid]>=k){

            end=mid;
        }
    }

    if(a[st]==k){

        cout<<st+1<<"\n";
    }else if(a[end]==k){
      
        cout<<end+1<<"\n";
    }
    else{

        cout<<0<<"\n";
    }


    return 0;
}
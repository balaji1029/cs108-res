/*

This program takes as input two numbers, n and k, and finds 
n^k modulus 1000000007 (1e9+7) using binary exponentiation.

Binary exponentiation is a method of exponentiation in O(log k),
instead of the usual O(k).

*/

#include <iostream>
#include <vector>

using namespace std;

int binary_exponentiation(int a, int b){
    
    int ans=0;

    int temp=binary_exponentiation(a,b/2);

    ans=temp*temp;

    ans%=1000000007;

    return ans;
}

int main(){

    int n,k;
    cin>>n>>k;

    cout<<binary_exponentiation(n,k)<<"\n";
    
    return 0;
}
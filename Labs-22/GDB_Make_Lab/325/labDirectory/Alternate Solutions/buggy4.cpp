/*

This program takes as input two numbers, n and k, and finds 
n^k modulus 1000000007 (1e9+7) using binary exponentiation.

Binary exponentiation is a method of exponentiation in O(log k),
instead of the usual O(k).

*/

#include <iostream>
#include <vector>

using namespace std;

long long int binary_exponentiation(int a, int b){
    
    if(b==1)return a%1000000007;
  if(b==0)return 1;
  	long long int ans=0;

    long long int temp=binary_exponentiation(a,b/2);
  
	ans=temp*temp;

    ans%=1000000007;
    long long int ans2=(ans*a)%1000000007;
    if(b%2==0)return ans;
    else return (ans2);
}

int main(){

    int n,k;
    cin>>n>>k;

    cout<<binary_exponentiation(n,k)<<"\n";
    
    return 0;
}
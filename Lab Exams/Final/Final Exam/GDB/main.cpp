/*
This program takes as input the number of elements in an array. It then takes an input of all the elements of the array and sorts the given array in ascending order using bubble sort and prints it.
*/

#include<iostream>

typedef int64_t ll;
using namespace std;
int main()
{
    ll i, n, j, temp;
      cin>>n;
    ll arr[n];

    for(i=0; i<n; i++)
   	 cin>>arr[i];    

    for(i=0; i<n-1; i++)
    {
   	 for(j=0; j<i; j++)
   	 {
   		 if(arr[j]<arr[j+1])
   		 {
       		 temp = arr[j];
   			 arr[j+1] = temp;
       		 arr[j] = arr[j+1];
   		 }
   	 }
    }
    for(i=0; i<n; i++)
   	 cout<<arr[i]<<" ";
    return 0;
}

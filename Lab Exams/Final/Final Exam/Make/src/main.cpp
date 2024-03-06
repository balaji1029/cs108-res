#include<iostream>
#include "minmax.h"

using namespace std;

int main() {
    int arr[] = {1, 4, 7, 13, -10};
    int n = 5;
    int mx = maximum(arr, n);
    int mn = minimum(arr, n);
    float average = (mx + mn) / 2.0;
    cout<<"Average: "<<average<<endl;
    return 0;
}
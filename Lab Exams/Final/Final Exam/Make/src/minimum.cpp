int minimum(int arr[], int n) {
    int mn = arr[0];
    for(int i=1;i<n;i++) {
        if(arr[i] < mn)
            mn = arr[i];
    }
    return mn;
}
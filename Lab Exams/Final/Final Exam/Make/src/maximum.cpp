int maximum(int arr[], int n) {
    int mx = arr[0];
    for(int i=1;i<n;i++) {
        if(arr[i] > mx)
            mx = arr[i];
    }
    return mx;
}
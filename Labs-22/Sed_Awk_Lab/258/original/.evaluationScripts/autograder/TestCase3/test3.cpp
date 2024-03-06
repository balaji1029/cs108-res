#include<iostream>
#include<string>

using namespace std;

void pprint(string s){
    static int i = 0;
    cout << i;
    cout << s << endl;
    i++;
}

void miniprintf()
{
    return;
}

int main(int argc, char* argv[])
{   
    int printf_k = 73;
    if(argc < 2)
    {
        printf("Wrong input");
        exit(1);
    }
    printf  ("Printing #\n");
    for(int i=0; i<argc; i++)
    {
        printf("#\n");
    }    
    return 0;
}

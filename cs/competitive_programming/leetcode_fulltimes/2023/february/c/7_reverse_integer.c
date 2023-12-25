#include <limits>
int reverse(int x){
    int k=0;
    int rev=0;
    while(x!=0)
    {
        if(rev>INT_MAX/10 || rev<INT_MIN/10)
        return 0;
        k=x%10;
        rev=rev*10+k;
        x=x/10;
    }
    return rev;

}

int reverse(int x){

    int tmp = 0;
    int rev = 0;

    while(x!=0){

        tmp = x%10;
        if(rev>INT_MAX/10 || rev<INT_MIN/10){
            return 0;
        }

        rev = 10*rev+tmp;
        x = x/10;
    }
    return rev;


}
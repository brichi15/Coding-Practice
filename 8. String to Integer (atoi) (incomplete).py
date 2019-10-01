#include <stdio.h>      
#include <math.h>       

int myAtoi(char * str){
    
    int length = strlen(str);
    
    
    int i;
    
    for(i=0;i<length;i++){
        
        if(str[i] != ' '){
            
            if((str[i]<'0' || str[i]>'9') && (str[i] != '-' && str[i] != '+')) return 0;
            break;
        }
    }
    
    
    int negflag = 0;
    int posflag = 0;
    int new = 0;
    int exp = 0;
    long sum = 0;
    
    for(i=length;i>=0;i--){
        if(str[i] == '-')negflag = 1;
        else if(str[i] == '+')posflag = 1;
        else if(str[i] >= '0' && str[i] <= '9'){      //acceptable character
            if(new == 0){
                sum = 0;
                exp = 0;
                new = 1;
            }
            
            sum += pow(10,exp)*(str[i] - '0');
            exp++;
        
        }
        else if(new == 1 && (str[i] > '9' || str[i] < '0')){
            new =0;
        }
        
    }
    
    if(negflag == 1 && posflag == 1) return 0;
        
    if(sum > INT_MAX && negflag == 0)return INT_MAX;
    else if(sum > INT_MAX && negflag == 1)return INT_MIN;
    
    if(negflag == 1 ){

        return sum*(-1);
    }
    
    return sum;
}


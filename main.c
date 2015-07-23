#include <stdio.h>
#include <string.h>

int main(void){
    char *path="reading36.txt";
    FILE *file=fopen(path,"r");
    
    char ch;
    while(fscanf(file,"%c",&ch)==1){
        if(ch>=' ' && ch<='~') printf("%c",ch);
        if(ch==10 || ch==13) printf("%c",ch);
    }
    
    return 0;
}


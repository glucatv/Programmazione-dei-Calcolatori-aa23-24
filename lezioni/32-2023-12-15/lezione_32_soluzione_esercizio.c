#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void bubble_sort(char**, int );

int main(int n, char *args[]){
	
	bubble_sort(args+1, n-1);
	
	for(int i = 1; i < n; i++){
			printf("%s\n", args[i]);
	}
}


void bubble_sort(char *a[], int n){
	int ordinata = 0; // False
    int i, c = 0;
    char *t;
    
    while ( ordinata == 0){
        ordinata = 1;
        for (i = 0; i < n-1-c; i++){
            if ( strcmp(a[i], a[i+1]) > 0 ){
                ordinata = 0;
                t = a[i];
                a[i] = a[i+1];
                a[i+1] = t;
            }
		}
		c++;
		
	}
}

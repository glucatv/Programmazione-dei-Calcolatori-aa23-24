#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>


int str_to_int0(char*);
int str_to_int(char*, int*);

int main(int n, char *args[]){
	float x, y;
	
	for(int i = 1; i < n; i++){
		if ( sscanf(args[i], "%f,%f", &x, &y) == 2){
			printf("x = %f; y = %f\n", x, y);
		}	
	}
}


int main0(int n, char *args[]){
	int v, somma = 0;
	for(int i = 1; i < n; i++){
		somma += str_to_int0(args[i]);	
	}
	printf("%d\n", somma);
	
	somma = 0;
	for(int i = 1; i < n; i++){
		if ( str_to_int(args[i], &v) == 1){
			somma += v;
		}	
	}
	printf("%d\n", somma);
	
	somma = 0;
	for(int i = 1; i < n; i++){
		if ( sscanf(args[i], "%d", &v) == 1){
			somma += v;
		}	
	}
	printf("%d\n", somma);
}

int str_to_int(char *a, int *q){
/*
 * Converte a in int. Ritorna 0 in caso di errore, 1 in caso di successo.
 * 
 * In caso di successo, l'intero viene scritto in posizione q
 * 
 * */
	
	int p = strlen(a)-1;
	int k = 1;
	
	*q = 0;
	while( p >= 0){
		if (  isdigit(a[p]) ) {
			(*q) += (a[p]-'0')*k;
			p--;
			k *= 10;
			
		} else {
			return 0;
		}
	}
	
	return 1;
	
}


int str_to_int0(char *a){
	int p = strlen(a)-1;
	int n = 0;
	int k = 1;
	
	while( p >= 0){
		n += (a[p]-'0')*k; 
		p--;
		k *= 10;
	}
	
	return n;	
}

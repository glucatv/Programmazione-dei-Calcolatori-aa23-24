#include <stdio.h>

int somma(int [], int );
int *somme_parziali(int [], int);

int N = 12;  // variabile globale

int main(){
	int n;
	int a[12];
	int b[] = {50, 1, 4, 9, 61};
	int c[10] = {3, 2, 10};
	int m[1000] = {0};
	// int x[n]; no, la dimensione di x è determinata in compile time, quindi non può essere il valore di una variabile
	int i;
	int na = sizeof(a)/sizeof(int);
	
	printf("size(a) = %d\n", sizeof(a));
	
	
	for(i = 0; i < na; i++){
		a[i] = i*i+1;
	}
	
	printf("a\n");

	
	for(i = 0; i < na; i++){
		printf("%d\n", a[i]);
	}
	
	printf("b\n");
	
	for(i = 0; i < 5; i++){
		printf("%d\n", b[i]);
	}
	
	printf("c\n");
	
	for(i = 0; i < 10; i++){
		printf("%d\n", c[i]);
	}
	
	printf("somma(a) = %d\n", somma(a, na));


	int *somme = somme_parziali(a, nx\a);
	
	for(i = 0; i < na; i++){
		printf("%d\n", somme[i]);
	}
	
}

int somma(int x[], int n){
	int somma = 0;
	
	//int na = sizeof(x)/sizeof(int);
	
	printf("sizeof(x) = %d\n", sizeof(x));
	
	for(int  i = 0; i < n; i++){
		somma += x[i];
	}
	
	return somma;
}


int somma2(int x[]){
	int somma = 0;
	
	//int na = sizeof(x)/sizeof(int);
	
	printf("sizeof(x) = %d\n", sizeof(x));
	
	for(int  i = 0; i < N; i++){
		somma += x[i];
	}
	
	return somma;
}

int *somme_parziali(int x[], int n){
	/*
	 * ritorna un int s[n] tale che s[i] = x[0]+x[1]+...+x[i]
	 * */
	 
	 int i, s[n], somme = 0;
	 
	 
	 for( i = 0; i < n; i++){
		somme += x[i];
		s[i] = somme;
	 }
	 
	 return s; // non va bene, ritorna l'indirizzo di una variabile locale
}

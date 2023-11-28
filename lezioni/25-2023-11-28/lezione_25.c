#include <stdio.h>
#include <stdlib.h>

int somma(int [], int );
int *somme_parziali(int [], int);


int *somme_parziali(int x[], int n){
	/*
	 * ritorna un int s[n] tale che s[i] = x[0]+x[1]+...+x[i]
	 * */
	 
	 int i, somme = 0;
	 int *s = malloc(n*sizeof(int));
	 
	 
	 for( i = 0; i < n; i++){
		somme += x[i];
		s[i] = somme;
	 }
	 
	 return s; // la memoria allocata con malloc non viene rilasciata al termine della funzione
}


int main(){
	float pi = 3.14;
	float *x, *y;
	float *z;
	
	x = &pi; /* x prende l'indirizzo di pi*/
	
	printf("%p\n", x);
	
	/* come ottenere il valore del float puntato da x? 
	 * 
	 * risposta *x è il float puntato da x
	 * */
	 
	 printf("%f\n", *x);  /* stampa dell'elemento puntato da x*/
	 
	 y = x;
	 
	 *y += 1;  /*  il valore di *y viene incrementato di uno e assegnato a *y  */
	 
	 printf("%f\n", *x);
	 
	 float a[] = {2.71, 3.14, 0, 9.12};
	 
	 x = a;
	 
	 for(int i = 0; i < 2; i++){
		printf("%f\n", x[i]);
	 }
	 
	 // a = y; no, l'indirizzo in a non può essere modificato
	 
	 /* perché l'indicizzazione richiede costo costanti in tempo*/
	 
	 for(int i = 0; i < 4; i++){
		printf("%f\n", *(a+i)  ); /*equivale a a[i] */
	 }
	
	z = a;
	
	printf("-------------\n");
	
	for(int i = 0; i < 4; i++){
		printf("%f\n", *(z+i)  ); /*equivale a a[i] */
	 } 
	
	int *b = malloc(10*sizeof(int));
	
	for(int i = 0; i < 10; i++){
		b[i] = i;
	}
	
	printf("-------------\n");
	
	for(int i = 0; i < 10; i++){
		printf("%d\n", *(b+i)  ); /*equivale a b[i] */
	 }
	 
	int *somme =somme_parziali(b, 10);
	
		printf("-------------\n");
	
	for(int i = 0; i < 10; i++){
		printf("%d\n", *(somme+i)  ); 
	 }
}

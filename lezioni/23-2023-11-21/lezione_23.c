#include <stdio.h>

float abs_val( float ); // prototipo di funzione
float radice2( float x ); 

void main(){
	int n = 5;       /* long, intero lungo 8 byte? */
	float pi = 3.14; /* double, virgola mobile doppia precisione */
	
	// questo è una riga commentata
	
	/*
	 * OPERAZIONI ARITMETICHE
	 * 
	 * +, -, *
	 * 
	 * */
	 
	n = n/2;
	pi = (n+1)/2; /* int assegnato ad un float */
	printf("n = %d, pi = %f\n", n, pi);	
	
	pi = (n+1)/2.0; /* float assegnato ad un float */
	printf("n = %d, pi = %f\n", n, pi);
	
	pi = (1.0*(n+1))/2; /* float assegnato ad un float */
	printf("n = %d, pi = %f\n", n, pi);
	
	/*
	 * OPERATORI RELAZIONALI
	 * 
	 * ==, <=, >=, !=
	 * 
	 * */
	 
	/*
	 * OPERATORI LOGICI
	 * 
	 * && and
	 * !! or
	 * 
	 * */
	 
	 printf("La radice di %f = %f\n", 2.0, radice2(2));
	 
	 
	 /*
	  * CICLO FOR
	  * */
	  
	 int i = 2;
	 while ( i < 20 ){
		 printf("La radice di %d = %f\n", i, radice2(i));
		 i++; /* equivalente a i += 1*/
	 }
	 
	 
	 for ( int j = 2; j < 20; j++ ){
		 printf("La radice di %d = %f\n", j, radice2(j));
	 }
	 
}


float radice2(float x){
	float g = x;
	
	while ( abs_val(g*g - x) > 0.00001 ) {
		g = (g + x/g)/2;
	}

	return g;
}

float abs_val( float x ){
	if ( x < 0 ) 
		return -x; /* unica istruzione nel blocco,
					posso omettere le parentesi*/
	else
		return x;
}

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef int tiposeq;

struct sequenza {
	tiposeq *a;
	int n; // numero di elementi effettivi in a
	int c; // capacità di a, ovvero quanto spazio c'è (n <= c)
};
typedef struct sequenza sequenza;


sequenza nuova_sequenza(  );
void mostra_sequenza( sequenza );
void set_sequenza(sequenza, int, tiposeq);
tiposeq get_sequenza(sequenza, int);
int dim_sequenza(sequenza);
int cap_sequenza(sequenza);
sequenza append_sequenza(sequenza, tiposeq);
sequenza pop_sequenza(sequenza);
int isempty_sequenza(sequenza);
sequenza insert_sequenza(sequenza, int, tiposeq);
sequenza delete_sequenza(sequenza, int);


char change_case(char);
int len(char*);
char *cat(char*, char*);
sequenza trova_vocali(char*);


int main(int n, char *args[]){
	for(int i = 0; i < n; i++){
		printf("%s\n", args[i]);	
	}
}

int main1(){
	char a[] = "programmazione ";
	char b[] = "dei calcolatori";
	
	char *c = cat(a, b);
	
	if (c != NULL)
		printf("%s*\n", c); 
	
	int n = 0;
	float pi =3.14;
	
	pi = n; /* conversione implicita non pericolosa*/
	
	pi = 3.14;
	
	n = pi; /* conversione implicita pericolosa*/
	
	n = (int)pi; /*conversione esplicita*/
	
	sequenza s = trova_vocali(c);
	mostra_sequenza(s);
}


sequenza trova_vocali(char *x){
	sequenza s = nuova_sequenza();
	int i = 0;
	
	while( x[i] != '\0' ){
		if (x[i] == 'a' || x[i]=='e' ){ /* aggiungere i o e u*/
			s = append_sequenza(s, i);
		}
		i++;
	}
	
	return s;
}

int main0(){
	sequenza w = nuova_sequenza();
	int i;

	for (i = 0; i < 15; i++){
		w = append_sequenza(w, 2.0*i);
		printf("dimensione = %d; capacita' = %d\n", dim_sequenza(w), cap_sequenza(w));
		mostra_sequenza(w);
	}
	
	printf("==================================\n");
	
	w = insert_sequenza(w, 7, 3.14);
	mostra_sequenza(w);

	printf("==================================\n");
	
	while ( isempty_sequenza(w) == 0 ){
		w = pop_sequenza(w);
		printf("dimensione = %d; capacita' = %d\n", dim_sequenza(w), cap_sequenza(w));
		mostra_sequenza(w);	
	}

}



char *cat(char *x, char *y){
	/*
	 * ritorna una nuova stringa dalla concatenazione di x ed y
	 * 
	 * oppure NULL non e' possibile allocare spazio per la nuova stringa
	 * */
	char *w;
	int n = len(x);
	int m = strlen(y); /* come len, ma nella libriria string  */
	int i;
	
	w = (char*)malloc((n+m+1)*sizeof(char));
	
	if (w != NULL) {
		for(i = 0; i < n; i++){
			w[i] = x[i];
		}
		for(; i < n+m; i++){
			w[i] = y[i-n];
		}
		w[i] = '\0'; /* perche' i e' n+m*/
	}
		
	return w;
}


char change_case(char c){
	/*
	 * se c e' maiuscolo ritorna il minuscolo e viceversa
	 * se c non e' una lettera ritorna c
	 * */
	 
	 if ( c >= 'a' && c <= 'z'){
		return 'A'+c-'a';
	 }
	 if ( c >= 'A' && c <= 'Z'){
		return 'a'+c-'A';
	 }
	 return c;
} 



int len(char *s){
	/*
	 * Ritorna il numero di caratteri nella stringa s (escluso il finestringa)
	 * */
	 
	int c = 0;
	for(int i = 0; s[i] != '\0'; i++){
		c++;
	}
	return c;
}


/*************************************************************/


sequenza nuova_sequenza( ){
	/*
	 * Ritorna una nuova sequenza vuota
	 * */
	 
	sequenza v = {NULL, 0, 0};
	 
	return v;
}

void mostra_sequenza(sequenza v){
	int i;
	for(i = 0; i < v.n; i++){
		printf("%.2f ", (float)v.a[i]);
	}
	printf("\n");
}

void set_sequenza(sequenza v, int p, tiposeq x){
	v.a[p] = x;
}

tiposeq get_sequenza(sequenza v, int p){
	return v.a[p];
}

int dim_sequenza(sequenza s){
	return s.n;
}

int cap_sequenza(sequenza s){
	return s.c;
}

sequenza append_sequenza(sequenza v, tiposeq x) {
	int n = dim_sequenza(v);
	
	if ( v.n == v.c ){ // tutti gli elementi dell'array sono occupati
		v.c = 2*v.c+1;
		v.a = realloc(v.a, sizeof(tiposeq)*v.c);
	}
	
	v.a[n] = x;
	v.n ++;
	
	return v;
}

sequenza pop_sequenza(sequenza v){
	/* elimina l'ultimo elemento dalla sequenza*/
	
	v.n --;

	if (4*v.n < v.c){
		v.c = v.n*2+1;
		v.a = realloc(v.a, sizeof(tiposeq)*v.c);
	}
	
	return v;
}

int isempty_sequenza(sequenza v){
	/*
	 * Ritorna 1 se la sequenza e' vuota, 0 altrimenti
	 * */
	 
	if (v.n == 0)
		return 1;
	else
		return 0;
}

sequenza insert_sequenza(sequenza v, int p, tiposeq x){
	/*
	 * Inserisce x in posizione p di v
	 * */
	 
	v = append_sequenza(v, 0.0);
	
	for(int i = v.n-2; i >= p; i--){
		v.a[i+1] = v.a[i];
	}
	
	v.a[p] = x;
	
	return v;
}

sequenza delete_sequenza(sequenza v, int p){
	/*
	 * Elimina l'elemento in posizione p di v
	 * */
	 
	 for( int i = p; i < v.n-1; i++){
		v.a[i] = v.a[i+1];
	 }
	 
	 v = pop_sequenza(v);
	 
	 return v;
}




#include<stdio.h>
#include<stdlib.h>

struct punto {
	float x; // campi della struct
	float y;
};

typedef struct punto punto;

struct sequenza {
	float *a;
	int n; // numero di elementi effettivi in a
	int c; // capacità di a, ovvero quanto spazio c'è (n <= c)
};
typedef struct sequenza sequenza;


sequenza nuova_sequenza(  );
void mostra_sequenza( sequenza );
void set_sequenza(sequenza, int, float);
float get_sequenza(sequenza, int);
int dim_sequenza(sequenza);
int cap_sequenza(sequenza);
sequenza append_sequenza(sequenza, float);
sequenza pop_sequenza(sequenza);
int isempty_sequenza(sequenza);
sequenza insert_sequenza(sequenza, int, float);


int main(){
	sequenza w = nuova_sequenza();
	int i;

	for (i = 0; i < 13; i++){
		w = append_sequenza(w, 2.0*i);
		printf("dimensione = %d; capacita' = %d\n", dim_sequenza(w), cap_sequenza(w));
		mostra_sequenza(w);
	}
	
	printf("==================================\n");
	
	w = insert_sequenza(w, 7, 3.14);
	//	w = append_sequenza(w, 0.0);
	mostra_sequenza(w);
/*	
	printf("==================================\n");
	
	while ( isempty_sequenza(w) == 0 ){
		w = pop_sequenza(w);
		printf("dimensione = %d; capacita' = %d\n", dim_sequenza(w), cap_sequenza(w));
		mostra_sequenza(w);	
	}
*/
}

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
		printf("%.2f ", v.a[i]);
	}
	printf("\n");
}

void set_sequenza(sequenza v, int p, float x){
	v.a[p] = x;
}

float get_sequenza(sequenza v, int p){
	return v.a[p];
}

int dim_sequenza(sequenza s){
	return s.n;
}

int cap_sequenza(sequenza s){
	return s.c;
}

sequenza append_sequenza(sequenza v, float x) {
	int i, n = dim_sequenza(v);
	float *b;
	
	if ( v.n == v.c ){ // tutti gli elementi dell'array sono occupati
		v.c = 2*v.c+1;
		b = malloc(sizeof(float)*v.c);
		for(i = 0; i < n; i++){
			b[i] = v.a[i];
		}
		free(v.a);
		v.a = b;
	}
	
	b[n] = x;
	v.n ++;
	
	return v;
}

sequenza pop_sequenza(sequenza v){
	/* elimina l'ultimo elemento dalla sequenza*/
	
	v.n --;

	if (4*v.n < v.c){
		v.c = v.n*2+1;
		float *b = malloc(sizeof(float)*v.c);
		for(int i = 0; i < v.n; i++){
			b[i] = v.a[i];
		}
		free(v.a);
		v.a = b;
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

sequenza insert_sequenza(sequenza v, int p, float x){
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

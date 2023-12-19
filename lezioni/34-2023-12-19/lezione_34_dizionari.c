#include<stdio.h>
#include<stdlib.h>
#include<string.h>


struct d_item {
	char *k;
	float v;
};
typedef struct d_item d_item;

struct nodo {
	d_item info;
	struct nodo *succ;
};
typedef struct nodo nodo;

struct dict {
	nodo **a;
	int m; // numero di liste (dimensione di a)
	int n; // numero di elementi nel dizionario
};
typedef struct dict dict;

int h(char*, dict);
dict dict_init(int);
dict dict_update(dict, d_item);
nodo *lista_cerca_k(nodo*, char*);
nodo *lista_in0(nodo*, d_item );
void dict_mostra(dict);
void lista_mostra(nodo*);


int main(int n, char *args[]){
	dict d = dict_init(3);
	int i;
	d_item e;
	
	for (i = 1; i < n; i++){
		e.k = args[i];
		e.v = i;
		d = dict_update(d, e); 
	}
	
	dict_mostra(d);
}


int h(char *x, dict d){
	int out = 0;
	int i = 0;
	
	while( x[i] != '\0'){
		out = x[i]^out;
		i++;
	}
	
	return out % d.m;
}

dict dict_init(int m){
	/*
	 * Ritorna un dizionario vuoto con m liste
	 * */
	dict d;
	int i;
	
	d.a = malloc(m*sizeof(nodo*));
	d.m = m;
	d.n = 0;
	for(i = 0; i < m; i++){
		d.a[i] = NULL;
	}
	
	return d;
}

dict dict_update(dict d, d_item e){
/*
 * Se e.k e' nel dizionario ne modifica il valore in e.v.
 * Altrimenti inserisce in d la nuova coppia e
 * 
 * */
	nodo *p; 
	int lis = h(e.k, d);
	
	
	p = lista_cerca_k(d.a[lis], e.k);
	
	if ( p == NULL ) { // la chiave non è nel dizionario
		/*
		 * inseriamo e in d
		 * */
		 d.a[lis] = lista_in0(d.a[lis], e);
		 d.n++;
	} else {
		/*
		 * aggiorno il valore associato a e.k
		 * */
		p->info.v = e.v;
	}
	
	return d;
}


nodo *lista_cerca_k(nodo *x, char *k){
	/*
	 * Ritorna il puntatore al nodo contenente l'item con chiave k, 
	 * oppure NULL se k non e' una chiave del dizionario
	 * */
	nodo *p = x;
	
	while ( p != NULL ){
		if ( strcmp(p->info.k, k) == 0 ) {
			return p;
		}
		p = p->succ;
	}
	
	return NULL;
}


nodo *lista_in0(nodo* x, d_item e){
	nodo *n = malloc(sizeof(nodo));
	
	n->info = e; // un po' delicato, perche'? 
	n->succ = x;
	
	return n;
}

void dict_mostra(dict d){
	int i;
	
	for (i = 0; i < d.m; i++){
		printf("%d - ", i);
		lista_mostra(d.a[i]);
	}
}

void lista_mostra(nodo *x){
	nodo *p = x;
	
	while( p != NULL ){
		printf("(%s, %.2f) ", p->info.k, p->info.v);
		p = p->succ;
	}
	printf("\n");
}

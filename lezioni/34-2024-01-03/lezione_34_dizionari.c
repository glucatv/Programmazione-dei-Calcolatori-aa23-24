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
//esercizi
dict dict_del(dict, char*);
nodo *lista_out0(nodo *x );
dict dict_resize(dict, int);

int main(int n, char *args[]){
	dict d = dict_init(5);
	int i;
	d_item e;
	
	for (i = 1; i < n; i++){
		e.k = args[i];
		e.v = i;
		d = dict_update(d, e); 
	}
	
	dict_mostra(d);
	
	d = dict_resize(d, 3);
	
	e.k = "tre";
	e.v = 0;
	d = dict_update(d, e);
	
	dict_mostra(d);
}

/*
 * 
 * ESERCIZI DI NATALE
 * 
 * */

/*1*/
dict dict_del(dict d, char *k){
/*
 * Se k e' una chiave del dizionario d, elimina da d la coppia con chiave k.
 * Ritorna il dizionario modificato
 * 
 * */
	nodo *p; 
	int lis = h(k, d);  /*la lista in cui dovrebbe stare la coppia con chiave k*/
	d_item e;
	
	p = lista_cerca_k(d.a[lis], k);
		
	if ( p != NULL ) { // la chiave è nel dizionario
		/*
		 * Visto che non interessa mantenere un particolare ordine tra
		 * gli elementi delle liste di trabocco, scambia il contenuto
		 * del nodo puntato da p con il primo nodo della lista in modo
		 * da cancellare in testa.
		 * 
		 * */
		e = p->info;
		p->info = d.a[lis]->info;
		d.a[lis]->info = e;
		
		d.a[lis] = lista_out0(d.a[lis]);
		d.n--;
	}
	
	return d;
}

nodo *lista_out0(nodo *x ){
	/*
	 * Cancella il primo nodo della lista. Rispetto alla versione vista
	 * nelle lezioni precedenti questa non deve gestire il campo prec
	 * che in questo caso non e' presente
	 *  
	 * */
	nodo *t = x;
	
	if ( x == NULL )
		return NULL;
		
	x = t->succ;
		
	free(t);
	
	return x;
}

/*2*/

dict dict_resize(dict d, int new_m){
	dict d1 = dict_init(new_m);
	int lis;
	nodo *p;
	
	for (int i = 0; i < d.m; i++){
		while(d.a[i] != NULL){
			/* lis e' l'indice della lista in d1 dove inserire
			 * il nuovo elemento*/
			lis = h(d.a[i]->info.k, d1);
			/* nell'insierimento in d1 non e' necessario eseuire la
			 * ricerca in quanto le chiavi inserite sono tutte uniche in quanto stiamo inserendo elementi da un dizionario*/
			d1.a[lis] = lista_in0(d1.a[lis], d.a[i]->info);
			d.a[i] = lista_out0(d.a[i]);
		}
	}
	d1.n = d.n;
	free(d.a);
	return d1;
}

/****************************************************************************/


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
	printf("==================\n");
}

void lista_mostra(nodo *x){
	nodo *p = x;
	
	while( p != NULL ){
		printf("(%s, %.2f) ", p->info.k, p->info.v);
		p = p->succ;
	}
	printf("\n");
}

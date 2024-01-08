#include<stdio.h>
#include<stdlib.h>

struct nodo {
	float info;
	struct nodo *prec, *succ;
};
typedef struct nodo nodo;

/* Definizione di coda
 * 
 * La coda e' implementata con una lista concatenata e due puntatori
 * al primo e all'ultimo nodo inserito (testa e coda)
 * 
 * */
struct coda {
	nodo *h;  // head, il puntatore al primo nodo inserito
	nodo *t;  // tail, il puntatore all'ultimo nodo inserito
};
typedef struct coda coda;

coda coda_new(void);
coda coda_in(coda, float);
float coda_get(coda);
coda coda_del(coda);
int coda_empty(coda);

/**/
nodo *lista_vuota();
nodo *lista_in0(nodo*, float);
nodo *lista_in1(nodo*, float);
void lista_mostra(nodo*);
nodo *lista_cerca(nodo*, int);
nodo *lista_in(nodo*, int, float);
nodo *lista_out1(nodo*);
nodo *lista_out0(nodo*);
nodo *lista_out(nodo*, int);

int main(){
	coda q = coda_new();
	
	/* in coda i primi 10 interi */
	for(int i = 0; i < 10; i++){
		q = coda_in(q, i);
	}
	
	
	/* fintanto la coda non è vuota, stampa il 
	 * contenuto in testa alla coda e lo elinina*/
	while( coda_empty(q)==0 ){
		printf("%f\n", coda_get(q));
		q = coda_del(q);
	}
}

coda coda_new(void) {
	/*
	 * Ritorna una nuova coda vuota
	 * */
	coda c = {NULL, NULL};
	return c;
}

int coda_empty(coda c){
	/*
	 * Ritorna 1 se la coda è vuota, 0 altrimenti
	 * */
	if (c.h == NULL)
		return 1;
	return 0;
}

/*
 * Utilizza l'inserimento in posizione 1 della sotto-lista concatenata 
 * puntata da c.t per
 * aggiungere un nuovo elemento nella coda
 * 
 * */
coda coda_in(coda c, float e){
	if ( coda_empty(c)==1 ) {//la coda è vuota
		/*
		 * Il nuovo noda sara' puntato sia da h che da t in quanto primo ed
		 * ultimo nodo della coda
		 * 
		 * */
		c.h = lista_in0(c.h, e);
		c.t = c.h;
	} else {
		/* coda.t punta all'ultimo elemento inserito, inserisce in
		 *  posizione uno a partire da coda.t*/
		 c.t = lista_in1(c.t,e);
		 c.t = c.t->succ;
	}
	return c;
}


/*
 *  Ritorna il contenuto in testa alla coda 
 * */
float coda_get(coda c){
	/* si assume che la cosa non sia vuota, quindi prima di 
	 * usare la funzione deve essere verificato questo requisito*/
	return c.h->info;
}


/*
 * Utilizza la cancellazione dalla posizione 0 per eliminare
 * l'elemento in testa alla coda
 * 
 * */
coda coda_del(coda c){
	if ( coda_empty(c)==1 )  // la coda è vuota
		return c;
	c.h = lista_out0(c.h);
	if ( coda_empty(c)==1 ) // nel caso ora la coda sia vuota...
		c.t = NULL;
		
	return c;
}

/* La complessita' temporale delle funzioni implementate è costante
 * perche' lo e' la complesita' delle funzioni di inserimento e
 * cancellazione in posizione 0 o 1 di una lista concatenata*/



/********************************************/
nodo *lista_vuota(){
	return NULL;
}

void lista_mostra(nodo *x){
	nodo *p = x;
	
	while( p != NULL ){
		printf("%.2f ", p->info);
		p = (*p).succ;
	}
	printf("\n");
}

nodo *lista_in0(nodo* x, float e){
	nodo *n = malloc(sizeof(nodo));
	
	n->info = e; // equivale a (*n).info
	(*n).succ = x;
	n->prec = NULL;
	if ( x != NULL )  // se lista non vuota
		(*x).prec = n;
	
	return n;
}

nodo *lista_in1(nodo* x, float e){
	nodo *n, *p;
	
	if ( x == NULL )
		return NULL;
	
	p = x->succ;
	
	n = malloc(sizeof(nodo));
	
	n->info = e;
	n->prec = x;
	n->succ = p;
	
	x->succ = n;
	if ( p != NULL)
		p->prec = n;
		
	return x;
}

nodo *lista_cerca(nodo *x, int pos){
	/*
	 * ritorna il puntatore al nodo in posizione pos di x.
	 * Se tale nodo non esiste, la funzione ritorna NULL.
	 * 
	*/
	nodo *p = x;
	int c = 0;
	
	while( p != NULL && c != pos ) {
		p = p->succ;
		c++;
	}
	
	return p;
}

nodo *lista_in(nodo *x, int pos, float e){
	nodo *p;
	
	if (pos == 0)
		return lista_in0(x, e);
	
	p = lista_cerca(x, pos-1);
	
	if (p == NULL)
		return x;
		
	p = lista_in1(p, e);
	return x;
}

nodo *lista_out1(nodo *x){
	nodo *t;
	
	if ( x == NULL || x->succ == NULL )
		return x;
		
	t = x->succ;
	
	x->succ = t->succ;
	if (t->succ != NULL)
		t->succ->prec = x;
		
	free(t);
	
	return x;
	
}

nodo *lista_out0(nodo *x ){
	nodo *t = x;
	
	if ( x == NULL )
		return NULL;
		
	x = t->succ;
	
	if (x != NULL)
		x->prec = NULL;
		
	free(t);
	
	return x;
}

nodo *lista_out(nodo *x, int pos){
	nodo *p;
	
	if(pos == 0)
		return lista_out0(x);
		
	p = lista_cerca(x, pos-1);
	
	p = lista_out1(p);
	
	return x;
}


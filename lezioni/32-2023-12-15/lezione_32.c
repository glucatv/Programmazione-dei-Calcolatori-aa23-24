#include<stdio.h>
#include<stdlib.h>

struct nodo {
	float info;
	struct nodo *prec, *succ;
};
typedef struct nodo nodo;

nodo *lista_vuota();
nodo *lista_in0(nodo*, float);
nodo *lista_in1(nodo*, float);
void lista_mostra(nodo*);

int main(){
	nodo *a = lista_vuota();
	
	a = lista_in1(a, 1);
	a = lista_in0(a, 3.14);
	a = lista_in0(a, 2.71);
	a = lista_in0(a, 1.4);
	a = lista_in1(a, 2);
	lista_mostra(a);
}

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



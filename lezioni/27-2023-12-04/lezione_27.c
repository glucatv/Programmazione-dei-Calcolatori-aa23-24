#include<stdio.h>
#include<stdlib.h>

struct punto {
	float x; // campi della struct
	float y;
};

typedef struct punto punto;

struct sequenza {
	float *a;
	int n;
	int c;
};
typedef struct sequenza sequenza;


sequenza nuova_sequenza( int );
void mostra_sequenza( sequenza );
void set_sequenza(sequenza, int, float);
float get_sequenza(sequenza, int);
int dim_sequenza(sequenza);
sequenza append_sequenza(sequenza, float);


int main(){
	struct punto p = { 1.0, 2.9 };
	punto q = p;
	
	p.x = 3.9;
	p.y = p.x+1;
	
	printf("%f %f\n", p.x, p.y);
	printf("%f %f\n", q.x, q.y);
	
	printf("================================\n");
	
	sequenza w, s = nuova_sequenza(10);
	mostra_sequenza(s);
	w = s;
	s.a[2] = 9;
	mostra_sequenza(w);
	
	set_sequenza(w, dim_sequenza(w)-1, get_sequenza(s, 2) );
	
	mostra_sequenza(w);
	
	w = append_sequenza(w, 3.14);
	
	mostra_sequenza(w);
}

sequenza nuova_sequenza( int d ){
	/*
	 * Ritorna una nuova sequenza di d float tutti nulli
	 * */
	 
	 sequenza v;
	 int i;
	 
	 v.a = malloc(sizeof(float)*d);
	 v.n = d;
	 for(i=0; i < v.n; i++){
		v.a[i] = 0;
	 }

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

sequenza append_sequenza(sequenza v, float x) {
	int i, n = dim_sequenza(v)+1;
	float *b = malloc(sizeof(float)*n);
	
	for(i = 0; i < n-1; i++){
		b[i] = v.a[i];
	}
	b[n-1] = x;
	v.a = b;
	v.n ++;
	
	return v;
}

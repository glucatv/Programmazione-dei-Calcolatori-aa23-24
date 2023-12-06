#include<stdio.h>
#include<stdlib.h>


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
sequenza delete_sequenza(sequenza, int);


char change_case(char);

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


int main(){
	char c = 65, d = 'u';
	
	c = c+1; // ASCII
	
	printf("%d, %c\n", c, c);
	printf("%d, %c\n", d, d);
	
	printf("%c, %c, %c\n", change_case('f'), change_case('H'),
		change_case('+') );
		
	char s[] = {'p', 'y', 't', 'h', 'o', 'n', '\0'};
	char s1[] = "python";
	
	printf("%s\t%s\n", s, s1);
	
	printf("%d\n", sizeof(s1));
	
	s1[2] = '\0';
	
	printf("%s\n", s1);
	
	printf("%d\n", sizeof(s1));
	
	
	printf("%d\n", len(s1));
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
	w = delete_sequenza(w, 2);
	mostra_sequenza(w);

	printf("==================================\n");
	
	while ( isempty_sequenza(w) == 0 ){
		w = pop_sequenza(w);
		printf("dimensione = %d; capacita' = %d\n", dim_sequenza(w), cap_sequenza(w));
		mostra_sequenza(w);	
	}
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
	
	if ( v.n == v.c ){ // tutti gli elementi dell'array sono occupati
		v.c = 2*v.c+1;
		v.a = realloc(v.a, sizeof(float)*v.c);
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
		v.a = realloc(v.a, sizeof(float)*v.c);
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

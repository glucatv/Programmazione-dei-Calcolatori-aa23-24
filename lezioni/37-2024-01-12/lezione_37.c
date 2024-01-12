#include <stdio.h>
#include <stdlib.h>

int get(int matrice[][5], int r, int c){
	/*
	 * Ritorna il valore in posizione r,c di matrice
	 * */
	 
	 return matrice[r][c];
}

void set_val(int *a, int n_c, int r, int c, int v){
	a[c+n_c*r] = v;
}

int get_val(int *a, int n_c, int r, int c){
	return a[c+n_c*r];
}

int main(){
	int a[7][5];
	int n_r = 7, n_c = 5;
	int r,c, val;
	int *M = malloc(sizeof(int)*(n_r*n_c));
	int p;
	
	a[3][2] = 9;
	
	//printf("%d\n", get(a, 3, 2) );
	
	for( r = 0; r < n_r; r++){
		for ( c = 0; c < n_c; c++) {
			val = c*r+1;
			set_val(M, n_c,  r, c, val);
		}
	}
	
	for( r = 0; r < n_r; r++){
		for ( c = 0; c < n_c; c++) {
			printf("%3d ", get_val(M, n_c, r, c) );
		}
		printf("\n");
	}
	
	for(p = 0; p < n_c*n_r-1; p++){
		r = p/n_c;
		c = p%n_c;
		val = M[p];
		printf("M[%d][%d] = %d\n", r, c, val);
	}
}

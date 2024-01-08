#include <stdio.h>
#include <stdlib.h>

union item {
	int val_i;
	float val_f;
	char *val_s;
};
typedef union item item;

struct object {
	char type; // 'I' per int, 'F' per float, 'S' per *char
	item u;
};
typedef struct object object;

object parse(char*);
void print(object);
int cercapunto(char *s);

int main(int n, char *args[]){
	object *a = malloc(sizeof(object)*(n-1));
	int i;
	
	for(i = 1; i < n; i++){
		a[i-1] = parse(args[i]);
	}
	
	for(i = 0; i < n-1; i++){
		print(a[i]);
	}
}

object parse(char *s){
	object obj;
	if ( cercapunto(s) == 0 && sscanf(s, "%d", &(obj.u.val_i) ) == 1 ){
		obj.type = 'I';
	} else if (cercapunto(s) == 1 && sscanf(s, "%f", &(obj.u.val_f) ) == 1) {
		obj.type = 'F';
	} else {
		obj.type = 'S';
		obj.u.val_s = s;
	}
	return obj;
}

int cercapunto(char *s){
	/*
	 * Ritorna 1 se il numero di punti in s è  1; 0 altrimenti
	 * */
	int c = 0, i = 0;
	
	while( s[i] != '\0'){
		if (s[i] == '.')
			c++;
		if (c == 2)
			return 0;
		i++;
	}
	if (c == 1)
		return 1;
	return 0;
}

void print(object obj){
	if (obj.type == 'I')
		printf("%d\n", obj.u.val_i);
	else if (obj.type == 'F')
		printf("%f\n", obj.u.val_f);
	else
		printf("%s\n", obj.u.val_s);
}

int main0(){
	object  obj;
	
	obj.type = 'I';
	obj.u.val_i = 10;
	
	if (obj.type == 'I')
		printf("%d\n", obj.u.val_i);
	else if (obj.type == 'F')
		printf("%f\n", obj.u.val_f);
	else
		printf("%s\n", obj.u.val_s);
}

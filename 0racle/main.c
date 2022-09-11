#include<stdio.h>
int main(){
	size_t rnd=0;
	int f = open("/dev/urandom",0);


	read(f,&rnd,2);

	for(int i =0 ; i < rnd;i++)
		malloc(0x128);

	char * a = malloc(0x0);
	
	
	read(f,&rnd,2);

	for(int i =0 ; i < rnd;i++)
		malloc(0x1000);

	char * b =malloc(0);

	free(a);
	free(b);

	printf("%p\n",*(size_t *)b);
    printf("%p\n",(((size_t)b>>12)-((size_t)a>>12)));
	// printf("%p\n",(size_t)a&0xfff);
	read(0,&rnd,8);

	if((rnd& 0xfffffffff000) == ((size_t)a& 0xfffffffff000))
		puts("Success");
	else
		puts("Fail");

}

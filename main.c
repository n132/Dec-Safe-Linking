#include<stdio.h>
int main(){

	char * a = malloc(0x0);
	size_t rnd=0; 
	int f = open("/dev/urandom",0);
	read(f,&rnd,1);
	for(int i =0 ; i < rnd;i++)
	{
		// printf("%d\n",i);
		malloc(0x1000);
	}
	char * b =malloc(0);
	free(a);
	free(b);
	printf("%p\n",*(size_t *)b);
    printf("%p\n",(((size_t)b>>12)-((size_t)a>>12)));
	printf("%p\n",(size_t)a&0xfff);
	read(0,&rnd,8);
	if(rnd == (size_t)a )
		puts("Success");
	else
		puts("Fail");	

}
// Compile & run it on glibc 2.32+

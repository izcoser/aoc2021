#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE * fp = fopen("input2", "r");
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    int horizontal = 0;
    int depth = 0;
    int aim = 0;

    while ((read = getline(&line, &len, fp)) != -1) {
	int n = line[strlen(line) - 2] - '0';
	
	if(line[0] == 'f'){
		horizontal += n;
		depth += aim * n;
	}
	else if(line[0] == 'u'){
		aim -= n;
	}
	else{
		aim += n;
	}

    }

    printf("%d\n", horizontal * depth);
    return 0;
}

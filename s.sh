for((i = 1; i < 1000; ++i)); do
	echo $i
	./gen $i > in
	./a.out < in > ou1
	./brute < in > ou2
	diff -w ou1 ou2 || break
done 
	
 

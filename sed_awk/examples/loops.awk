BEGIN {
   sum = 0; 
   #example of for loop with break
   for (i = 0; i < 15; ++i) {
      sum += i; 
      if (sum > 30) break; 
      else printf "i = %d Sum = %d \n", i, sum 
   } 
}

{
   #example of exit
   sum = 0; 
   print "\n";
   for (i = 0; i < 15; ++i) {
      sum += i; 
      if (sum > 20) exit(1); 
      else printf "i = %d Sum = %d \n", i, sum 
   } 
}

END {
   #example of continue statement
   print "\n";
   for (i = 1; i <= 10; ++i) {
      if (i % 2 == 0) print i ; else continue
   } 
   
   #example of while loop
   print "\n";
   n = 1; 
   while (n < 4) { 
   print n;
   ++n;
   }
   
   #example of do while loop
   print "\n";
   n = 4; 
   do { 
   print n; 
   --n 
   } 
   while (n > 0) 
   
}

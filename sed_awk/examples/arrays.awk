BEGIN {
   fruits["mango"] = "yellow";
   fruits["orange"] = "orange";
   fruits["apple"] = "red";
}

END {
for(g in fruits) print g, fruits[g];
delete fruits["orange"];
print "\nAfter deletion"
for(g in fruits) print g, fruits[g];
}


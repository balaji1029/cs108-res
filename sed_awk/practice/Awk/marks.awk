BEGIN {
    FS = ",";
    OFS="\t";
}

/Name/ {
    $1=$1
    print $0, "Average";
    var=1
}

{
    if (var == 1) {var = 0; next; }
    $1=$1
    sum = 0;
    for(i=2; i<=NF; i++) {
        sum += $i;
    }
    print $0, sum/(NF-1);
}

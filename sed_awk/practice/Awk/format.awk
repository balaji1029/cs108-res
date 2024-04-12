BEGIN {
    FS = " ";
    OFS = ";";
}

NR == 1 {
    $1 = $1
    print $0, "Comments"
}

NR == 2 {
    $1 = $1
    for (i = 2; i <= NF; i++) {
        arr[i] = $i
    }
    print $0, "-"
}

NR > 2 {    
    $1 = $1
    reg = $1
    for (i = 2; i <= NF; i++) {
        reg = reg OFS "[A-Za-z0-9_]+\\" arr[i];
    }
    print reg
    result = (match($0, reg)) ? "Correct Submission Format" : "Wrong Submission Format"
    print $0, result
    # print ($0 ~ reg ? "YES" : "NO") 
}
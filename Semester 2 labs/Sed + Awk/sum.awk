BEGIN {
    print "Week_end,Indicator,High_industry,Value"
    FS=","
    count=1
}

NR > 1 {
    if ($3 in employment_wise){
        employment_wise[$3] += $4    
    }
    else {
        employment_wise[$3] = $4
        keys[count] = $3
        count++
    }
    net += $4
    print
}

END {
    print "====="
    print "Net :", net
    for (i = 1; i < count; i++){
        for (key in keys){
            min_key = keys[key]
            min_index = key
            break
        }
        for (key in keys){
            if (keys[key] < min_key){
                min_key = keys[key]
                min_index = key
            }
        }
        print min_key, ":", employment_wise[min_key]
        delete keys[min_index]
    }
}
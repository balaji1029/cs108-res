BEGIN {
    FS=" "
    OFS=" "
}
{
    if (match($0, /^[a-zA-Z]+ got [1-9][0-9]* medals in [a-zA-Z]+ in [0-9]{4}$/)){
        print "In", $8 ",", $1, $2, $3, $4, $5, $6 
        
    }
    else {
        print
    }
}
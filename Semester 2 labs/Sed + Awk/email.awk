BEGIN {
    print "Student ID,First Name,Middle Name,Last Name,Email-ID";
    FS=","
    OFS=","
}

NR > 1 {
    $5 = $2 $4 "@surveycorps.com"
    print
}
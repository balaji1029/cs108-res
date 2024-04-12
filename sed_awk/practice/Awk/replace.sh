awk -v input="$1" -v paragraph="$(cat $2)" 'BEGIN {
    FS = ":"
    OFS = "\n"
}

{
    cmd = "sed -E \"s/student_name/" $1 "/g;s/roll_no/" $2 "/g\" paragraph.txt"
    system(cmd)
    # "sed -E \"s/student_name/" $1 "/g;s/roll_no/" $2 "/g\" paragraph.txt"
    print "\n"
}' input.txt

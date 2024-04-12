BEGIN {
  FS=",";
}

{
  if($8 ~ /H16/) {
    M++;
  } else if($8 ~ /H1$/) {
    N++;
  } else {
    B++;
  }
}

END {
  print "H16:", M, "H1:", N, "everything else:", B;
}

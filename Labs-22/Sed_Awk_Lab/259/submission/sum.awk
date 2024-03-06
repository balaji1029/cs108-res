#!/bin/awk

BEGIN {FS=",";
s=0;
x["a"]=0; x["b"]=0; x["f"]=0; x["m"]=0; x["r"]=0;
}
{print;
 s=s+$4;
if ($3=="Agriculture") x["a"]=x["a"]+$4
else if ($3=="Banking") x["b"]+=$4
else if ($3=="Film") x["f"]+=$4
else if ($3=="Manufacturing") x["m"]+=$4
else if ($3=="Railways") x["r"]+=$4
}
END {print "=====\n" "Net : " s "\nAgriculture : " x["a"] "\nBanking : " x["b"] "\nFilm : " x["f"] "\nManufacturing : " x["m"] "\nRailways : " x["r"]}


#!/bin/bash

let "n=$#-1"

if [ $1 = "max" ]; then
        max=$2

        for i in $@; do
                if [[ $i -gt $max ]]; then
                        max=$i
                fi
        done

        echo $max

elif [ $1 = "min" ]; then
        min=$2
for i in $@; do
                if [[ $i -lt $min ]]; then
                        min=$i
                fi
        done
        echo $min

elif [ $1 = "sum" ]; then
        sum=0
        for i in $@; do
                let "sum=sum+i"
        done

        echo $sum

elif [ $1 = "avg" ]; then
        sum=0

        for i in $@; do

                let "sum=sum+i"
        done

        let "sum=sum/n" 
        echo $sum

fi





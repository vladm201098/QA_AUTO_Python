#!/bin/bash

for n in {11..1}
do
   out=$(( $n % 2 ))
   if [ $out -eq 0 ]
   then
    echo "$n is even number"
   fi
done

#!/bin/bash 
echo "Введите Ваше число: "
read n

if [ "$n" -gt 15 -a "$n" -lt 45 ]
then 
echo "Ваше число больше 15 и меньше 45. Вы ввели число $n"
else
echo "Ваше число меньше 15 или больше 45. Вы ввели число $n"
fi 
#!/bin/bash 
echo  "Введите Ваше число: "
read n

if [ "$n" -lt -1 -o "$n" -eq 45 ]
then
echo "Ваше число меньше -1 или равно 45. Вы ввели число $n"
else
echo "Ваше число не соответствует заданному условию меньше -1 или равно 45. Вы ввели число $n"
fi


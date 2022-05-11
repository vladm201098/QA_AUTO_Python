#!/bin/bash 

PS3="Хотите ли Вы установить python?"

select variable in Да Нет;
do
	case $variable in
		Да  ) echo "Вы выбрали установить python"
		break;;
		Нет ) echo "Не правильный вариант"
		break;;
		*   ) echo "Выберите действие!!!";;
esac
done

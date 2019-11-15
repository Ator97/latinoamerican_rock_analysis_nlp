#!/bin/bash

#Author: Oscar Gutiérrez Castillo
#Fecha de creacion: 14 - nov - 2019
#Fecha de modificacion: 14 - nov - 2019

egrep -o -e '_[[:alnum:]]+_' mysongs.txt  | sort | uniq | egrep -o [A-Za-z0-9]+  > myartist.txt

while read l
do
	mkdir $l
	mv *$l*.json $l
	
done < myartist.txt





#!/bin/bash
# take-links.sh takes the links of es.famousbirthdays.com/

months=(january february march april may june july august september october november december)
###########################################
TEMP_FILE=temp_month_file
LINKS_FILE=links_file

# colors
RESET="\e[0m"
RED="\e[0;31m"
GREEN="\e[0;32m"
YELLOW="\e[0;33m"
BLUE="\e[0;34m"

############################################
#The next step is for:
#- Generating the months with a number
#EXAMPLE:
#january1.html
#january2.html
############################################


if [ -f $TEMP_FILE ]; then
	echo -e $YELLOW"skipping $TEMP_FILE, file exists" $RESET
else
	touch $TEMP_FILE;
	echo -e $GREEN"creating a file with the months and days" $RESET
	for i in "${months[@]}"
	do
		for j in {1..2};
		do
			echo -n $i >> $TEMP_FILE;
			echo $j ".html" | tr -d ' ' >> $TEMP_FILE;
		done;
	done;
fi

############################################
#The next step is for:
	#---> FROM:
#january1.html
#january2.html
	#---> TO:
#https://es.famousbirthdays.com/january1.html
#https://es.famousbirthdays.com/january2.html
	#--- EXPLANATION: We take the links of each person
############################################

if [ -f $LINKS_FILE ]; then
	echo -e $YELLOW"skipping $LINKS_FILE, file exists" $RESET
else
	echo -e $GREEN"creating a link file..." $RESET
	while read -r LINE
	do
		echo 'https://es.famousbirthdays.com/' "$LINE" | tr -d ' ' >> $LINKS_FILE
	done < "$TEMP_FILE"
fi

if [ -f $TEMP_FILE ]; then
	echo -e $GREEN"removing $TEMP_FILE"
	rm -rf $TEMP_FILE
fi

ALL_LINKS_PEOPLE=links_href_grep

############################################
#The next step is for:
#	---> FROM:
#https://es.famousbirthdays.com/january1.html
	#---> TO:
				#<a class="tile" href="https://es.famousbirthdays.com/people/morris-chestnut.html">
#
	#--- EXPLANATION: We take the links of each person
############################################
if [ -f $ALL_LINKS_PEOPLE ]; then
	echo -e $YELLOW"skipping $ALL_LINKS_PEOPLE, file exists" $RESET
else
	echo -e $GREEN"creating all links people file..." $RESET
	while read -r LINE
	do
		curl $LINE | grep "tile__item" -A 10 | grep "href=" >> $ALL_LINKS_PEOPLE
	done < "$LINKS_FILE"
fi

# Now with this links we must clean and save only the links
############################################
#The next step is for:
	#---> FROM:
				#<a class="tile" href="https://es.famousbirthdays.com/people/morris-chestnut.html">
	#---> TO:
#https://es.famousbirthdays.com/people/morris-chestnut.html
	#--- EXPLANATION: Saving only the exact link and not the HTML
############################################
if [ -f $LINKS_FILE ]; then
	echo -e $GREEN"removing $LINKS_FILE"
	rm -rf $LINKS_FILE;
fi

ALL_LINKS_PEOPLE_FILTERED=links_to_scrape.txt
if [ -f $ALL_LINKS_PEOPLE_FILTERED ]; then
	echo -e $YELLOW"skipping $ALL_LINKS_PEOPLE_FILTERED, file exists" $RESET
else
	echo -e $GREEN"creating all links people FILTERED file..." $RESET
	while read -r LINE
	do
		echo $LINE | tr -d '\t' | awk '{print $3}' | awk -F "\"" '{print $2}' >> $ALL_LINKS_PEOPLE_FILTERED
		echo "copied: $LINE"
	done < "$ALL_LINKS_PEOPLE"
fi

############################################
#Now, i have all the links
#LIKE THIS:
#https://es.famousbirthdays.com/people/morris-chestnut.html
#https://es.famousbirthdays.com/people/ali-siadat.html
#https://es.famousbirthdays.com/people/frank-langella.html
#https://es.famousbirthdays.com/people/paolo-guerrero.html
############################################

if [ -f $ALL_LINKS_PEOPLE ]; then
	echo -e $GREEN"removing $ALL_LINKS_PEOPLE"
	rm -rf $ALL_LINKS_PEOPLE;
fi

FOLDAR_NAME=data
mkdir $FOLDAR_NAME
mv $ALL_LINKS_PEOPLE_FILTERED $FOLDAR_NAME
echo -e $GREEN"ALL LINKS SAVED, FILENAME:"$BLUE $FOLDAR_NAME/$ALL_LINKS_PEOPLE_FILTERED $RESET
#xargs -n 1 curl -O < "$ALL_LINKS_PEOPLE_FILTERED"

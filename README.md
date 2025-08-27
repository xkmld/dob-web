# Date of Birth Web
## Scaping
### Take links
Using the `take-links.sh` script. You can change how many days yo want in the `for j in ...`
```bash
	for i in "${months[@]}"
	do
		for j in {1..2}
		#for j in {1..31}
		do
			echo -n $i >> $TEMP_FILE;
			echo $j ".html" | tr -d ' ' >> $TEMP_FILE;
		done;
	done;
```
### Scraping info
With the file `data/links_to_scrape.txt` now is python time.
## Useful data
```bash
# For script
https://atareao.es/tutorial/scripts-en-bash/arrays-en-bash/
https://stackoverflow.com/questions/43158140/way-to-create-multiline-comments-in-bash
https://unix.stackexchange.com/questions/156579/how-do-i-remove-spaces-from-shell-variables
https://unix.stackexchange.com/questions/279760/how-can-we-use-multiple-variables-in-single-for-loop-in-shell-script
https://stackoverflow.com/questions/638975/how-do-i-tell-if-a-file-does-not-exist-in-bash
https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
https://askubuntu.com/questions/992336/how-to-extract-certain-data-from-a-line
```

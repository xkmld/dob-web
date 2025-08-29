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

# Python Scraping
https://j2logo.com/python/web-scraping-con-python-guia-inicio-beautifulsoup/
https://realpython.com/beautiful-soup-web-scraper-python/#find-elements-by-class-name-and-text-content
https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
https://blog.finxter.com/5-best-ways-to-convert-html-strings-to-plain-text-in-python/
https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
https://www.geeksforgeeks.org/python/python-removing-newline-character-from-string/
https://www.geeksforgeeks.org/python/python-remove-unwanted-spaces-from-string/
https://stackoverflow.com/questions/11505318/meaning-of-i-in-vim-and-how-to-not-show-them
https://stackoverflow.com/questions/31565609/python-while-loop-condition-check-for-string
https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
https://www.digitalocean.com/community/tutorials/how-to-construct-while-loops-in-python-3

https://stackoverflow.com/questions/43982002/extract-the-src-attribute-from-an-img-tag-using-beautiful-soup
https://stackoverflow.com/questions/43982002/extract-the-src-attribute-from-an-img-tag-using-beautiful-soup
https://stackoverflow.com/questions/68753721/how-to-find-second-div-from-html-in-python-beautifulsoup
https://medium.com/@spaw.co/using-find-next-element-in-beautifulsoup-8a97cbef38eb
https://wiki.python.org/moin/WorkingWithTime
https://stackoverflow.com/questions/26745519/converting-dictionary-to-json
https://stackoverflow.com/questions/23669024/how-to-strip-a-specific-word-from-a-string
https://stackoverflow.com/questions/24756915/creating-a-mapping-variable-in-python
https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
https://www.w3schools.com/python/python_file_write.asp
https://www.programiz.com/python-programming/methods/string/lower
https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories
https://www.askpython.com/python/examples/get-month-name-from-number
https://www.w3schools.com/python/python_functions.asp
https://stackoverflow.com/questions/59812779/for-loop-string-line-by-line-not-letter-by-letter
```

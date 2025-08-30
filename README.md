# Date of Birth Web

## Execution Order
```bash
Before: Install psql, install python3...

- Environment creation: make venv (and run the commands printed: source venv/bin/activate...)
- Take links: make links
- Scrape links: make scrape
    - Scrape images
- Insert data to database
```

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

# SQL
https://www.geeksforgeeks.org/sql/sql-create-database/
https://www.w3schools.com/sql/sql_create_db.asp

# Postgres
https://shape.host/resources/como-instalar-postgresql-en-debian-12
https://www.postgresql.org/download/linux/debian/
https://wiki.debian.org/es/PostgreSql
https://www.w3resource.com/PostgreSQL/snippets/import-sql-dump-into-postgresql-database.php
https://stackoverflow.com/questions/51404594/syntax-error-auto-increment
https://neon.com/postgresql/postgresql-indexes/postgresql-create-index
https://www.postgresql.org/docs/8.0/sql-createuser.html
https://stackoverflow.com/questions/22483555/postgresql-give-all-permissions-to-a-user-on-a-postgresql-database
https://dba.stackexchange.com/questions/33943/granting-access-to-all-tables-for-a-user
https://commandprompt.com/education/how-to-grant-permissions-on-all-tables-to-a-postgresql-user/
https://neon.com/postgresql/postgresql-indexes/postgresql-create-index

# Insert data python to postgres
https://stackoverflow.com/questions/26496388/how-to-connect-python-to-postgresql
https://unix.stackexchange.com/questions/345814/gcc-error-installing-psycopg2-package-for-python3-on-centos-7-3      # important for (sudo apt install libpq-dev)
https://stackoverflow.com/questions/22483555/postgresql-give-all-permissions-to-a-user-on-a-postgresql-database
https://dev.to/saint_vandora/resolving-psycopg2errorsinsufficientprivilege-4nl4
https://packages.ubuntu.com/noble/libpq-dev
https://stackoverflow.com/questions/20199126/reading-json-from-a-file
https://stackoverflow.com/questions/5767325/how-can-i-remove-a-specific-item-from-an-array-in-javascript
https://stackoverflow.com/questions/30229231/python-save-image-from-url
https://stackoverflow.com/questions/19235686/psycopg2-insert-into-table-with-placeholders
https://www.digitalocean.com/community/tutorials/python-string-comparison
https://stackoverflow.com/questions/69418919/what-is-the-difference-between-connection-commit-and-cursor-executecommit
https://stackoverflow.com/questions/42767733/inserting-date-into-postgresql-columns-from-and-to
https://stackoverflow.com/questions/4231491/how-to-insert-null-values-into-postgresql-database-using-python
https://stackoverflow.com/questions/9325017/error-permission-denied-for-sequence-cities-id-seq-using-postgres
https://stackoverflow.com/questions/5342440/reset-auto-increment-counter-in-postgres
```

## Add scheme.sql to postgres
```
postgres@debian:~$ psql 
postgres=# CREATE DATABASE dob_web;
CREATE DATABASE
postgres=#
\q
postgres@debian:~$ psql -d dob_web -f scheme.sql     #(first add scheme.sql in /var/lib/postgresql)
```

## Permissions
Some of them are innecesary...
```sql
CREATE USER dob_user WITH PASSWORD 'dob_pass';
GRANT ALL PRIVILEGES ON DATABASE dob_web TO dob_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO dob_user;
GRANT USAGE ON SCHEMA PUBLIC TO dob_user;
GRANT CONNECT ON DATABASE dob_web TO dob_user;
GRANT ALL PRIVILEGES ON DATABASE dob_web TO dob_user;

GRANT INSERT, SELECT, UPDATE, DELETE ON TABLE famous TO dob_user;
```

## Youtube Serie
[![Watch the video](https://img.youtube.com/vi/4hnB018iWzg/hqdefault.jpg)](https://youtu.be/4hnB018iWzg)

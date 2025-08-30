UTILS_FOLDER=utils/
SCRIPTS_FOLDER=$(UTILS_FOLDER)scripts/
SCRAPER_FOLDER=$(UTILS_FOLDER)scraper/

.DEFAULT_GOAL := help

links:
	/bin/bash "$(SCRIPTS_FOLDER)take-links.sh"

venv:
	/bin/bash "$(SCRIPTS_FOLDER)/create-venv.sh"

requirements:
	pip install -r $(SCRAPER_FOLDER)/requirements.txt > logs
	rm logs

scrape: requirements
	python3 utils/scraper/scrape.py

help:
	echo "COMMANDS: links, venv, requirements, scrape"

inserter: requirements
	python3 utils/inserter/inserter.py

insert: 
	make inserter

.PHONY: links venv scrape help requirements

UTILS_FOLDER=utils/
SCRIPTS_FOLDER=$(UTILS_FOLDER)scripts/
SCRAPER_FOLDER=$(UTILS_FOLDER)scraper/
INSERTER_FOLDER=$(UTILS_FOLDER)inserter/

.DEFAULT_GOAL := help

links:
	/bin/bash "$(SCRIPTS_FOLDER)take-links.sh"

venv:
	/bin/bash "$(SCRIPTS_FOLDER)/create-venv.sh"

requirements:
	pip install -r $(SCRAPER_FOLDER)/requirements.txt >/dev/null

scrape: requirements
	python3 utils/scraper/scrape.py

help:
	echo "COMMANDS: links, venv, requirements, scrape"

inserter:
	pip install -r $(INSERTER_FOLDER)/requirements.txt >/dev/null
	python3 utils/inserter/inserter.py

insert: 
	make inserter

.PHONY: links venv scrape help requirements

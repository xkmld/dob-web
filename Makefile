SCRIPTS_FOLDER=utils/scripts/
SCRAPER_FOLDER=utils/scraper/

.DEFAULT_GOAL := help

links:
	/bin/bash "$(SCRIPTS_FOLDER)take-links.sh"

venv:
	/bin/bash "$(SCRIPTS_FOLDER)/create-venv.sh"

scrape: requirements
	echo "Not yet"

requirements:
	pip install -r $(SCRAPER_FOLDER)/requirements.txt

help:
	echo "COMMANDS: links, venv, scrape"

.PHONY: links venv scrape help requirements

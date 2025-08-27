UTILS_FOLDER=utils/
SCRIPTS_FOLDER=$(UTILS_FOLDER)scripts/
SCRAPER_FOLDER=$(UTILS_FOLDER)scraper/

.DEFAULT_GOAL := help

links:
	/bin/bash "$(SCRIPTS_FOLDER)take-links.sh"

venv:
	/bin/bash "$(SCRIPTS_FOLDER)/create-venv.sh"

requirements:
	pip install -r $(SCRAPER_FOLDER)/requirements.txt

scrape: requirements
	echo "Not yet"

help:
	echo "COMMANDS: links, venv, requirements, scrape"

.PHONY: links venv scrape help requirements

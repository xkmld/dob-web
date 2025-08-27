SCRIPTS_FOLDER=utils/scripts/

.DEFAULT_GOAL := help

links:
	/bin/bash "$(SCRIPTS_FOLDER)take-links.sh"

venv:
	/bin/bash "$(SCRIPTS_FOLDER)/create-venv.sh"

scrape:
	echo "Not yet"

help:
	echo "COMMANDS: links, venv, scrape"

.PHONY: links venv scrape help

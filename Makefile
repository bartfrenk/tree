NAME=Tree
.DEFAULT_GOAL:=help

.PHONY: clean
clean: ## Remove all generated artifacts
	rm -rf docs/build

.PHONY: docs
docs: ## Generate package documentation
docs: docs/build/index.html

.PHONY: help
help: ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | \
	fgrep -v fgrep | sed -e 's/## */##/' | column -t -s##

docs/build/index.html: docs/source src
	sphinx-build $< $@

docs/build:
	mkdir -p $@

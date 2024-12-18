

# ==================================================================================== #
# HELPERS
# ==================================================================================== #


## help: print this help message
.PHONY: help
help:
	@echo 'Usage: '
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

# ==================================================================================== #
# Days
# ==================================================================================== #

## d1: run the first days challange
.PHONY: d1
d1:
	@python3 src/day_01/main.py

## d2: run the second days challange
.PHONY: d2
d2:
	@python3 src/day_02/main.py


## test: run the tests
.PHONY: test
test:
	@pytest
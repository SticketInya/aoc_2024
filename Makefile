

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

## run: run the nth days challange. Pass variable day=01 to run the first, day=02 to run the second and so on.
.PHONY: run
run:
	@python3 src/day_$(shell printf "%02d" $(day))/main.py

## test: run the tests. Pass variable day=01 to run tests for a specific day, otherwise runs all tests.
.PHONY: test
test:
ifdef day
	@pytest src/day_$(shell printf "%02d" $(day))/
else
	@pytest
endif
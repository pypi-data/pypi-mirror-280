# Detect platform
ifeq ($(OS), Windows_NT)
	PLATFORM := win-64
	PYTHON := python
else
	uname := $(shell sh -c 'uname 2>/dev/null || echo unknown')
	ifeq ($(uname), Darwin)
		PLATFORM := osx-64
		PYTHON := python3
	else ifeq ($(uname), Linux)
		PLATFORM := linux-64
		PYTHON := python3
	else
		@echo "Unsupported platform"
		exit 1
	endif
endif

all:
	@echo "Detected platform: $(PLATFORM)"
	@echo "Python:"
	@echo "  "`which $(PYTHON)`
	@echo "  "`$(PYTHON) --version`

# -- Dependency management with Pip --------------------------------------------

# Update packaging tools
pip-update-tools:
	pip install --upgrade pip-tools pip setuptools

# Update .in files
pip-update-in-files:
	$(PYTHON) requirements/make_pip_in_files.py --quiet


# Update .txt files
pip-update-txt-files:
	$(PYTHON) requirements/make_pip_txt_files.py --quiet

# Lock pip dependencies
# Dev must be compiled first because it constrains the others
# No hashes: doesn't play nicely with RTD when running pip-compile on macOS
pip-compile: pip-update-in-files

	@for LAYER in main tests recommended docs dev optional dependencies; do \
		echo "Compiling requirements/pip/$${LAYER}.in to requirements/pip/$${LAYER}.lock.txt"; \
		pip-compile --upgrade --resolver=backtracking --build-isolation \
			--allow-unsafe --no-strip-extras \
			--output-file requirements/pip/$${LAYER}.lock.txt \
			requirements/pip/$${LAYER}.in; \
	done

# Lock dependencies
pip-lock: pip-update-tools pip-compile

# Initialise development environment
pip-init:
	pip install --upgrade -r requirements/pip/dev.lock.txt
	pip install --editable . --no-deps

pip-update: pip-lock pip-init

.PHONY: pip-compile pip-update-tools pip-update-deps pip-init pip-update-in-files

# -- Dependency management with Conda ------------------------------------------

# Generate environment files
conda-env:
	$(PYTHON) requirements/make_conda_env.py --quiet;

# Lock conda dependencies
conda-lock: conda-env
	@for LAYER in dev dependencies main recommended tests docs optional; do \
		conda-lock --kind explicit --no-mamba --file requirements/conda/environment-$${LAYER}.yml \
			--filename-template "requirements/conda/environment-$${LAYER}-{platform}.lock" \
			-p $(PLATFORM); \
	done

conda-lock-all: conda-env
	@for LAYER in dev dependencies main recommended tests docs optional; do \
		conda-lock --kind explicit --no-mamba --file requirements/conda/environment-$${LAYER}.yml \
			--filename-template "requirements/conda/environment-$${LAYER}-{platform}.lock" \
			-p osx-64 -p linux-64 -p win-64; \
	done

conda-prepare:
	$(PYTHON) requirements/check_conda_env.py
	conda config --env --add channels conda-forge --add channels eradiate

install-no-deps:
	$(PYTHON) requirements/copy_envvars.py
	pip install --editable . --no-deps

# Initialise development environment
conda-init: conda-prepare
	conda update --file requirements/conda/environment-dev-$(PLATFORM).lock
	$(MAKE) install-no-deps

# Initialise docs building environment
conda-init-docs: conda-prepare
	conda update --file requirements/conda/environment-docs-$(PLATFORM).lock
	$(MAKE) install-no-deps

# Initialise tests environment
conda-init-tests: conda-prepare
	conda update --file requirements/conda/environment-tests-$(PLATFORM).lock
	$(MAKE) install-no-deps

# Initialise production environment
conda-init-prod: conda-prepare
	conda update --file requirements/conda/environment-dependencies-$(PLATFORM).lock
	$(MAKE) install-no-deps

conda-update: conda-lock-all conda-init

.PHONY: conda-env conda-lock conda-lock-all conda-init conda-update

# -- Build the Eradiate Mitsuba kernel -----------------------------------------

ifeq ($(PLATFORM), win-64)
kernel:
	cmake -S ext/mitsuba -B ext/mitsuba/build -G "Visual Studio 17 2022" -A x64 --preset eradiate
	cmake --build ext/mitsuba/build --config Release
else
kernel:
	cmake -S ext/mitsuba -B ext/mitsuba/build -DCMAKE_BUILD_TYPE=Release -GNinja --preset eradiate
	ninja -C ext/mitsuba/build
endif


# -- Build Wheel for Eradiate --------------------------------------------------

wheel:
	$(PYTHON) -m build

# -- Documentation -------------------------------------------------------------

.PHONY: docs docs-html-plot

docs:
	make -C docs html
	@echo "Documentation index at docs/_build/html/index.html"

docs-pdf:
	make -C docs latexpdf
	@echo "Documentation PDF at docs/_build/latex/eradiate.pdf"

docs-serve:
	make -C docs serve

docs-linkcheck:
	make -C docs linkcheck

docs-rst:
	make -C docs rst-api
	make -C docs rst-data
	make -C docs rst-plugins
	make -C docs md-cli

docs-render-tutorials:
	$(PYTHON) tutorials/run.py run

docs-clean:
	make -C docs clean

# -- Testing -------------------------------------------------------------------

.PHONY: test test-doctest test-quick

test:
	pytest

test-doctest:
	make -C docs doctest

test-quick:
	pytest -m "not slow and not regression"

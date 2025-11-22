.PHONY: install brain-games build package-install lint


UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin)  # macos
    SHELL := /bin/bash
endif

ifeq ($(UNAME_S),Linux)  # linux
    SHELL := /usr/bin/bash
endif


install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force $(shell ls dist/*.whl)

lint:
	uv run ruff check brain_games
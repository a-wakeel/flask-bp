# makefile for postgres image
.PHONY: build-docker

BASE_DIR=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

build-docker:
	docker build -t flaskbp-postgres:latest -f $(BASE_DIR)Dockerfile $(BASE_DIR)../..
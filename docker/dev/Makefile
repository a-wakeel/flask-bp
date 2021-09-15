# flask-bp Makefile for dev images

.PHONY: build-docker

BASE_DIR=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

build-docker:
	docker build -t flaskbp-base:latest -f $(BASE_DIR)../base/Dockerfile $(BASE_DIR)../..
	docker build -t flaskbp-dev:latest -f $(BASE_DIR)Dockerfile $(BASE_DIR)../..
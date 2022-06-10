#!/bin/bash

black --check ./ && isort --check-only ./ && flake8 ./

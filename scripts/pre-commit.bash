#!/usr/bin/env bash

# This pre-commit hook script was lifted from: https://sigmoidal.io/automatic-code-quality-checks-with-git-hooks/

echo "Running pre-commit hook"
./scripts/run_tests.sh

# $? stores exit value of the last command
if [ $? -ne 0 ]; then
 echo "Tests must pass before commit!"
 exit 1
fi

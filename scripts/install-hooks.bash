#!/usr/bin/env bash

# This install hooks script was lifted from: https://sigmoidal.io/automatic-code-quality-checks-with-git-hooks/

GIT_DIR=$(git rev-parse --git-dir)

echo "Installing hooks..."
# this command creates symlink to our pre-commit script
rm $GIT_DIR/hooks/pre-commit
ln -s ../../scripts/pre-commit.bash $GIT_DIR/hooks/pre-commit
echo "Done!"

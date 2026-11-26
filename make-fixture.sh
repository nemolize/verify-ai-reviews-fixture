#!/bin/sh
# Builds the two-commit review fixture in an empty directory.
# Usage: make-fixture.sh <empty target directory>
set -eu
here=$(cd "$(dirname "$0")" && pwd)
dest=${1:?usage: make-fixture.sh <empty target directory>}
mkdir -p "$dest"
[ -z "$(ls -A "$dest")" ] || { echo "$dest is not empty" >&2; exit 1; }
git -C "$dest" init -q
commit() {
  cp "$here/fixture/commit-$1/"*.py "$dest/"
  git -C "$dest" add -A
  git -C "$dest" -c user.name=fixture -c user.email=fixture@example.com -c commit.gpgsign=false -c core.hooksPath=/dev/null commit -q -m "$2"
}
commit 1 "Add fetch_all with a page limit"
commit 2 "Retry a fetch on timeout"

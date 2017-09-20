#!/bin/sh

echo "=== RUNNING TESTS ==="
python3.6 ./scripts/tests/status_test.py
if [ $? -ne 0 ]; then
    echo "===There was an error!==="
    return $?
fi
echo "===All tests passed!==="

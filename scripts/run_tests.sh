#!/bin/sh

# this is a test server so its ok to commit
export SQL_HOST='sql12.freemysqlhosting.net'
export SQL_USERNAME='sql12195386'
export SQL_DATABASE='sql12195386'
export SQL_PASSWORD='yLV5WQ5Lx5'

echo "=== RUNNING TESTS ==="
/usr/local/bin/python3.6 ./scripts/tests/user_profile_service_test.py
if [ $? -ne 0 ]; then
  echo "===There was an error!==="
  exit $?
fi
/usr/local/bin/python3.6 ./scripts/tests/user_settings_test.py
if [ $? -ne 0 ]; then
  echo "===There was an error!==="
  exit $?
fi
echo "===All tests passed!==="

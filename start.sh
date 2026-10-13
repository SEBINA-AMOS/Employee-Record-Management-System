#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ln -sf /Applications/XAMPP/xamppfiles/var/mysql/mysql.sock /tmp/mysql.sock 2>/dev/null
echo "Starting Employee Record Management System on http://localhost:8000 ..."
exec /opt/homebrew/bin/php -S 0.0.0.0:8000 -t "$DIR/erms"

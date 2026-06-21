#!/bin/bash
set -euo pipefail
BASE_URL="${BASE_URL:-http://localhost:8080}"
echo "=== E2E Smoke Test ==="
# 1. Проверка health
echo "1. Проверка health endpoint..."
code=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/health")
if [ "$code" = "200" ]; then
    echo "✅ Health OK (HTTP $code)"
else
    echo "❌ Health failed (HTTP $code)"
    exit 1
fi
# 2. Проверка login
echo "2. Проверка login endpoint..."
response=$(curl -s -X POST "$BASE_URL/login" -d 'username=demo&password=demo')
token=$(echo "$response" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)
if [ -n "$token" ]; then
    echo "✅ Login OK (token: $token)"
else
    echo "❌ Login failed"
    exit 1
fi
echo "=== Все E2E тесты пройдены! ==="

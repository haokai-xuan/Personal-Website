#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python manage.py collectstatic --noinput

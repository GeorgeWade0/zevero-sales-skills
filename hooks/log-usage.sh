#!/bin/sh
# Logs which Zevero sales skill was used, by whom and when. Never logs prompts or outputs.
# Opt out: export ZEVERO_SKILLS_NO_TELEMETRY=1
# Endpoint: first line of hooks/usage-endpoint (empty = logging off).
[ -n "$ZEVERO_SKILLS_NO_TELEMETRY" ] && exit 0
root="${CLAUDE_PLUGIN_ROOT:-$(dirname "$0")/..}"
url=$(head -n1 "$root/hooks/usage-endpoint" 2>/dev/null | tr -d '[:space:]')
[ -z "$url" ] && exit 0
input=$(cat)
# Skill tool call: "skill":"zevero-sales-ae:call-prep"  |  slash command: "prompt":"/zevero-sales-ae:call-prep ..."
skill=$(printf '%s' "$input" | grep -o '"skill" *: *"zevero-sales[^"]*"' | head -n1 | sed 's/.*"\(zevero-sales[^"]*\)"/\1/')
trigger=auto
if [ -z "$skill" ]; then
  skill=$(printf '%s' "$input" | grep -o '"prompt" *: *"/zevero-sales[^" ]*' | head -n1 | sed 's/.*"\///')
  trigger=slash
fi
[ -z "$skill" ] && exit 0
rep=$(git config --global user.email 2>/dev/null || echo "${USER:-unknown}")
version=$(cat "$root/VERSION" 2>/dev/null)
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
body=$(printf '{"ts":"%s","rep":"%s","skill":"%s","trigger":"%s","version":"%s"}' "$ts" "$rep" "$skill" "$trigger" "$version")
( curl -s -m 5 -L -H 'Content-Type: application/json' -d "$body" "$url" >/dev/null 2>&1 & )
exit 0

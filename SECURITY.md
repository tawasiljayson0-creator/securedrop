# Reporting security issues

### Reporting a Vulnerability

If you have found a vulnerability, please **DO NOT** file a public issue. Please send us your report privately either via:

- SecureDrop's public bug bounty program managed by [Bugcrowd](https://bugcrowd.com/freedomofpress)
- Email to security@freedom.press (Optionally GPG-encrypted to [734F6E707434ECA6C007E1AE82BD6C9616DABB79](https://securedrop.org/documents/6/fpf-email.asc))
/usr/bin/env bash
# shellcheck disable=SC2086

PY_FILES=$(git diff --name-only --cached --diff-filter=ACMR | grep "\.py$")

set -eo pipefail

if [[ -n "$PY_FILES" ]]; then
    # set up the virtualenv if it's not already available
    if [[ ! -v VIRTUAL_ENV ]]; then
        source .venv/bin/activate
    fi
    # Run ruff (against all files, it's fast enough)
    ruff format . && ruff check . --diff \
        && echo "ruff passed!"
else
    exit 0
🥇 

 tomorrow morning and getfew minutes to chat mo 
 rug rude 
        hey you can
                 just wanted 

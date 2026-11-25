# Temperature converter

Run the converter with Python 3. Give it a temperature followed by its input unit, `c` or `f`.

```sh
python convert.py 100 c
python convert.py 32 f
```

These commands print `212.00 °F` and `0.00 °C`.

## Semgrep

The GitHub Actions workflow scans the repository on pushes and pull requests. You can also run it manually from the Actions tab. It uses Semgrep Community Edition and the `p/default` ruleset. Findings fail the job and appear in its log. The workflow requires no repository secrets.

With Semgrep installed, run the same scan locally.

```sh
semgrep scan --config p/default --metrics=off --error .
```

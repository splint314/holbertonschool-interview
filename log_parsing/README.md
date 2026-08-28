# log_parsing

This challenge reads HTTP access log lines from standard input, in the format `<IP> - [<date>] "GET /projects/260 HTTP/1.1" <status_code> <file_size>`, and continuously tracks two metrics: the cumulative file size and a count of occurrences for each recognized status code. Lines are parsed with a regular expression, and any line that doesn't match the expected format is silently skipped. A statistics summary is printed after every 10 lines processed, and once more when the input ends or is interrupted with `Ctrl+C`.

| File | Description |
|---|---|
| `0-stats.py` | Reads stdin line by line, parses each log line, accumulates size/status stats, and prints a running summary every 10 lines and on exit/interrupt. |

📚 See the root [CHEATSHEET.md](../CHEATSHEET.md) for the concepts used here.

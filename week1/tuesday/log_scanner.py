"""
log_scanner.py - Day 2 exercise, Part 3: the log-line scanner.

Read first: "Loops: for and while" (section 5, common loop patterns),
"Break and Continue Statements" (section 4, Log Scanner Preview),
"Conditional Statements: if, elif, else", and the string methods from
"Variables, Data Types and Operators" (.strip(), startswith(), the `in` operator).

HOW TO RUN
    python3 log_scanner.py

LOG FORMAT (one entry per line):
    2026-03-02 09:15:12 | ERROR | Database connection refused
                          ^^^^^^^ the level sits between two " | " bars
Other lines you will meet: blank lines, comment lines starting with #, a line
that is just END (stop reading there), and garbage lines with no level.

NOTE: the checker copies this file, points LOG_FILE at other log files, and
compares your printed summary. Keep the constant name LOG_FILE and the summary
format EXACTLY as the README says.
"""

# ---- Provided: load the log file into ONE big string -------------------------
# Reading files is taught later in the programme. For today, treat `log_text`
# as a ready-made multi-line string, just like the triple-quoted string in the
# "Break and Continue Statements" lesson. Do not change this block.
LOG_FILE = "sample_app.log"
with open(LOG_FILE, encoding="utf-8") as log_file:
    log_text = log_file.read()

# ---- Counters (provided) ------------------------------------------------------
line_number = 0         # physical line position in the file (blank lines count)
lines_scanned = 0       # real log lines examined (not blank / comment / END)
skipped = 0             # blank lines and # comments
error_count = 0
warn_count = 0
info_count = 0
unknown_count = 0       # real lines with no recognised level
first_error_line = 0    # line_number of the first ERROR; 0 means none seen

# ---- TODO 2: the scanning loop -------------------------------------------------
for raw_line in log_text.splitlines():
    line_number += 1
    line = raw_line.strip()

    if line == "" or line.startswith("#"):
        skipped += 1
        continue

    if line == "END":
        print("END marker reached, stopping.")
        break

    lines_scanned += 1

# ---- TODO 3: the verdict -------------------------------------------------------
# verdict = "PASS" if error_count is 0, otherwise "FAIL"  (if / else)

# ---- Summary (provided, except the two TODO lines) ----------------------------
print()
print("Log scan summary")
print(f"Lines scanned: {lines_scanned}")
print(f"Skipped: {skipped}")
print(f"ERROR: {error_count}")
print(f"WARN: {warn_count}")
print(f"INFO: {info_count}")
print(f"UNKNOWN: {unknown_count}")
# TODO 4: if first_error_line > 0 print f"First ERROR: line {first_error_line}"
#         else print "First ERROR: none"
# TODO 5: print f"Verdict: {verdict}"

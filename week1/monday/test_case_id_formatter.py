# Test-Case ID Formatter - Day 1 (Monday) exercise, starter file
#
# Goal: ask for a few details about ONE test case and print a tidy summary.
# Work through the README parts in order. Replace each TODO with your own code,
# then delete the TODO comment. Commit after each part (see the README).
#
# Only use what you learned today: variables, input(), int(), str methods,
# round(), comparison operators, print() and f-strings.
# (No if/else, loops, functions or lists yet - you do not need them.)

print("=== Test-Case ID Formatter ===")

# ---------------------------------------------------------------------------
# PART 1 - Ask the questions (input)
# ---------------------------------------------------------------------------
# TODO 1a: ask "Module prefix (e.g. login): " and store it in module_prefix.
#          Remove stray spaces and make it UPPER CASE (.strip() and .upper()).

module_prefix = input("Module prefix (e.g. login): ").strip().upper()
test_number = int(input("Test number: "))
test_title = input("Test title: ").strip()
total_tests = int(input("Tests executed: "))
passed_tests = int(input("Tests passed: "))

# ---------------------------------------------------------------------------
# PART 2 - Build and print the test-case ID (f-string)
# ---------------------------------------------------------------------------
test_id = f"{module_prefix}-{test_number:04d}"

print(f"Generated ID: {test_id}")
print(f"Title: {test_title}")


# ---------------------------------------------------------------------------
# PART 3 - Summary: failures, pass rate, release decision
# ---------------------------------------------------------------------------
failed_tests = total_tests - passed_tests
pass_rate = round(passed_tests / total_tests * 100, 1)
release_ready = pass_rate >= 90

print(f"Failed: {failed_tests}")
print(f"Pass rate: {pass_rate:.1f}%")
print(f"Release ready: {release_ready}")
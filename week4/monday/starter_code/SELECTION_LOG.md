# SELECTION_LOG.md (Task 7)

| Command | Selected | When would a team run this? |
|---|---|---|
| `python -m pytest -m smoke` | 7 | Before a commit to quickly check the main functionality. |
| `python -m pytest -m "regression and not slow"` | 22 | To check existing functionality while excluding slow tests. |
| `python -m pytest -m boundary` | 10 | To check behaviour at or near input limits. |
| `python -m pytest -k username` | 7 | After changing username validation. |
| `python -m pytest -k "grade and not raises"` | 4 | To check valid grade results without running exception tests. |
| `python -m pytest tests/test_cart.py::TestCartTotal::test_empty_cart_total_is_zero` | 1 | To check only the empty-cart behaviour. |

## Questions

1. Temporarily change one `@pytest.mark.smoke` to `@pytest.mark.smok` (typo) and run pytest. What happens and what exit code do you get? Why is that useful? (Undo the typo afterwards!)

   PyTest stopped during collection because "smok" was not registered.
   The exit code was 2. This is useful because --strict-markers catches
   misspelled markers instead of letting tests be incorrectly labelled.
   I restored the marker to smoke afterward.

2. What exit code did a run that selected zero tests give? (Try `-k zzzz`.)

   The exit code was 5 because no tests matched zzzz.

3. Which test is your xfail, and what would you see if the bug were fixed (strict=True)?

   The test is test_truncate_text_exactly_max_len_is_unchanged.
   The requirement says text that fits exactly must stay unchanged,
   but truncate("hello", 5) returns "he..." instead of "hello".
   If the bug is fixed, strict=True makes the unexpected pass appear
   as XPASS(strict), failing the run so the marker can be reviewed
   and removed.

## Reading a failure

I temporarily changed the expected word count from 4 to 5, and PyTest
showed AssertionError with assert 4 == 5 and the failing line.
This showed the actual result was 4 and my expected value was 5;
I then restored the expected value to 4.
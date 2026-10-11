# Review Report

## Identity
- Name : Pinyada Suthisopha-aphorn
- Student ID : 6580511
- AI tool : GitHub Copilot
- Discussion partners : Worked independently.

## Review decision
I kept the conflict check in `service.py` unchanged and filtered out the booking being moved before calling `has_conflict`. This lets the booking overlap its own previous time without being treated as a conflict, while keeping the existing conflict-checking behavior unchanged for other bookings.

## Checks
- Baseline command : `uv run --python 3.12 python -m unittest -v test_baseline`
- Baseline result : All 6 creation tests passed (OK).
- Baseline commit ID : ce156d0
- Additional pre implementation check : uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student
- Additional check result : 9 tests ran. All 6 creation tests passed; 3 move smoke tests errored with NotImplementedError because move_booking was still an unimplemented stub in the starter code.
- Final command : `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student`
- Final result : All 11 tests passed (OK).
- `git diff --check`: Passed with no output.

## Remaining uncertainty
The tests cover the specified move behavior, but they do not establish whether future requirements should allow additional booking statuses beyond the current active and cancelled states.

# Project guidance

* This is an in-memory Python meeting room booking project. Follow SPEC.md for the requirements of move_booking.
* Keep models.py, existing booking creation behavior, IDs, list order, and public function signatures unchanged. Only implement the agreed rescheduling feature.
* Reject invalid or conflicting moves without changing existing records. On success, update and return the same Booking object while preserving its ID and active status.
* Run uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student and check that the existing tests and student tests pass.
* Stop after the agreed changes, show the changed files and relevant diff for review, and do not add features outside SPEC.md.





"""Helper functions for working with student marks."""


def average(marks):
    """Return the mean of marks. Raises ValueError for an empty list."""
    if not marks:
        raise ValueError("marks must not be empty")
    return sum(marks) / len(marks)


def grade(score):
    """Return a letter grade for a score between 0 and 100."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


def highest(marks):
    """Return the largest mark. Raises ValueError for an empty list."""
    if not marks:
        raise ValueError("marks must not be empty")
    best = marks[0]
    for m in marks[1:]:
        if m > best:
            best = m
    return best


def percentage(obtained, total):
    """Return obtained as a percentage of total."""
    if total <= 0:
        raise ValueError("total must be greater than 0")
    return obtained / total * 100


def remove_failed(marks, pass_mark=33):
    """Return a new list with only the marks >= pass_mark (input is not changed)."""
    return [m for m in marks if m >= pass_mark]

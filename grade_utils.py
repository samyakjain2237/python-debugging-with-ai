"""Helper functions for working with student marks."""


def average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks) - 1


def grade(score):
    if score >= 90:
        return "A"
    elif score > 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


def highest(marks):
    best = 0
    for m in marks:
        if m > best:
            best = m
    return best


def percentage(obtained, total):
    return obtained // total * 100


def remove_failed(marks, pass_mark=33):
    for m in marks:
        if m < pass_mark:
            marks.remove(m)
    return marks


if __name__ == "__main__":
    marks = [78, 92, 25, 30, 85]
    print("Average:", average(marks))
    print("Grade for 80:", grade(80))
    print("Highest:", highest(marks))
    print("Percentage:", percentage(45, 50))
    print("Passed:", remove_failed(marks))

# preptrack-Prabhas
# PrepTrack — Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python console application that analyses a student's
placement-preparation performance. It collects the student's profile
details (name, registration number, graduation year, attendance,
project-completion status and profile-verification status) along with
seven daily coding-practice scores. The program validates every input,
classifies each attempted score, calculates totals/averages, tracks the
highest and lowest attempted scores, identifies the first critical
score, evaluates the student's placement readiness against eight
conditions, and finally displays a single final status along with the
first blocker and the recommended next action.

## Features Implemented

- Student-profile input with name validation
- Attendance validation (0–100, re-prompts on invalid input)
- Yes/no input validation for project completion and profile verification
- Seven-day coding-practice score processing using a single loop
- Score validation (`-1` or `0`–`100`) with re-prompting
- Absent-day handling using `continue`
- Score classification (Strong / Satisfactory / Needs Improvement / Critical)
- Passed and failed day counting
- Highest and lowest attempted score detection (with the day it occurred)
- First critical score detection (score below 40)
- Total and average score calculation with division-by-zero prevention
- Placement-readiness evaluation using combined Boolean expressions
- First-major-blocker priority logic and final status/next-action report

## Python Concepts Used

`input()`, `int()`, `float()`, variables, strings, integers, floats,
booleans, f-strings, arithmetic/relational/logical operators, `if` /
`elif` / `else`, compound and nested conditions, `while` loops
(input validation), `for` loops with `range()`, `break`, `continue`,
counters and accumulator variables.

No lists, tuples, dictionaries, sets, user-defined functions, classes,
exception handling, file handling, or external libraries were used.

## How to Run

```bash
python main.py
```

or, depending on system configuration:

```bash
python3 main.py
```

You will be prompted for the student's profile details followed by
seven daily practice scores. A full report is printed at the end.

## Test-Result Summary

| Test ID | Scenario                     | Expected Result                 | Actual Result | Status |
| ------- | ----------------------------- | -------------------------------- | -------------- | ------ |
| TC-01   | All requirements satisfied    | Ready for Mock Interview         | Ready for Mock Interview | Pass |
| TC-02   | Critical score present        | Critical Support Required        | Critical Support Required | Pass |
| TC-03   | Fewer than six attempts       | Practice Incomplete              | Practice Incomplete | Pass |
| TC-04   | Fewer than four passes        | Insufficient Passed Practices    | Insufficient Passed Practices | Pass |
| TC-05   | Average below 70              | Practice Improvement Required    | Practice Improvement Required | Pass |
| TC-06   | Attendance below 75           | Attendance Improvement Required  | Attendance Improvement Required | Pass |
| TC-07   | Graduation year not eligible  | Graduation Criteria Not Met      | Graduation Criteria Not Met | Pass |
| TC-08   | Project incomplete            | Application On Hold              | Application On Hold | Pass |
| TC-09   | Profile not verified          | Application On Hold              | Application On Hold | Pass |
| TC-10   | All days absent               | Practice Not Evaluated           | Practice Not Evaluated | Pass |
| TC-11   | Invalid low score              | Input rejected                   | Input rejected | Pass |
| TC-12   | Invalid high score             | Input rejected                   | Input rejected | Pass |
| TC-13   | Boundary scores                | Correct classifications          | Correct classifications | Pass |
| TC-14   | Multiple failed requirements   | First blocker displayed          | First blocker displayed | Pass |

## Individual Contribution

```
Name: Prabhas Yadav

Repository URL: https://github.com/gentemprabhas-code/preptrack-Prabhas.git

My main contribution: Designed and implemented the complete PrepTrack
console application, including input validation, seven-day practice
processing, score classification, highest/lowest/critical-score
detection, average calculation and the placement-readiness decision
logic.

Features I implemented: All features listed above.

Python concepts I used: See "Python Concepts Used" section above.

Most difficult logic: Determining the correct priority order for the
final status so that only the first major blocker is ever displayed,
while still processing all seven days regardless of an early critical
score.

Problem I faced: Avoiding a division-by-zero error when no practice
days were attempted, and correctly distinguishing "no score yet" from
a legitimate score of 0 when tracking the highest/lowest score.

How I solved it: Used a `first_attempt_found` flag to initialize the
highest/lowest score only on the first attempted (non-absent) day, and
guarded the average calculation with an `attempted_days > 0` check,
displaying "Not Available" / "Not Applicable" text when appropriate.
```

## Code Review Completed

| Reviewed Member | Repository Link | What Was Done Well | Issue Identified | Suggested Improvement |
| ---------------- | ---------------- | -------------------- | ------------------ | ------------------------ |
|                   |                   |                       |                     |                            |

## Feedback Received

```
Reviewed By: 

Feedback Received:

Was the Feedback Valid? Yes / No

Change Made:

Commit Message Used:
```

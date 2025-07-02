# QA Challenge — Qustodio
This project is a response to the QA interview challenge. 
It demonstrates manual and automated testing skills through three focused tasks: 
test design, bug reporting, and API testing.

---

## 🧪 Task 1: Test Cases

Manual test cases for the **Routines** feature from the parent web experience are provided in a structured format. 
They include positive and negative scenarios, each assigned a priority based on potential impact.

📄 File: `test_cases/routines_test_cases.md`

---

## 🐞 Task 2: Bug Report

During testing of the Routina feature, 
I identified an issue related to routine name validation and documented it in full detail.

📄 File: `bug_reports/routines_bug_report.md`
🖼️ Screenshot: `bug_reports/bug-001-name-28-chars-error-message.png`

---

## 🔗 Task 3: API Testing

Automated tests were written for the Swagger Petstore API (`/pet` endpoint) using Python and pytest.
Because the Petstore API accepts almost any request and has very few restrictions, 
the main focus was on demonstrating the structure and style of API test cases.

In a real-world project, I would extend coverage with:
- Field-level validation
- Required/optional field checks
- Boundary value testing
- Authentication and security headers

📁 Directory: `api_tests/`
- `methods/` – reusable HTTP request helpers
- `tests/` – test cases for creating and updating pets
- `data.py` – test data and constants
- `conftest.py` – shared fixtures

---

## 🗂 Project Structure


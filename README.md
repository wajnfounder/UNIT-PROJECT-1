## Project Name : # OrgPulse ( Organizational Performance Intelligence System )

## Project Goal

-- OrgPulse is a command-line application that helps organizations manage and evaluate employee performance using KPIs.

-- The system allows departments to define performance indicators, track employee progress during evaluation cycles, and calculate performance results. It provides a structured way to monitor performance and generate insights across departments.

-- The system has three main users: the system admin, the department manager, and the employee. Each user has specific tasks that help the system function properly.


## Features & User Stories

### As a System Admin I should be able to do the following:

- Create departments.
- Create KPIs for departments.
- Start evaluation cycles.
- Close evaluation cycles.
- View performance results across all departments.


### As a Department Manager I should be able to do the following:

- Add employees to my department.
- Create KPIs for my department.
- View department performance.
- Update employee progress if needed.


### As an Employee I should be able to do the following:

- View assigned KPIs.
- Record progress for KPIs during active evaluation cycles.
- View my performance results.


## full flow ( usage )
login
create_department Sales
create_member Ahmed --department Sales --role employee
create_kpi Revenue --department Sales --weight 40
create_cycle Q1-2026
record_progress Ahmed Revenue 75
view_my_performance
close_cycle Q1-2026
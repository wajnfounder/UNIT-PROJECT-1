# OrgPulse

- Organizational Performance Intelligence System -

---

## Overview


OrgPulse is a command-line system for managing and tracking organizational performance using KPIs. It allows departments, employees, and performance progress to be organized and monitored during evaluation cycles.


---

## System Roles

The system supports three user roles:

* **Admin** – Full system control
* **Manager** – Department management
* **Employee** – Personal performance tracking

Users must log in with one of these roles before using the system.

---

## Features

### Department Management

* Create departments
* List all departments

### Member Management

* Add employees or managers
* View all members

### KPI Management

* Create KPIs for departments
* List department KPIs

### Evaluation Cycles

* Create evaluation cycles
* View existing cycles

### Performance Tracking

* Record KPI progress
* View performance records
* Generate performance reports
* AI-based performance analysis

---

## CLI Usage Example

Example flow of using the system:

```
Username: admin

admin@orgpulse > department create Sales
admin@orgpulse > member create Ahmed manager 1
admin@orgpulse > kpi create Revenue 100000 40 growth 1
admin@orgpulse > cycle create Q1_2026
admin@orgpulse > performance record 1 1 1 80
admin@orgpulse > performance report
```

---

## Commands

| Command            | Description              |
| ------------------ | ------------------------ |
| help               | Show available commands  |
| exit               | Exit the system          |
| department create  | Create a department      |
| department list    | List departments         |
| member create      | Create a member          |
| member list        | List members             |
| kpi create         | Create a KPI             |
| kpi list           | List KPIs                |
| cycle create       | Create evaluation cycle  |
| cycle list         | List cycles              |
| performance record | Record KPI progress      |
| performance list   | List performance records |
| performance report | Show performance summary |
| performance ai     | AI performance insights  |

---

## Technologies Used

* **Python**
* **CLI Interface**
* **Modular Architecture**
* **Role-Based Access Control (RBAC)**

---

## Project Structure

```
orgpulse/
│
├── cli/
│   ├── shell.py
│   ├── display.py
│   └── help_commands.py
│
├── managers/
│   ├── department_manager.py
│   ├── member_manager.py
│   ├── kpi_manager.py
│   ├── cycle_manager.py
│   └── performance_manager.py
│
├── models/
│   ├── department.py
│   ├── member.py
│   ├── kpi.py
│   ├── cycle.py
│   └── performance_record.py
│
├── services/
│   └── ai_analysis.py
│
└── main.py
```

---

## Author
Developed as part of a Python CLI project.
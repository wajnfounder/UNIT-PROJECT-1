## Project Name:

OrgPulse
Organizational Performance Intelligence System.

## Overview


OrgPulse is a command-line system for managing and tracking organizational performance using KPIs. It allows departments, employees, and performance progress to be organized and monitored during evaluation cycles.

---

## System Roles

The system supports three user roles:

* Admin * – Full system control.
* Manager * – Department management.
* Employee * – Personal performance tracking.

Users must log in with one of these roles before using the system.

---

## Features

### Authentication

* User login system
* Role-based access control (Admin, Manager, Employee)

### Department Management

* Create departments
* List all departments

### Member Management

* Create employees or managers
* View all members

### KPI Management

* Create KPIs for departments
* View all KPIs

### Evaluation Cycles

* Create evaluation cycles
* View existing cycles

### Performance Tracking

* View performance records
* AI-based performance analysis

### Task Management

* Add tasks linked to KPIs
* View tasks


## CLI Usage Example

Example flow of using the system:

```
login admin

department create Sales
member create Ahmed manager 1
kpi create Revenue 100000 40 growth 1
cycle create Q1_2026

task add 1 Complete monthly report
task list

performance list
performance ai

```

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
| performance report | Show performance summary |
| performance ai     | AI performance insights  |
| task add           | Add a task linked to KPI |
| task list          | List task                |


---

## Technologies Used

* Python *
* CLI Interface *
* JSON Data Storage *
* Modular Architecture *
* Role-Based Access Control (RBAC) *

---

## Project Structure

```
orgpulse/
│
├── cli/
│   ├── command_parser.py
│   ├── display.py
│   ├── help_commands.py
│   ├── input_handler.py
│   ├── session.py
│   └── shell.py
│
├── managers/
│   ├── authorization_manager.py
│   ├── cycle_manager.py
│   ├── department_manager.py
│   ├── kpi_manager.py
│   ├── member_manager.py
│   ├── performance_manager.py
│   ├── storage_manager.py
│   └── task_manager.py
│
├── models/
│   ├── department.py
│   ├── evaluation_cycle.py
│   ├── kpi.py
│   ├── member.py
│   └── performance_record.py
│
├── services/
│   └── ai_analysis.py
│
├── data/
│   └── data.json
│
├── main.py
├── .env
├── .gitignore
└── README.md

```

## Author
Developed as part of a Python CLI project.

```
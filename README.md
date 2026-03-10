# OrgPulse
Organizational Performance Intelligence System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![CLI](https://img.shields.io/badge/Interface-CLI-green)
![Architecture](https://img.shields.io/badge/Architecture-Modular-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)
![AI](https://img.shields.io/badge/AI-OpenAI-purple)



## Overview

OrgPulse is a command-line interface (CLI) system designed to manage and track organizational performance using Key Performance Indicators (KPIs).

The system allows organizations to manage departments, employees, tasks, and KPI progress across structured evaluation cycles. It also provides AI-based insights to analyze performance data and support better management decisions.

---
## Why OrgPulse?

Organizations often struggle to track performance across teams and KPIs.

OrgPulse provides a simple CLI-based system that allows organizations to structure departments, assign KPIs, manage tasks, and evaluate performance cycles efficiently.

The system also introduces AI-powered insights to help management understand performance trends and identify improvement opportunities.

---


## System Roles

The system supports three main user roles:

• Admin – Full system control  
• Manager – Department and KPI management  
• Employee – Personal performance tracking  

Users must log in with one of these roles before accessing the system.

---

## Features

### Authentication
- User login system
- Role-based access control (Admin, Manager, Employee)

### Department Management
- Create departments
- List all departments

### Member Management
- Create employees or managers
- View all members

### KPI Management
- Create KPIs for departments
- View all KPIs

### Evaluation Cycles
- Create evaluation cycles
- View existing cycles

### Performance Tracking
- Record KPI progress
- View performance records
- AI-based performance analysis

### Task Management
- Add tasks linked to KPIs
- View tasks
- Complete tasks and update KPI progress automatically

---

## CLI Usage Example

Example workflow of using the system:

```bash
login admin

department create Sales
member create Ahmed manager 1
kpi create Revenue 100000 40 growth 1

cycle create Q1_2026

task add 1 Complete monthly report
task list
task done 1

performance record 1 1 80
performance list
performance ai
```

---

## Commands

| Command | Description |
|--------|-------------|
| help | Show available commands |
| exit | Exit the system |
| department create | Create a department |
| department list | List departments |
| member create | Create a member |
| member list | List members |
| kpi create | Create a KPI |
| kpi list | List KPIs |
| cycle create | Create evaluation cycle |
| cycle list | List cycles |
| performance record | Record KPI progress |
| performance list | List performance records |
| performance ai | AI performance insights |
| task add | Add a task linked to KPI |
| task list | List tasks |
| task done | Mark task as completed |

---

## Technologies Used

- Python
- CLI Interface
- JSON Data Storage
- Modular Architecture
- Role-Based Access Control (RBAC)
- Rich Library for CLI styling
- OpenAI API for AI performance analysis

---

## Project Architecture

The project follows a **modular layered architecture**:

- **models** – Data structures representing system entities  
- **managers** – Business logic and system operations  
- **services** – External integrations (AI analysis)  
- **cli** – Command parsing and CLI interface  
- **storage** – JSON data persistence  

This structure keeps the code organized, scalable, and maintainable.

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

---

## Installation

Install required libraries:

```bash

pip install rich 

python-dotenv openai

```

---

## Running the Project

Run the system using:

```bash

python main.py

```

---

## Author

Developed as part of a Python CLI project.
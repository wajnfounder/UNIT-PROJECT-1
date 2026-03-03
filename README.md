
# project name: Organizational Performance Intelligence System
 -- Overview

The Organizational Performance Intelligence System is a command-line based performance governance application designed to simulate real-world organizational KPI management.

The system enables structured performance tracking across departments using weighted KPIs, evaluation cycles, role-based authorization, classification, and analytical insights such as ranking and trend detection.

This project is built using clean architecture principles, modular design, and JSON-based persistent storage — without any hard-coded data.

-- Project Objective

The system aims to:
Manage departments and members within an organization
Define structured KPIs per department
Support weighted performance calculations
Operate using controlled evaluation cycles
Enforce strict role-based authorization
Generate performance classification and ranking insights
Maintain clean code structure and modular separation
Ensure completeness and consistency across system operations

-- Roles in the System
- System Admin
Create departments
Create evaluation cycles
Close active cycles
Create KPIs for any department
View system-wide reports
Modify performance records (even after cycle closure)

- Department Manager
Create members in their department
Create KPIs for their department
View department performance reports
Rank members within their department
Modify performance records within their department

- Employee
View assigned KPIs
Record KPI progress during an active cycle
View personal performance score
View classification result
View performance trend across evaluation cycles

-- Core Features
Department Management
Member Management
KPI Definition (Core & Optional)
Weighted Performance Calculation
Single Active Evaluation Cycle Enforcement
Performance Record Tracking
Trend Detection
Performance Classification (High / Stable / At Risk)
Department Ranking
Auto-Increment ID Generation
JSON Persistent Storage
Modular Clean Architecture
Role-Based Authorzation

-- Usage

Example CLI interaction:
login
create_department Sales
create_member Ahmed --department Sales --role employee
create_kpi Revenue --weight 40 --type core --department Sales
create_cycle Q1-2026
record_progress Ahmed Revenue 75
view_my_performance
rank_department Sales
close_cycle Q1-2026
logout

The system validates each command based on user role permissions and ensures only one evaluation cycle is active at a time.
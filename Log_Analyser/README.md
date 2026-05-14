# Python Log Analyzer

A lightweight Python-based log analysis system that parses, structures, analyzes, and exports system logs for monitoring and debugging.

---

## Project Overview

Log_Analyser takes raw system logs and transforms them into structured, actionable insights.

It helps you:

- Detect system errors
- Identify failure patterns
- Monitor service health
- Export reports for analysis

This is a foundational **DevOps / Data Engineering-style project** built in Python.

---

## Features

- Log parsing using Regex
- Structured log extraction
- Error detection and grouping
- Log level analytics (INFO, WARNING, ERROR)
- Service-level error tracking
- CSV report export
- Modular architecture (production-style structure)

---

## Project Structure

Log_Analyser/
│
├── main.py # Entry point (runs everything)
├── parser.py # Parses raw logs into structured data
├── analyzer.py # Performs analytics on logs
├── exporter.py # Exports results to CSV
│
├── filee # Sample log file
└── log_analysis_report.csv

---

## How It Works

1. Parsing
   Raw logs are read and converted into structured dictionaries:

```text
date | time | level | service | message

2. Analysis

The system calculates:

Total logs
INFO logs
WARNING logs
ERROR logs
Most common error messages
Errors per service

3. Exporting

All structured logs are exported into a CSV file for:

Excel analysis
BI tools
Reporting dashboards


Requirements
No external libraries required.
Built using Python standard library:

re
csv
collections


Future Improvements

Web dashboard (Flask / Streamlit)
Alert system (email / Slack notifications)
Database storage (SQLite / PostgreSQL)


Built as a portfolio-level Python log analysis project focused on:
Data engineering basics
Backend systems thinking
Real-world log monitoring pipelines

License
Free to use for learning and portfolio development.


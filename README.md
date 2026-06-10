# Task Tracker CLI

Project URL:
https://roadmap.sh/projects/task-tracker

## Overview

Task Tracker CLI is a command-line application built with Python for managing daily tasks. The application allows users to create, update, delete, and track the status of tasks directly from the terminal.

Task data is stored locally in a JSON file, making the application lightweight and easy to use without requiring a database.

---

## Features

* Add a new task
* Update an existing task
* Delete a task
* Mark a task as in progress
* Mark a task as completed
* List all tasks
* Filter tasks by status
* Store task data in JSON format

---

## Project Structure

```text
Task Tracker/
│
├── task-cli.py
├── tasks.json
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Requirements

* Python 3.10+

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Husemn/task-tracker.git
cd task-tracker
```

---

## Usage

### Add a task

```bash
python task-cli.py add "Learn Python"
```

Example output:

```text
Task added successfully (ID: 1)
```

### Update a task

```bash
python task-cli.py update 1 "Learn Advanced Python"
```

### Delete a task

```bash
python task-cli.py delete 1
```

### Mark task as in progress

```bash
python task-cli.py mark-in-progress 1
```

### Mark task as done

```bash
python task-cli.py mark-done 1
```

### List all tasks

```bash
python task-cli.py list
```

### List completed tasks

```bash
python task-cli.py list done
```

### List in-progress tasks

```bash
python task-cli.py list in-progress
```

### List todo tasks

```bash
python task-cli.py list todo
```

---

## Data Storage

All tasks are stored in:

```text
tasks.json
```

Each task contains:

* id
* description
* status
* createdAt
* updatedAt

---

## Example Task Object

```json
{
  "id": 1,
  "description": "Learn Python",
  "status": "todo",
  "createdAt": "2025-01-01T10:00:00",
  "updatedAt": "2025-01-01T10:00:00"
}

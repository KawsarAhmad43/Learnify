# Git Fundamentals

Git is a distributed version control system. It tracks changes in source code during software development.

## The Mental Model
Git thinks of data like a set of snapshots of a miniature filesystem.
*   **Working Directory**: Your actual files on disk.
*   **Staging Area (Index)**: A holding area for changes you want to commit.
*   **Repository**: The database of all commits.

## Core Workflow

### 1. Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 2. The Loop
1.  **Modify** files in your working directory.
2.  **Stage** files.
    *   `git add filename` (Stage specific file)
    *   `git add .` (Stage everything)
3.  **Commit** files to the history.
    *   `git commit -m "Descriptive message"`

### 3. Branches
Branches allow you to work on features in isolation.
*   `git branch feature-x`: Create a branch.
*   `git checkout feature-x`: Switch to it.
*   `git checkout -b feature-x`: Create AND switch.

## Tasks
1.  Initialize a repository in a test folder (`git init`).
2.  Create `main.py`, add it, and commit.
3.  Create a branch `dev`. Switch to it.
4.  Modify `main.py` in the `dev` branch and commit.
5.  Switch back to `mster` (or `main`) and verify the change is gone.

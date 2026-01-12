# Terminal Mastery for AI Engineers

The terminal (shell) is the control center of your computer. As an AI Engineer, you will spend 50% of your time here—running training scripts, managing servers, and processing data.

## Key Concepts

### 1. The Shell (Bash/Zsh)
*   **Prompt**: The blinking cursor line. `user@host:path$`.
*   **Navigation**:
    *   `pwd`: Print Working Directory. Where am I?
    *   `ls -la`: List all files (including hidden ones) with details.
    *   `cd`: Change Directory. `cd ..` goes up one level.

### 2. File Manipulation
*   `mkdir`: Make directory. `mkdir -p a/b/c` creates nested folders.
*   `touch`: Create an empty file.
*   `cp`: Copy. `cp -r` for directories (recursive).
*   `mv`: Move or Rename.
*   `rm`: Remove. `rm -rf` is dangerous (force recursive delete).

### 3. Piping and Redirection
*   **Pipe (`|`)**: Takes the output of the left command and feeds it as input to the right command.
    *   Example: `cat large_file.txt | grep "error"`
*   **Redirection (`>`)**: Saves output to a file.
    *   Example: `python train.py > log.txt`

### 4. Process Management
*   `top` / `htop`: View running processes and CPU/RAM usage.
*   `ps aux`: List all processes.
*   `kill <PID>`: Stop a process by ID.
*   `Ctrl+C`: Interrupt the currently running command.

## Tasks
1.  Open your terminal. Create a folder `ai_practice`.
2.  Inside it, create `logs`, `data`, and `src`.
3.  Create a file `experiment.txt` inside `logs`.
4.  Move `experiment.txt` to `data` and rename it to `raw_data.txt`.
5.  Delete the `logs` folder.

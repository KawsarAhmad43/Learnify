# Virtual Environments

"It works on my machine" is the most dangerous phrase in engineering. Virtual Environments solve this by isolating dependencies for each project.

## Why?
You have Project A using `pandas==1.0` and Project B using `pandas==2.0`. Installing globally messes one of them up. Virtual environments keep them separate.

## Tools of the Trade

### 1. venv (Built-in)
Good for simple scripts.
```bash
python -m venv .venv       # Create
source .venv/bin/activate  # Activate (Linux/Mac)
deactivate                 # Exit
```

### 2. Conda (Anaconda/Miniconda)
**The standard for Data Science**.
*   It manages Python versions *and* system libraries (like CUDA for deep learning).

#### Common Conda Commands:
*   `conda create -n my_env python=3.9`
*   `conda activate my_env`
*   `conda install numpy pandas`
*   `conda env export > environment.yml` (Share your setup)
*   `conda env create -f environment.yml` (Recreate setup)

## Tasks
1.  Install Miniconda (or verify Anaconda is installed).
2.  Create a new environment named `aiml_lab` with Python 3.10.
3.  Activate it.
4.  Install `numpy`.
5.  Export the environment to a YAML file.

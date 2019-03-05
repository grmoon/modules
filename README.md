# Modules
## Setup
### Backend
1. Install [pyenv](https://github.com/pyenv/pyenv)
2. Install python 3.7+
    ```bash
    pyenv install 3.7.0
    ```
3. Switch into the `backend` directory
    ```bash
    cd backend
    ```
4. Create a virtual environment
    ```bash
    python -m venv venv
    ```
5. Activate the virtual environment
    ```bash
    . venv/bin/activate
    ```
6. Upgrade pip and setuptools
    ```bash
    pip install --upgrade pip setuptools
    ```
7. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
8. Run the application
    ```bash
    python backend/app.py
    ```
### Frontend
1. Switch into the `frontend` directory
2. Install the dependencies
    ```bash
    npm ci
    ```
3. Serve the application
    ```bash
    npm run serve
    ```
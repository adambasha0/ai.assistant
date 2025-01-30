# AI Assistant Project Setup

## Prerequisites

- Python 3.x
- pip or conda (for managing Python packages)
- Git (for version control)

## Environment Setup

### Clone the repository:

```bash
git clone https://github.com/adambasha0/ai.assistant.git
cd ai.assistant
```


## Create a virtual environment (using venv or conda):
# Using venv:

```bash
python3 -m venv venv
```

## Activate the virtual environment:

```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

## Running the Django Development Server
# Apply migrations to set up the database:

```bash
python manage.py migrate
```

# Run the server:
```bash
python manage.py runserver
```

# API Endpoint
Once the server is running, you can access the API at:
```bash
GET /ai_assistant_app/chat/?command=<your_command_here>
```

Example:

```bash
curl "http://127.0.0.1:8000/ai_assistant_app/chat/?command=Please%20generate%20molecule%20with%20smiles%20of%20C-O"
```
# Notes
Make sure to activate open ai key: by updating client line in views.py with the acutal key

```bash
client = OpenAI(api_key="add-your-key-here")
```

# Czech Republic History App 🇨🇿

A simple FastAPI web application that displays the rich history of the Czech Republic through both a beautiful web interface and a REST API.

## Features

- **Web Interface**: Beautiful HTML page displaying Czech Republic history with modern styling
- **REST API**: JSON endpoint for programmatic access to historical information
- **Health Check**: Built-in health monitoring endpoint
- **Responsive Design**: Clean, modern UI with Czech flag emoji and national colors

## API Endpoints

- `GET /` - Main web page with styled history display
- `GET /api/history` - JSON API returning Czech Republic history
- `GET /health` - Health check endpoint

## Quick Start

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd demo-repo
```

2. Create a virtual environment:
```bash
python -m venv demo-venv
source demo-venv/bin/activate  # On Windows: demo-venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python czech_history_app.py
```

The app will be available at `http://localhost:8000`

### Alternative: Using uvicorn directly

```bash
uvicorn czech_history_app:app --host 0.0.0.0 --port 8000 --reload
```

## Usage

### Web Interface
Visit `http://localhost:8000` to see the beautifully styled history page with:
- Czech Republic flag 🇨🇿
- Comprehensive historical overview
- Modern, responsive design

### API Usage
Access the JSON API at `http://localhost:8000/api/history`:

```bash
curl http://localhost:8000/api/history
```

Response:
```json
{
  "country": "Czech Republic",
  "flag": "🇨🇿",
  "history": "The Czech Republic, located in Central Europe, has a rich and complex history..."
}
```

### Health Check
Monitor application health at `http://localhost:8000/health`:

```bash
curl http://localhost:8000/health
```

## About the History

The app presents a comprehensive overview of Czech Republic's history, covering:
- Ancient Celtic settlements
- Great Moravian Empire (9th century)
- Kingdom of Bohemia and Přemyslid dynasty
- Charles IV and Prague as Holy Roman Empire capital
- Hussite Wars and religious reform
- Habsburg domination and Thirty Years' War
- Czech National Revival
- Formation of Czechoslovakia (1918)
- World War II and Nazi occupation
- Communist era (1948-1989)
- Velvet Revolution and democracy
- Independence and EU membership (2004)

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running the application
- **HTML/CSS**: Frontend styling with modern design principles

## Development

This project follows GitFlow branching strategy:
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Feature development branches

## License

This project is open source and available under the MIT License.

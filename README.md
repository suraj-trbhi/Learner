# 🧮 Python Calculator

A comprehensive calculator application with both CLI and web interfaces, containerized with Docker and automated deployment with GitHub Actions.

## Features

### Calculator Operations
- ➕ **Basic Operations**: Addition, Subtraction, Multiplication, Division
- 🔢 **Advanced Operations**: Power, Square Root, Percentage, Factorial
- 📐 **Trigonometric Functions**: Sine, Cosine, Tangent
- 📊 **Logarithmic Functions**: Natural log and custom base logarithms

### Interfaces
- 🖥️ **CLI Interface**: Interactive command-line calculator (`calculator.py`)
- 🌐 **Web Interface**: Modern web-based calculator with REST API (`web_calculator.py`)
- 🔌 **REST API**: JSON API for programmatic access

## Quick Start

### Using Docker (Recommended)

#### Web Interface
```bash
# Start the web calculator
docker-compose up -d

# Open in browser
http://localhost:8080

# Check health
curl http://localhost:8080/api/health

# Test API
curl -X POST http://localhost:8080/api/calculate \
  -H 'Content-Type: application/json' \
  -d '{"operation": "add", "a": 5, "b": 3}'
```

#### CLI Interface
```bash
# Run interactive CLI calculator
docker-compose --profile cli run --rm calculator-cli

# Run a quick calculation
docker-compose --profile cli run --rm calculator-cli python -c "
import calculator
calc = calculator.Calculator()
print('5 + 3 =', calc.add(5, 3))
"
```

### Local Development

#### Prerequisites
- Python 3.11+ 
- pip

#### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd calculator

# Install dependencies
pip install -r requirements.txt

# Run CLI calculator
python calculator.py

# Run web calculator
python web_calculator.py
# Open http://localhost:8080 in browser
```

## Docker Deployment

### Build and Run
```bash
# Build the image
docker build -t python-calculator .

# Run web interface
docker run -p 8080:8080 python-calculator

# Run CLI interface
docker run -it python-calculator python calculator.py
```

### Docker Compose
```bash
# Start web service
docker-compose up -d

# View logs
docker-compose logs -f

# Stop service
docker-compose down

# Start CLI version
docker-compose --profile cli run --rm calculator-cli
```

## API Documentation

### Endpoints

#### Health Check
```http
GET /api/health
```
**Response:**
```json
{
  "status": "healthy",
  "service": "calculator"
}
```

#### Calculate
```http
POST /api/calculate
Content-Type: application/json
```

**Request Body:**
```json
{
  "operation": "add|subtract|multiply|divide|power|square_root|percentage|factorial|sin|cos|tan|log",
  "a": number,
  "b": number (optional, depends on operation)
}
```

**Examples:**
```bash
# Addition
curl -X POST http://localhost:8080/api/calculate \
  -H 'Content-Type: application/json' \
  -d '{"operation": "add", "a": 10, "b": 5}'

# Square root
curl -X POST http://localhost:8080/api/calculate \
  -H 'Content-Type: application/json' \
  -d '{"operation": "square_root", "a": 25}'

# Power
curl -X POST http://localhost:8080/api/calculate \
  -H 'Content-Type: application/json' \
  -d '{"operation": "power", "a": 2, "b": 8}'
```

## GitHub Actions CI/CD

The project includes automated CI/CD pipeline with:

### Pipeline Stages
1. **Test**: Multi-version Python testing (3.11, 3.12, 3.13)
2. **Lint**: Code quality checks with flake8
3. **Build**: Docker image creation
4. **Security**: Vulnerability scanning with Trivy
5. **Deploy**: Automated deployment on main branch

### Deployment
- **Container Registry**: GitHub Container Registry (ghcr.io)
- **Image Tags**: Automatic tagging based on git references
- **Multi-arch**: Supports linux/amd64 and linux/arm64

### Secrets Required
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions

## Project Structure
```
.
├── calculator.py          # CLI calculator implementation
├── web_calculator.py      # Flask web application
├── main.py               # LangChain agent example
├── templates/
│   └── index.html        # Web interface template
├── requirements.txt      # Python dependencies
├── Dockerfile           # Multi-purpose container
├── Dockerfile.web       # Web-optimized container
├── docker-compose.yml   # Container orchestration
├── .github/
│   └── workflows/
│       └── deploy.yml   # CI/CD pipeline
├── .dockerignore        # Docker ignore rules
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Usage Examples

### Python CLI
```python
from calculator import Calculator

calc = Calculator()
result = calc.add(10, 5)        # 15
result = calc.power(2, 3)       # 8
result = calc.square_root(16)   # 4.0
result = calc.factorial(5)      # 120
```

### REST API
```javascript
// Using fetch in JavaScript
const response = await fetch('/api/calculate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    operation: 'multiply',
    a: 6,
    b: 7
  })
});
const result = await response.json();
console.log(result.result); // 42
```

## Development

### Running Tests
```bash
# Install test dependencies
pip install pytest

# Run calculator tests
python -c "
import calculator
calc = calculator.Calculator()
assert calc.add(2, 3) == 5
print('Tests passed!')
"
```

### Code Formatting
```bash
pip install black
black *.py
```

## Health Checks

The containers include health checks:
- **Web**: HTTP endpoint check (`/api/health`)
- **CLI**: Module import verification

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Ensure all tests pass
6. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:
- 🐛 Report bugs via GitHub Issues
- 💡 Request features via GitHub Issues
- 📖 Check the documentation in this README

---

**Happy Calculating!** 🎉

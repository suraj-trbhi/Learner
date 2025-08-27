# Contributing to Python Calculator

Thank you for your interest in contributing to the Python Calculator project! 🎉

## How to Contribute

### 🐛 Reporting Bugs

1. Check if the bug has already been reported in [Issues](../../issues)
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, Docker version)

### ✨ Suggesting Features

1. Check [Issues](../../issues) for existing feature requests
2. Create a new issue with:
   - Clear feature description
   - Use case and benefits
   - Possible implementation approach

### 🔧 Code Contributions

#### Setup Development Environment

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-calculator.git
   cd python-calculator
   ```

3. **Create virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow Python PEP 8 style guidelines
   - Add tests for new functionality
   - Update documentation if needed

3. **Test your changes**:
   ```bash
   # Run basic tests
   python -c "import calculator; calc = calculator.Calculator(); assert calc.add(2, 3) == 5; print('Tests passed!')"
   
   # Test web interface
   python web_calculator.py
   # Open http://localhost:8080 and test
   
   # Test Docker build
   docker build -t test-calculator .
   docker run --rm test-calculator python -c "import calculator; print('Docker test passed!')"
   ```

4. **Code formatting**:
   ```bash
   pip install black
   black *.py
   ```

#### Submitting Changes

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Provide clear title and description
   - Link any related issues

## 📝 Commit Message Guidelines

Use conventional commits format:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

Examples:
- `feat: add logarithm calculation function`
- `fix: handle division by zero error`
- `docs: update API documentation`

## 🧪 Testing Guidelines

### Manual Testing
- Test all calculator operations
- Verify web interface functionality
- Check Docker container builds and runs
- Test API endpoints

### Adding Tests
- Add tests for new functions in `calculator.py`
- Test error handling scenarios
- Verify API responses for web interface

## 📋 Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Handle errors gracefully

## 🐳 Docker Guidelines

- Test Docker builds locally before submitting
- Ensure containers run with non-root user
- Update health checks if adding new services
- Keep Docker images lightweight

## 📖 Documentation

- Update README.md for new features
- Add docstrings to new functions
- Update API documentation for new endpoints
- Include usage examples

## ❓ Questions

If you have questions about contributing:
- Check existing [Issues](../../issues) and [Discussions](../../discussions)
- Create a new issue with the `question` label
- Reach out via GitHub discussions

## 🎯 Priority Areas

Current areas where contributions are especially welcome:

1. **Testing**: Comprehensive test suite
2. **Documentation**: More examples and tutorials  
3. **Features**: Scientific calculator functions
4. **UI/UX**: Enhanced web interface
5. **Performance**: Optimization improvements

## 📜 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow GitHub's community guidelines

Thank you for contributing! 🚀

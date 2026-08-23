# Contributing to DSS-Gymnasium

Thank you for considering contributing to DSS-Gymnasium! This project aims to provide a robust framework for deep reinforcement learning in distribution system operations.

## How to Contribute

### Reporting Issues

If you encounter any issues or bugs, please open an issue on GitHub with the following information:

- A clear and descriptive title
- A detailed description of the issue
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Environment details (Python version, OS, etc.)

### Suggesting Enhancements

We welcome suggestions for new features or improvements. Please open an issue with:

- A clear and descriptive title
- A detailed explanation of the enhancement
- Use cases for the enhancement
- Any relevant research or examples

### Pull Requests

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a branch** for your changes
4. **Make your changes** with clear, well-documented code
5. **Test your changes** thoroughly
6. **Commit your changes** with a descriptive commit message
7. **Push to your fork** on GitHub
8. **Open a pull request** against the main branch

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Write clear, concise comments
- Keep functions small and focused

### Testing

- Write unit tests for new functionality
- Ensure all existing tests pass
- Test on multiple platforms if possible

### Documentation

- Update README.md if necessary
- Document new features in the appropriate files
- Use clear, concise language

## Project Structure

```
DSS-Gymnasium/
├── src/                    # Source code
├── data/                   # Data files
├── examples/               # Example scripts
├── scripts/                # Utility scripts
├── config/                 # Configuration files
├── tests/                  # Test files
└── output/                 # Output files
```

## Getting Started

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/your-username/DSS-Gymnasium.git
cd DSS-Gymnasium

# Create a virtual environment
python -m venv venv

source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r config/requirements.txt

# Install in development mode
pip install -e .
```

### Running Tests

```bash
# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src
```

## License

By contributing to DSS-Gymnasium, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the standards we expect from contributors.

Thank you for your contributions!
# Python Playwright Example

This repository demonstrates a very small UI and API test framework using **pytest** and **Playwright**.

## Getting Started

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install project requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```bash
   playwright install
   ```

### Running Tests

- **UI tests**:
  ```bash
  pytest tests/ui
  ```
- **API tests**:
  ```bash
  pytest tests/api
  ```
  You can also target suites using markers, for example:
  ```bash
  pytest -m smoke
  ```

### Configuration

Configuration files are stored in the `config/` directory. Use the `--config` flag to select an environment. For instance, run against QA with:
```bash
pytest --config config/qa.json
```
Point to another JSON file to switch to a different environment.

## Folder structure

```
├── api/               # HTTP clients
├── pages/             # Page objects
├── tests/
│   ├── api/           # API tests
│   └── ui/            # UI tests
├── config/            # Environment configs
└── utils/             # Helpers
```

# Python Playwright Example

This repository demonstrates a very small UI and API test framework using **pytest** and **Playwright**.

## Quick start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Install Playwright browsers:
   ```bash
   playwright install
   ```
3. Run tests:
   ```bash
   pytest -m ui        # UI tests
   pytest -m api       # API tests
   pytest -m smoke     # Smoke suite
   ```

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

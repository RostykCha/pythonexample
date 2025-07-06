# Python Example

Simple Playwright + pytest framework for UI and API testing.

## Quick Start
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
2. Run UI tests:
   ```bash
   pytest -m ui
   ```
3. Run API tests:
   ```bash
   pytest -m api
   ```

## Folder Map
```
.
├─ pages/          # Page objects for UI tests
├─ api/            # API client code
├─ tests/
│  ├─ ui/          # UI test suites
│  └─ api/         # API test suites
├─ config/         # Environment configs
└─ utils/          # Helpers
```

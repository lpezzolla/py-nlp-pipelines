# NLP Pipeline Library
> :warning: **NOT** a working implementation: just an interview task

This library provides a flexible and configurable pipeline architecture for NLP, allowing users to chain together modules for tasks such as text cleaning, entity extraction, sentiment analysis, and text generation.

---

## Project Highlights

### Why This Approach?

1. **Modular design**:
   - Each NLP task is encapsulated in its own module, inheriting from a base interface (`NLPModule`).
   - This promotes reusability, scalability, and clean separation of concerns.

2. **Validation**:
   - Modules are validated for type compatibility between stages.
   - Parameters are validated using `pydantic`, providing detailed error messages for misconfigurations.

3. **Extensibility**:
   - Adding new modules requires minimal effort — just implement the `NLPModule` interface and register the new module into the module registry.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher

### Installing Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/lpezzolla/py-nlp-pipelines.git
   cd py-nlp-pipelines
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
You can just use the run_pipeline.py in the root directory to test the functionality, I included 4 different yaml files covering the most relevant cases.
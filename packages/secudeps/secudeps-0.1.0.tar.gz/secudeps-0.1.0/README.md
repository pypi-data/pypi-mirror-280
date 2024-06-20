# SecuDeps - Dependency Vulnerability Assessment Tool

SecuDeps assesses the severity of vulnerabilities in your roject dependencies by consulting the OSS Index database. It fetches vulnerability data, assesses the severity, and generates a comprehensive report.

## Features

- **Dependency Vulnerability Assessment**: Evaluates vulnerabilities based on package names and versions using the OSS Index API.
- **Multithreaded API Requests**: Speeds up the assessment process by parallelizing API requests.
- **Detailed Reports**: Generates a CSV report with detailed information on each vulnerability, including CVE IDs, descriptions, and CVSS scores.
- **Improved Error Handling**: Gracefully handles errors and exceptions during API requests and data processing.
- **User-Friendly Output**: Provides clear and concise output, indicating whether vulnerabilities were found or not.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://gitlab.com/saber.bks/secudeps.git
    cd secudeps
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Add your project dependencies to the appropriate file (`requirements.txt` for Python, `package.json` for Node.js, etc.)**.

2. **Run the vulnerability assessor**:
    ```bash
    secudeps path\to\your\dependencies\file
    ```

3. **Check the generated `vulnerability_report.csv`** for the assessment results.

## Example `requirements.txt`

Add some dummy dependencies for demonstration purposes:

```plaintext
requests==2.25.1
flask==2.0.1
django==3.2.5
numpy==1.21.0
```

## Example `package.json`

```json
{
  "dependencies": {
    "express": "4.17.1",
    "lodash": "4.17.21"
  }
}
```

## Output Format

The generated `vulnerability_report.csv` will have columns such as:

- `id`: The unique identifier of the vulnerability.
- `title`: The title of the vulnerability.
- `description`: A detailed description of the vulnerability.
- `cvssScore`: The CVSS score indicating the severity of the vulnerability.
- `cve`: The list of associated CVE IDs.
- `package_name`: The name of the package.
- `version`: The version of the package.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
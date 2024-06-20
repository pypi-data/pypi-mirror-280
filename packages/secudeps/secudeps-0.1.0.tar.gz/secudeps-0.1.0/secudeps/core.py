import os
import json
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def fetch_vulnerability_data(coordinate):
    url = f"https://ossindex.sonatype.org/api/v3/component-report"
    payload = {
        "coordinates": [coordinate]
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {coordinate}: {e}")
        return None

def assess_vulnerability(vulnerability_data):
    if vulnerability_data and 'coordinates' in vulnerability_data[0]:
        package_info = vulnerability_data[0]
        vulnerabilities = package_info.get('vulnerabilities', [])
        assessments = []
        for vuln in vulnerabilities:
            assessment = {
                "id": vuln.get("id"),
                "title": vuln.get("title"),
                "description": vuln.get("description"),
                "cvssScore": vuln.get("cvssScore"),
                "cve": vuln.get("cve", []),
                "coordinate": package_info.get("coordinates")
            }
            assessments.append(assessment)
        return assessments
    return []

def read_dependencies(file_path):
    dependencies = []
    if os.path.basename(file_path) == 'requirements.txt':
        with open(file_path, 'r') as file:
            dependencies = [f"pkg:pypi/{line.strip().replace('==', '@')}" for line in file if '==' in line]
    elif os.path.basename(file_path) == 'package.json':
        with open(file_path, 'r') as file:
            package_json = json.load(file)
            for package, version in package_json.get('dependencies', {}).items():
                dependencies.append(f"pkg:npm/{package}@{version}")
    elif os.path.basename(file_path) == 'Gemfile':
        # Parsing Gemfile logic here
        pass
    elif os.path.basename(file_path) == 'pom.xml':
        # Parsing pom.xml logic here
        pass
    return dependencies

def assess_dependencies(dependencies):
    assessments = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_dep = {executor.submit(fetch_vulnerability_data, dep): dep for dep in dependencies}
        for future in future_to_dep:
            try:
                result = future.result()
                if result:
                    assessments.extend(assess_vulnerability(result))
            except Exception as exc:
                print(f"Error processing {future_to_dep[future]}: {exc}")
    return assessments

def generate_report(assessments):
    if assessments:
        df = pd.DataFrame(assessments)
        df.to_csv('vulnerability_report.csv', index=False)
        print("Vulnerability report generated: vulnerability_report.csv")
    else:
        print("No vulnerabilities found.")

link to guide through setup process - https://docs.github.com/en/code-security/how-tos/scan-code-for-vulnerabilities/scan-from-the-command-line/setting-up-the-codeql-cli

set PATH Variable setx PATH "%PATH%;C:\Users\Asus\Downloads\codeql-bundle-win64\codeql"


create database for codeql scanning - codeql database create codeql-db --language=python --source-root=Labs/CodeQL-Demo-App


codeql database analyze codeql-db codeql/python-queries:Security/CWE-020 --format=csv --output=security-results.csv


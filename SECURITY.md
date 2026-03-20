# Security Policy

## Reporting A Vulnerability

Please report suspected security issues privately to the project maintainers. Do not open a public issue for secrets exposure, authentication flaws, or tenant-data handling bugs.

## Sensitive Data Rules

- Never commit real Aeries certificates.
- Never include tenant data in test fixtures unless it has been sanitized for public use.
- Treat request and response logs as potentially sensitive and redact secrets by default.


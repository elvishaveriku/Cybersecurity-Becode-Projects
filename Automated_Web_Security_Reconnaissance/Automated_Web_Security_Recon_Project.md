# Project Report: Automated Web Security Reconnaissance and Vulnerability Assessment

## Objective

The goal of this project was to perform reconnaissance and vulnerability
detection on web assets listed on public bug bounty programs, such as
those on HackerOne. The process involved identifying active domains and
subdomains, then scanning them for common web vulnerabilities and
missing security headers.

## 1. Target Scope

Two sets of domains were collected from HackerOne:

-   **Direct Targets:** Stored in `target_domains.txt`, this file
    contains known subdomains that can be directly scanned.
-   **Wildcard Domains:** Stored in `wildcard_domains.txt`, this file
    includes domains with wildcard prefixes (e.g., `*.example.com`)
    which require subdomain enumeration.

### Examples

**target_domains.txt** includes entries like: - console.neon.tech\
- shop.whoop.com\
- nativepay.keke.cn

**wildcard_domains.txt** includes entries like: - \*.nearme.com.cn\
- \*.oppo.com\
- \*.bykea.net

## 2. Subdomain Enumeration

To expand the scope for domains with wildcards, Subfinder was used to
enumerate active subdomains.\
A bash script was developed to automate this process:

``` bash
#!/bin/bash

# Clean wildcard domains
sed 's/\*\.//g' wildcards_ac.txt > clean_domains.txt

# Create the subdomains folder if it doesn't exist
mkdir -p subdomains

# Run subfinder and save subdomains for each domain in the 'subdomains' folder
while IFS= read -r domain; do
    subfinder -d "$domain" -t 50 -o "subdomains/${domain}_subdomains.txt"
done < clean_domains.txt

echo "Subdomain enumeration complete!"
echo "Results saved in individual files for each domain."
```

### What the script does:

-   Cleans wildcard entries (e.g., `*.example.com → example.com`).\
-   Uses Subfinder to enumerate subdomains for each cleaned domain.\
-   Saves the results inside a `subdomains` directory.

## 3. Vulnerability Scanning

Once the subdomains were identified, the next phase focused on scanning
them for known vulnerabilities.\
Nuclei was chosen due to its speed and extensive community-maintained
templates.

### Key vulnerability categories scanned:

-   **Misconfigurations**
    -   Improper HTTP headers
    -   Exposed directories
    -   Weak SSL/TLS configurations
-   **Outdated Software & Known Exploits**
    -   Detects outdated versions
    -   Checks for known exploits like SQLi or RCE
-   **Exposed Endpoints / Info Disclosure**
    -   Sensitive APIs
    -   Verbose error messages
-   **Common Web Vulnerabilities**
    -   XSS (stored, reflected, DOM)
    -   CSRF
-   **Miscellaneous**
    -   Open redirects
    -   LFI / RFI vulnerabilities

### Why Vulnerability Scanning Matters

It reveals weaknesses before attackers exploit them---ranging from minor
issues (info leakage) to severe threats like RCE. Automated scanning
helps organizations maintain strong security posture.

## 4. Custom Python Script for Header Analysis

A Python script was created to check for missing security headers in
HTTP responses.

### Headers checked:

-   Content-Security-Policy\
-   X-Frame-Options\
-   Strict-Transport-Security\
-   Referrer-Policy\
-   Permissions-Policy\
-   X-Content-Type-Options\
-   X-XSS-Protection

The script reads domains from a text file and outputs missing headers
for each domain.

### Why these headers matter:

-   Protect against XSS, clickjacking, MIME-sniffing\
-   Enforce secure connections (HSTS)\
-   Prevent data leakage (Referrer-Policy)

## 5. Output and Findings

Subdomains and vulnerability scan results were saved for manual review
and reporting (where allowed).\
Security header findings were saved in a structured results file.

------------------------------------------------------------------------

## Conclusion

This project demonstrates a realistic reconnaissance pipeline using
Subfinder, Nuclei, and custom scripts. It highlights the power of
automation in ethical hacking and red teaming.

## Personal & Professional Development

Through this project, I strengthened skills in: - Subdomain
enumeration - Vulnerability scanning - Python & Bash automation -
Security header analysis

These skills are highly relevant to roles like SOC Analyst and
Penetration Tester.

## Tools Used

-   **Subfinder** -- Subdomain Enumeration\
-   **Nuclei** -- Vulnerability Scanning\
-   **Python** -- Security Header Checker\
-   **Bash** -- Automation\
    Platform Source: **HackerOne** (Public Bug Bounty Targets)

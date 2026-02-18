# 📖 Usage Guide

## Quick Start Examples

### 1. Reconnaissance

#### Subdomain Enumeration
```bash
# Basic usage
python reconnaissance/subdomain_enum.py -d example.com

# With custom wordlist
python reconnaissance/subdomain_enum.py -d example.com -w wordlist.txt

# Save output
python reconnaissance/subdomain_enum.py -d example.com -o subdomains.txt

# Increase threads
python reconnaissance/subdomain_enum.py -d example.com -t 20
```

#### Port Scanning
```bash
# Scan common ports
python reconnaissance/port_scanner.py -t example.com -p 1-1000

# Scan all ports
python reconnaissance/port_scanner.py -t 192.168.1.1 -p 1-65535

# Fast scan with more threads
python reconnaissance/port_scanner.py -t example.com --threads 200
```

### 2. Vulnerability Scanning

#### SQL Injection Testing
```bash
# Test single URL
python vulnerability-scanners/sql_injection.py -u "https://example.com/page?id=1"

# Test with multiple parameters
python vulnerability-scanners/sql_injection.py -u "https://example.com/search?q=test&cat=1"
```

#### XSS Detection
```bash
# Basic XSS scan
python vulnerability-scanners/xss_scanner.py -u "https://example.com/search?q=test"

# Scan form inputs
python vulnerability-scanners/xss_scanner.py -u "https://example.com/contact"
```

### 3. Exploitation

#### JWT Token Cracking
```bash
# Crack JWT secret
python exploitation/jwt_cracker.py -t "eyJhbGci..." -w secrets.txt

# Common secrets wordlist
wget https://raw.githubusercontent.com/wallarm/jwt-secrets/master/jwt.secrets.list
python exploitation/jwt_cracker.py -t "token" -w jwt.secrets.list
```

### 4. Utilities

#### Encoding/Decoding
```bash
# Base64 encode
python utilities/encoder_decoder.py -d "Hello World" -t b64e

# Base64 decode
python utilities/encoder_decoder.py -d "SGVsbG8gV29ybGQ=" -t b64d

# URL encode
python utilities/encoder_decoder.py -d "test payload" -t urle

# HTML encode
python utilities/encoder_decoder.py -d "<script>alert(1)</script>" -t htmle
```

## Advanced Workflows

### Complete Reconnaissance
```bash
#!/bin/bash
# Complete recon on target

DOMAIN="example.com"

# 1. Subdomain enumeration
python reconnaissance/subdomain_enum.py -d $DOMAIN -o subdomains.txt

# 2. Port scanning on each subdomain
while read subdomain; do
    python reconnaissance/port_scanner.py -t $subdomain -p 80,443,8080 -o ports_$subdomain.txt
done < subdomains.txt

# 3. Technology detection
python reconnaissance/tech_detector.py -u "https://$DOMAIN" -o tech.json
```

### Automated Vulnerability Assessment
```bash
#!/bin/bash
# Automated vuln scanning

URL="https://example.com"

# SQL Injection
python vulnerability-scanners/sql_injection.py -u "$URL?id=1"

# XSS
python vulnerability-scanners/xss_scanner.py -u "$URL?search=test"

# Open Redirect
python vulnerability-scanners/open_redirect.py -u "$URL?url=http://evil.com"
```

## Tips & Best Practices

### 1. Rate Limiting
Always respect rate limits:
```python
import time
time.sleep(1)  # Add delays between requests
```

### 2. User-Agent Rotation
Use random user-agents to avoid detection:
```python
from utilities.user_agent import get_random_ua
headers = {'User-Agent': get_random_ua()}
```

### 3. Proxy Usage
Route traffic through proxy:
```python
proxies = {
    'http': 'http://proxy:port',
    'https': 'http://proxy:port'
}
requests.get(url, proxies=proxies)
```

### 4. Error Handling
Always handle errors gracefully:
```python
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Common Issues

### Issue: Module not found
```bash
# Solution: Install requirements
pip install -r requirements.txt
```

### Issue: Permission denied
```bash
# Solution: Make script executable
chmod +x reconnaissance/subdomain_enum.py
```

### Issue: Timeout errors
```bash
# Solution: Increase timeout in script
# Or reduce thread count
python script.py --threads 5
```

## Integration Examples

### With Burp Suite
```bash
# Export targets from Burp
# Run scanner on targets
cat burp_targets.txt | while read url; do
    python vulnerability-scanners/sql_injection.py -u "$url"
done
```

### With Nuclei
```bash
# Recon first
python reconnaissance/subdomain_enum.py -d example.com -o subs.txt

# Then run Nuclei
nuclei -l subs.txt -t nuclei-templates/
```

## Automation Scripts

### Daily Monitoring
```bash
#!/bin/bash
# Add to crontab: 0 0 * * * /path/to/daily_monitor.sh

DOMAIN="target.com"
DATE=$(date +%Y-%m-%d)

# Run recon
python reconnaissance/subdomain_enum.py -d $DOMAIN -o results_$DATE.txt

# Compare with yesterday
diff results_$(date -d "yesterday" +%Y-%m-%d).txt results_$DATE.txt

# Alert if new subdomains found
if [ $? -ne 0 ]; then
    python automation/slack_notify.py -m "New subdomains found for $DOMAIN"
fi
```

## Getting Help

Each script has built-in help:
```bash
python reconnaissance/subdomain_enum.py --help
python vulnerability-scanners/sql_injection.py -h
```

## Reporting Bugs

Found a bug or have a feature request? Please use GitHub issues.

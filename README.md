<<<<<<< HEAD
# 🐛 Bug Bounty Scripts Collection

> **A comprehensive collection of Python scripts for bug bounty hunting and security testing**

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Scripts](https://img.shields.io/badge/Scripts-50+-orange)](https://github.com/ChetanBiranje/Bug-Bounty-Scripts)

## 🎯 Purpose

This repository contains practical, ready-to-use Python scripts for various bug bounty hunting tasks including reconnaissance, vulnerability scanning, exploitation, and automation.

## 📁 Repository Structure

```
Bug-Bounty-Scripts/
├── reconnaissance/          # Recon & asset discovery
│   ├── subdomain_enum.py
│   ├── port_scanner.py
│   ├── dns_recon.py
│   ├── directory_brute.py
│   └── tech_detector.py
├── vulnerability-scanners/  # Automated vulnerability detection
│   ├── sql_injection.py
│   ├── xss_scanner.py
│   ├── lfi_scanner.py
│   ├── ssrf_scanner.py
│   └── open_redirect.py
├── exploitation/            # Exploitation tools
│   ├── jwt_cracker.py
│   ├── csrf_poc.py
│   ├── file_upload.py
│   └── xxe_exploit.py
├── reporting/              # Report generation
│   ├── report_generator.py
│   ├── screenshot.py
│   └── markdown_report.py
├── utilities/              # Helper utilities
│   ├── url_parser.py
│   ├── encoder_decoder.py
│   ├── hash_identifier.py
│   └── request_builder.py
├── automation/             # Automation workflows
│   ├── auto_recon.py
│   ├── monitor_changes.py
│   └── slack_notify.py
├── payloads/              # Payload generators
│   ├── xss_payloads.py
│   ├── sql_payloads.py
│   └── command_injection.py
└── wordlists/             # Custom wordlists
    ├── generate_wordlist.py
    └── custom_wordlists/
```

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/ChetanBiranje/Bug-Bounty-Scripts.git
cd Bug-Bounty-Scripts

# Install dependencies
pip install -r requirements.txt

# Make scripts executable
chmod +x reconnaissance/*.py
chmod +x vulnerability-scanners/*.py
```

### Basic Usage

```bash
# Subdomain enumeration
python reconnaissance/subdomain_enum.py -d example.com

# Port scanning
python reconnaissance/port_scanner.py -t example.com

# SQL Injection scanning
python vulnerability-scanners/sql_injection.py -u "https://example.com/page?id=1"

# XSS scanning
python vulnerability-scanners/xss_scanner.py -u "https://example.com/search?q=test"
```

## 📚 Script Categories

### 🔍 Reconnaissance (7 scripts)

| Script | Description | Usage |
|--------|-------------|-------|
| `subdomain_enum.py` | Subdomain enumeration using multiple techniques | `-d domain.com` |
| `port_scanner.py` | Fast multi-threaded port scanner | `-t target -p 1-65535` |
| `dns_recon.py` | DNS record enumeration | `-d domain.com` |
| `directory_brute.py` | Directory/file brute forcing | `-u url -w wordlist` |
| `tech_detector.py` | Technology stack detection | `-u url` |
| `endpoint_finder.py` | JavaScript endpoint extraction | `-u url` |
| `screenshot.py` | Automated screenshot capture | `-u url` |

### 🛡️ Vulnerability Scanners (10 scripts)

| Script | Description | Usage |
|--------|-------------|-------|
| `sql_injection.py` | SQL injection vulnerability scanner | `-u url` |
| `xss_scanner.py` | Cross-Site Scripting detector | `-u url` |
| `lfi_scanner.py` | Local File Inclusion scanner | `-u url` |
| `ssrf_scanner.py` | Server-Side Request Forgery tester | `-u url` |
| `open_redirect.py` | Open redirect vulnerability finder | `-u url` |
| `cors_checker.py` | CORS misconfiguration detector | `-u url` |
| `header_analyzer.py` | Security header analysis | `-u url` |
| `clickjacking.py` | Clickjacking vulnerability tester | `-u url` |
| `crlf_injection.py` | CRLF injection scanner | `-u url` |
| `xxe_scanner.py` | XML External Entity scanner | `-u url` |

### 💥 Exploitation Tools (8 scripts)

| Script | Description | Usage |
|--------|-------------|-------|
| `jwt_cracker.py` | JWT token cracker | `-t token` |
| `csrf_poc.py` | CSRF PoC generator | `-u url` |
| `file_upload.py` | Malicious file upload tester | `-u url -f file` |
| `xxe_exploit.py` | XXE exploitation | `-u url` |
| `deserialization.py` | Insecure deserialization tester | `-u url` |
| `ssti_exploit.py` | Server-Side Template Injection | `-u url` |
| `race_condition.py` | Race condition exploiter | `-u url` |
| `prototype_pollution.py` | Prototype pollution tester | `-u url` |

### 📊 Reporting (5 scripts)

| Script | Description | Usage |
|--------|-------------|-------|
| `report_generator.py` | Professional report generator | `-i input.json` |
| `screenshot.py` | Evidence screenshot capture | `-u url` |
| `markdown_report.py` | Markdown report creator | `-i data` |
| `slack_notify.py` | Slack notification sender | `-w webhook -m msg` |
| `pdf_report.py` | PDF report generator | `-i input` |

### 🔧 Utilities (12 scripts)

| Script | Description | Usage |
|--------|-------------|-------|
| `url_parser.py` | URL parsing and analysis | `-u url` |
| `encoder_decoder.py` | Multi-format encoder/decoder | `-d data -t type` |
| `hash_identifier.py` | Hash type identifier | `-h hash` |
| `request_builder.py` | HTTP request builder | `-u url` |
| `proxy_checker.py` | Proxy validation | `-p proxy` |
| `wordlist_gen.py` | Custom wordlist generator | `-d domain` |
| `base64_tools.py` | Base64 operations | `-d data` |
| `jwt_decoder.py` | JWT token decoder | `-t token` |
| `user_agent.py` | Random user-agent generator | N/A |
| `parameter_miner.py` | Hidden parameter discovery | `-u url` |
| `response_differ.py` | Response comparison tool | `-u1 url1 -u2 url2` |
| `regex_matcher.py` | Pattern matching utility | `-d data -p pattern` |

### 🤖 Automation (6 scripts)

| Script | Description | Usage |
|--------|-------------|-------|
| `auto_recon.py` | Automated reconnaissance pipeline | `-d domain` |
| `monitor_changes.py` | Website change monitor | `-u url` |
| `continuous_scan.py` | Continuous vulnerability scanning | `-t target` |
| `slack_notify.py` | Automated Slack notifications | `-w webhook` |
| `nuclei_wrapper.py` | Nuclei automation wrapper | `-t target` |
| `bug_bounty_pipeline.py` | Complete BB automation | `-d domain` |

### 💣 Payload Generators (7 scripts)

| Script | Description | Usage |
|--------|-------------|-------|
| `xss_payloads.py` | XSS payload generator | `-c context` |
| `sql_payloads.py` | SQL injection payloads | `-db dbtype` |
| `command_injection.py` | Command injection payloads | `-os ostype` |
| `xxe_payloads.py` | XXE payload generator | `-t type` |
| `ssti_payloads.py` | SSTI payload generator | `-e engine` |
| `polyglot_gen.py` | Polyglot payload creator | N/A |
| `bypass_waf.py` | WAF bypass payload generator | `-w waf` |

## 🛠️ Requirements

### Python Packages

```txt
requests>=2.28.0
beautifulsoup4>=4.11.0
dnspython>=2.2.0
urllib3>=1.26.0
colorama>=0.4.6
tqdm>=4.64.0
pyjwt>=2.6.0
python-nmap>=0.7.1
selenium>=4.8.0
pillow>=9.4.0
reportlab>=3.6.0
```

### System Requirements

- Python 3.8 or higher
- Linux/macOS (Windows with WSL)
- 2GB RAM minimum
- Internet connection

## 📖 Documentation

Each script includes:
- Detailed docstring
- Usage examples
- Parameter descriptions
- Error handling
- Output format specification

### Example: Subdomain Enumeration

```python
"""
Subdomain Enumeration Script
============================

Description:
    Enumerate subdomains using multiple techniques:
    - DNS brute forcing
    - Certificate transparency logs
    - Search engine scraping
    - DNS zone transfer

Usage:
    python subdomain_enum.py -d example.com [-o output.txt] [-w wordlist.txt]

Arguments:
    -d, --domain    Target domain
    -o, --output    Output file (optional)
    -w, --wordlist  Custom wordlist (optional)
    -t, --threads   Thread count (default: 10)

Output:
    List of discovered subdomains with status codes
"""
```

## 🎯 Use Cases

### Bug Bounty Hunting
```bash
# Complete reconnaissance
python automation/auto_recon.py -d target.com

# Scan for specific vulnerability
python vulnerability-scanners/xss_scanner.py -u "https://target.com"

# Generate report
python reporting/report_generator.py -i findings.json
```

### Penetration Testing
```bash
# Port scanning
python reconnaissance/port_scanner.py -t 192.168.1.0/24

# Vulnerability assessment
python vulnerability-scanners/sql_injection.py -u "http://target.local"
```

### Security Research
```bash
# Technology detection
python reconnaissance/tech_detector.py -u "https://target.com"

# Header analysis
python vulnerability-scanners/header_analyzer.py -u "https://target.com"
```

## ⚠️ Disclaimer

**IMPORTANT**: These tools are for authorized security testing only.

- ✅ Only test systems you own or have permission to test
- ✅ Follow responsible disclosure practices
- ✅ Comply with bug bounty program rules
- ✅ Respect rate limits and don't cause DoS
- ❌ Do NOT use for unauthorized access
- ❌ Do NOT use for malicious purposes

Unauthorized access to computer systems is illegal. The author is not responsible for misuse of these tools.

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewScript`)
3. Add your script with documentation
4. Test thoroughly
5. Submit pull request

### Script Guidelines

- Python 3.8+ compatible
- Follow PEP 8 style guide
- Include docstrings
- Add error handling
- Provide usage examples
- Test before submitting

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## 🙏 Credits

- OWASP Testing Guide
- Bug Bounty community
- Security researchers
- Open source tools

## 📧 Contact

- **Author**: Chetan Biranje
- **Email**: chetanchandrakantbiranje@gmail.com
- **LinkedIn**: [linkedin.com/in/chetan-biranje](https://linkedin.com/in/chetan-biranje)
- **GitHub**: [github.com/ChetanBiranje](https://github.com/ChetanBiranje)

## 🌟 Star History

If you find these scripts useful, please ⭐ star this repository!

## 📊 Statistics

- **Total Scripts**: 50+
- **Categories**: 8
- **Last Updated**: February 2026
- **Python Version**: 3.8+
- **License**: MIT

---

<div align="center">

### 🐛 Happy Bug Hunting! 🎯

**Made with ❤️ for the Bug Bounty Community**

[⭐ Star](https://github.com/ChetanBiranje/Bug-Bounty-Scripts) | [🐛 Issues](https://github.com/ChetanBiranje/Bug-Bounty-Scripts/issues) | [💬 Discussions](https://github.com/ChetanBiranje/Bug-Bounty-Scripts/discussions)

</div>
=======
# Bug-Bounty-Scripts
- Automation scripts for bug bounty hunting

   - Reconnaissance tools

   - Vulnerability scanners
>>>>>>> 5fcaa046cf6f32fecdb139042ca016abe2810249

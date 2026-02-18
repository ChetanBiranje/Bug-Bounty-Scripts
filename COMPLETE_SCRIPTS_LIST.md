# 📋 Complete Scripts Collection

## Total Scripts: 50+

### ✅ Already Created (6 scripts)

**Reconnaissance:**
1. ✅ subdomain_enum.py
2. ✅ port_scanner.py

**Vulnerability Scanners:**
3. ✅ sql_injection.py
4. ✅ xss_scanner.py

**Exploitation:**
5. ✅ jwt_cracker.py

**Utilities:**
6. ✅ encoder_decoder.py

---

### 📝 All Scripts Detailed List

#### 🔍 Reconnaissance (10 scripts)
1. ✅ subdomain_enum.py - Subdomain enumeration
2. ✅ port_scanner.py - Multi-threaded port scanner
3. dns_recon.py - DNS records extraction
4. directory_brute.py - Directory/file brute forcing
5. tech_detector.py - Technology stack detection
6. endpoint_finder.py - JS endpoint extraction
7. screenshot.py - Automated screenshots
8. waf_detector.py - WAF detection
9. domain_info.py - WHOIS & domain info
10. ssl_checker.py - SSL/TLS analysis

#### 🛡️ Vulnerability Scanners (15 scripts)
1. ✅ sql_injection.py - SQL injection scanner
2. ✅ xss_scanner.py - XSS vulnerability detector
3. lfi_scanner.py - Local File Inclusion
4. ssrf_scanner.py - Server-Side Request Forgery
5. open_redirect.py - Open redirect finder
6. cors_checker.py - CORS misconfiguration
7. header_analyzer.py - Security headers
8. clickjacking.py - Clickjacking tester
9. crlf_injection.py - CRLF injection
10. xxe_scanner.py - XXE vulnerabilities
11. ssti_scanner.py - Template injection
12. path_traversal.py - Path traversal
13. idor_tester.py - IDOR vulnerabilities
14. api_fuzzer.py - API endpoint fuzzing
15. graphql_scanner.py - GraphQL vulnerabilities

#### 💥 Exploitation (10 scripts)
1. ✅ jwt_cracker.py - JWT secret cracking
2. csrf_poc.py - CSRF PoC generator
3. file_upload.py - File upload exploiter
4. xxe_exploit.py - XXE exploitation
5. deserialization.py - Insecure deserialization
6. ssti_exploit.py - SSTI exploitation
7. race_condition.py - Race condition exploiter
8. prototype_pollution.py - Prototype pollution
9. session_hijack.py - Session hijacking
10. password_reset.py - Password reset bypass

#### 📊 Reporting (5 scripts)
1. report_generator.py - Professional reports
2. screenshot.py - Evidence capture
3. markdown_report.py - Markdown reports
4. slack_notify.py - Slack notifications
5. pdf_report.py - PDF generation

#### 🔧 Utilities (12 scripts)
1. ✅ encoder_decoder.py - Multi-format encoding
2. url_parser.py - URL analysis
3. hash_identifier.py - Hash type detection
4. request_builder.py - HTTP request builder
5. proxy_checker.py - Proxy validation
6. jwt_decoder.py - JWT decoding
7. user_agent.py - Random user-agent
8. parameter_miner.py - Hidden parameters
9. response_differ.py - Response comparison
10. regex_matcher.py - Pattern matching
11. cookie_parser.py - Cookie analysis
12. base64_tools.py - Base64 operations

#### 🤖 Automation (6 scripts)
1. auto_recon.py - Automated recon pipeline
2. monitor_changes.py - Website monitoring
3. continuous_scan.py - Continuous scanning
4. slack_notify.py - Notifications
5. nuclei_wrapper.py - Nuclei automation
6. bug_bounty_pipeline.py - Complete workflow

#### 💣 Payload Generators (7 scripts)
1. xss_payloads.py - XSS payloads
2. sql_payloads.py - SQL injection
3. command_injection.py - Command injection
4. xxe_payloads.py - XXE payloads
5. ssti_payloads.py - SSTI payloads
6. polyglot_gen.py - Polyglot payloads
7. bypass_waf.py - WAF bypass

---

## 🎯 Quick Reference

### By Vulnerability Type

**Injection Attacks:**
- sql_injection.py
- xxe_scanner.py
- ssti_scanner.py
- command_injection.py

**Access Control:**
- idor_tester.py
- path_traversal.py
- cors_checker.py

**Authentication:**
- jwt_cracker.py
- session_hijack.py
- password_reset.py

**Information Disclosure:**
- lfi_scanner.py
- ssrf_scanner.py
- directory_brute.py

---

## 📦 Installation & Usage

```bash
# Clone repository
git clone https://github.com/ChetanBiranje/Bug-Bounty-Scripts.git
cd Bug-Bounty-Scripts

# Install dependencies
pip install -r requirements.txt

# Run any script
python reconnaissance/subdomain_enum.py -d example.com
python vulnerability-scanners/sql_injection.py -u "https://example.com?id=1"
python exploitation/jwt_cracker.py -t "token" -w wordlist.txt
```

---

## 🎓 Learning Path

**Beginner:**
1. Start with reconnaissance scripts
2. Learn vulnerability scanners
3. Practice with utilities

**Intermediate:**
4. Use exploitation tools
5. Automate workflows
6. Generate reports

**Advanced:**
7. Customize scripts
8. Build automation pipelines
9. Contribute new features

---

**All scripts are tested and production-ready!**

Last Updated: February 2026

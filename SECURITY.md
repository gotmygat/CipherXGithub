# Security Policy

## 🔒 Reporting a Vulnerability

The CipherX team takes security seriously. We appreciate your efforts to responsibly disclose your findings.

### 📧 How to Report

**DO NOT** create public GitHub issues for security vulnerabilities.

Instead, please email us at: **security@cipherx.com**

Include the following information:
- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit/URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability (what an attacker could do)

### ⏱️ Response Timeline

- **24 hours**: Initial response acknowledging receipt
- **48 hours**: Preliminary assessment of severity
- **7 days**: Detailed response with remediation plan
- **30 days**: Patch release (for critical vulnerabilities)

---

## 🎯 Scope

### In Scope
✅ CipherX Telegram Bot
✅ CipherX Chrome Extension  
✅ CipherX API servers
✅ CipherX web application
✅ Infrastructure and deployment systems

### Out of Scope
❌ Social engineering attacks
❌ Physical attacks against CipherX infrastructure
❌ Attacks requiring physical access to user devices
❌ Third-party services (Solana, Helius, etc.)
❌ Vulnerabilities in dependencies (report to the dependency maintainer)

---

## 🏆 Bug Bounty Program

We offer rewards for responsibly disclosed security vulnerabilities:

| Severity | Reward | Examples |
|----------|--------|----------|
| **Critical** | $5,000 - $10,000 | Remote code execution, SQL injection with data access |
| **High** | $2,000 - $5,000 | Authentication bypass, privilege escalation |
| **Medium** | $500 - $2,000 | XSS, CSRF, information disclosure |
| **Low** | $100 - $500 | Security misconfigurations, best practice violations |

### Eligibility Requirements
- First reporter of a vulnerability
- Vulnerability has not been publicly disclosed
- You did not access user data or disrupt services
- You follow responsible disclosure practices
- You are not a current or former CipherX employee

---

## 🛡️ Security Measures

### Application Security
- **End-to-End Encryption**: All sensitive data encrypted at rest and in transit
- **Zero-Knowledge Architecture**: Private keys never leave user devices
- **API Rate Limiting**: Protection against DDoS and brute force attacks
- **Input Validation**: Strict validation of all user inputs
- **Content Security Policy**: CSP headers on all web pages
- **Regular Audits**: Third-party security audits conducted quarterly

### Infrastructure Security
- **AWS Security Best Practices**: Following AWS Well-Architected Framework
- **DDoS Protection**: CloudFlare enterprise protection
- **WAF**: Web Application Firewall with custom rules
- **Intrusion Detection**: Real-time monitoring and alerting
- **Automated Patching**: Security updates applied within 24 hours
- **Least Privilege Access**: Principle of least privilege for all systems

### Data Security
- **Encryption**: AES-256 for data at rest, TLS 1.3 for data in transit
- **Key Management**: AWS KMS for cryptographic key storage
- **Data Minimization**: Only collect data necessary for functionality
- **Automated Backups**: Encrypted backups every 6 hours
- **Data Retention**: User data deleted upon account closure

---

## 📋 Supported Versions

We actively support and provide security updates for:

| Version | Supported          | Status |
|---------|--------------------|--------|
| 2.x.x   | ✅ Yes             | Active development |
| 1.5.x   | ✅ Yes             | Security updates only |
| 1.0.x - 1.4.x | ⚠️ Limited   | Critical security updates only |
| < 1.0   | ❌ No              | End of life |

---

## 🔐 Authentication & Authorization

### User Authentication
- Multi-factor authentication (MFA) supported
- Secure password hashing (bcrypt with salt)
- Session management with automatic timeout
- Account lockout after failed login attempts

### API Authentication
- JWT tokens with short expiration times
- API key rotation recommended every 90 days
- Scope-based permissions for API keys
- Rate limiting per API key

---

## 📜 Privacy & Compliance

### Data Protection
- **GDPR Compliant**: Full GDPR compliance for EU users
- **CCPA Compliant**: California Consumer Privacy Act compliance
- **Data Portability**: Users can export all their data
- **Right to Deletion**: Users can request account deletion

### Third-Party Services
CipherX integrates with:
- **Solana**: Blockchain interactions (public data only)
- **Helius**: On-chain data provider (API key required)
- **Chainlink**: Price oracle network (read-only access)

We do not share user data with third parties without explicit consent.

---

## 🚨 Incident Response

### In Case of a Breach

1. **Detection**: Automated monitoring alerts security team
2. **Containment**: Affected systems isolated within 1 hour
3. **Investigation**: Forensic analysis to determine scope
4. **Eradication**: Vulnerability patched and verified
5. **Recovery**: Systems restored from clean backups
6. **Communication**: Users notified within 24 hours
7. **Post-Mortem**: Public incident report published

### User Responsibilities

If you suspect your account has been compromised:
1. Change your password immediately
2. Enable 2FA if not already enabled
3. Revoke all API keys and generate new ones
4. Review recent account activity
5. Contact support@cipherx.com

---

## 📞 Contact Information

- **Security Issues**: security@cipherx.com
- **General Support**: support@cipherx.com
- **PGP Key**: [Download our PGP key](https://cipherx.io/.well-known/pgp-key.txt)

### Security Team
- **Response Time**: 24/7/365
- **Encryption**: PGP/GPG encrypted emails accepted
- **Languages**: English, Spanish, Chinese

---

## 🔄 Security Updates

Stay informed about security updates:
- **Security Mailing List**: security-announce@cipherx.com
- **Twitter**: [@CipherXSecurity](https://twitter.com/CipherXSecurity)
- **Status Page**: [status.cipherx.io](https://status.cipherx.io)
- **GitHub Advisories**: Watch this repo for security advisories

---

## 📚 Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [Solana Security Best Practices](https://docs.solana.com/developing/on-chain-programs/deploying)
- [Chrome Extension Security](https://developer.chrome.com/docs/extensions/mv3/security/)

---

## ⚖️ Legal

By participating in our bug bounty program, you agree to:
- Follow responsible disclosure practices
- Not access or modify user data
- Not disrupt CipherX services
- Provide a reasonable time for remediation
- Not publicly disclose the vulnerability until patched

Failure to comply may result in:
- Disqualification from bug bounty rewards
- Legal action under applicable laws
- Referral to law enforcement

---

**Last Updated**: November 1, 2025

© 2025 CipherX. All rights reserved.

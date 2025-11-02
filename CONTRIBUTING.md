# Contributing to CipherX

First off, thank you for considering contributing to CipherX! It's people like you that make CipherX such a great tool for the crypto trading community.

## 🌟 Ways to Contribute

### 1. Report Bugs
- Use the GitHub issue tracker
- Check if the bug has already been reported
- Include detailed reproduction steps
- Provide system information (OS, browser version, etc.)

### 2. Suggest Features
- Open an issue with the "enhancement" label
- Clearly describe the feature and its use case
- Explain why this feature would be useful to most users

### 3. Submit Code
- Fork the repository
- Create a feature branch (`git checkout -b feature/AmazingFeature`)
- Write clean, documented code
- Add tests for new functionality
- Ensure all tests pass
- Submit a pull request

### 4. Improve Documentation
- Fix typos or clarify existing docs
- Add examples and tutorials
- Translate documentation to other languages

---

## 🔧 Development Setup

### Prerequisites
```bash
- Node.js >= 18.x
- Python >= 3.10
- PostgreSQL >= 14
- Redis >= 7.x
```

### Initial Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/CipherXGithub.git
cd CipherXGithub

# Install dependencies
cd bot && pip install -r requirements.txt
cd ../extension && npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run tests
npm test
python -m pytest
```

---

## 📝 Code Style Guidelines

### JavaScript/TypeScript
- Use ESLint and Prettier configurations provided
- Follow Airbnb JavaScript Style Guide
- Use async/await over promises
- Prefer functional programming patterns

```typescript
// ✅ Good
const getWalletBalance = async (address: string): Promise<number> => {
  const balance = await solanaConnection.getBalance(address);
  return balance / LAMPORTS_PER_SOL;
};

// ❌ Bad
function getWalletBalance(address) {
  return solanaConnection.getBalance(address).then(balance => {
    return balance / 1000000000;
  });
}
```

### Python
- Follow PEP 8 style guide
- Use type hints
- Document functions with docstrings

```python
# ✅ Good
async def fetch_whale_transactions(
    wallet_address: str,
    limit: int = 100
) -> List[Transaction]:
    """
    Fetch recent transactions for a whale wallet.
    
    Args:
        wallet_address: Solana wallet address to query
        limit: Maximum number of transactions to retrieve
        
    Returns:
        List of Transaction objects
    """
    pass

# ❌ Bad
def get_txs(addr, lim=100):
    pass
```

---

## 🧪 Testing

### Unit Tests
- Write tests for all new features
- Aim for >80% code coverage
- Use descriptive test names

```typescript
describe('WalletTracker', () => {
  it('should track whale wallet when balance exceeds threshold', async () => {
    // Test implementation
  });
  
  it('should emit alert when large transaction detected', async () => {
    // Test implementation
  });
});
```

### Integration Tests
- Test API endpoints
- Verify database interactions
- Mock external services (Helius, Chainlink)

---

## 📋 Pull Request Process

1. **Update Documentation**: Ensure README and docs reflect your changes
2. **Add Tests**: New features must include test coverage
3. **Update Changelog**: Add entry to CHANGELOG.md under "Unreleased"
4. **Lint & Format**: Run `npm run lint` and `npm run format`
5. **Commit Messages**: Use conventional commits format

### Commit Message Format
```
type(scope): subject

body

footer
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```bash
feat(bot): add whale wallet tracking alerts

Implemented real-time webhook subscriptions to Helius API for 
monitoring large wallet transactions. Alerts are sent via Telegram 
when transactions exceed configured thresholds.

Closes #123
```

---

## 🐛 Bug Report Template

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. macOS 13.0]
 - Browser: [e.g. Chrome 120]
 - Extension Version: [e.g. 1.2.0]
 - Bot Version: [e.g. 2.1.0]

**Additional context**
Add any other context about the problem here.
```

---

## ✨ Feature Request Template

```markdown
**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear description of any alternative solutions or features.

**Additional context**
Add any other context or screenshots about the feature request.

**Potential Implementation**
If you have ideas on how to implement this, share them here.
```

---

## 🔒 Security

**DO NOT** create public issues for security vulnerabilities. Instead, please email security@cipherx.io with:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

See [SECURITY.md](SECURITY.md) for our full security policy.

---

## 📜 Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inspiring community for all. Please be respectful and professional in all interactions.

### Our Standards
✅ **Do:**
- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards others

❌ **Don't:**
- Use sexualized language or imagery
- Make derogatory comments or personal attacks
- Harass others publicly or privately
- Publish others' private information without permission

---

## 📬 Questions?

- **General Questions**: Open a GitHub Discussion
- **Bug Reports**: Create a GitHub Issue
- **Feature Requests**: Create a GitHub Issue with "enhancement" label
- **Security Concerns**: Email security@cipherx.io
- **Other Inquiries**: Email support@cipherx.io

---

## 🎉 Recognition

Contributors will be:
- Listed in our [CONTRIBUTORS.md](CONTRIBUTORS.md) file
- Mentioned in release notes for significant contributions
- Eligible for CipherX swag and NFT airdrops
- Invited to our private contributor Discord channel

---

**Thank you for contributing to CipherX!** 🚀

Together, we're building the future of crypto trading intelligence.

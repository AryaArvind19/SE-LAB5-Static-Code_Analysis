### Reflection on Static Code Analysis

**1. Easiest and Hardest Fixes:**
The easiest fixes were formatting issues and removing unused imports flagged by Flake8.  
The hardest was handling the `eval()` warning — understanding why it was insecure and replacing it safely using `ast.literal_eval()`.

**2. False Positives:**
Pylint reported a missing docstring for simple functions, which wasn’t critical in a small script.  
Apart from that, all findings were valid and useful.

**3. Integrating Static Analysis in Development:**
I would integrate `flake8`, `pylint`, and `bandit` in a pre-commit hook or GitHub Actions CI workflow so every commit is checked automatically for quality and security.

**4. Improvements Observed:**
After fixing the issues:
- Code readability improved (snake_case, f-strings, blank lines)
- Security improved by removing `eval()` and adding safe file handling
- Maintainability increased with clear functions and proper exception handling

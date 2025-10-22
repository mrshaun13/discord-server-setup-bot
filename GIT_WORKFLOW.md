# 🔄 Git Workflow Quick Reference

## 📝 Daily Development Workflow

### 1. Check Status
```bash
git status
```
Shows what files have changed.

### 2. See Changes
```bash
git diff                    # See unstaged changes
git diff --staged           # See staged changes
```

### 3. Add Changes
```bash
git add .                   # Add all changes
git add setup_bot.py        # Add specific file
git add templates/          # Add specific directory
```

### 4. Commit Changes
```bash
git commit -m "Brief description of changes"
```

**Good commit messages:**
- `feat: Add new gaming template`
- `fix: Fix scaling bug in preview command`
- `docs: Update README with new examples`
- `refactor: Improve template loading performance`
- `test: Add tests for template_utils`

### 5. Push to GitHub
```bash
git push
```

---

## 🎯 Common Scenarios

### Scenario 1: Add New Feature
```bash
# Make your changes to files
git status                           # Check what changed
git add .                            # Stage all changes
git commit -m "feat: Add new feature X"
git push                             # Push to GitHub
```

### Scenario 2: Fix a Bug
```bash
# Fix the bug in your code
git add setup_bot.py
git commit -m "fix: Fix preview command error handling"
git push
```

### Scenario 3: Update Documentation
```bash
# Edit README.md or other docs
git add README.md
git commit -m "docs: Update installation instructions"
git push
```

### Scenario 4: Multiple Changes
```bash
# Made changes to multiple files
git add setup_bot.py templates.py
git commit -m "feat: Add template validation"
git add README.md
git commit -m "docs: Document template validation"
git push
```

---

## 🌿 Branching (For Larger Features)

### Create a Feature Branch
```bash
git checkout -b feature/new-template
# Make your changes
git add .
git commit -m "feat: Add new template"
git push -u origin feature/new-template
```

Then create a Pull Request on GitHub to merge into `main`.

### Switch Branches
```bash
git checkout main              # Switch to main
git checkout feature/xyz       # Switch to feature branch
```

### Merge Branch
```bash
git checkout main
git merge feature/new-template
git push
```

---

## 🔍 Viewing History

### See Commit History
```bash
git log                        # Full history
git log --oneline              # Compact view
git log --graph --oneline      # Visual graph
```

### See What Changed in a Commit
```bash
git show <commit-hash>
git show HEAD                  # Show last commit
```

---

## ⚠️ Undo Changes

### Undo Unstaged Changes
```bash
git checkout -- setup_bot.py   # Undo changes to file
git checkout -- .              # Undo all unstaged changes
```

### Unstage Files
```bash
git reset HEAD setup_bot.py    # Unstage specific file
git reset HEAD                 # Unstage all
```

### Undo Last Commit (Keep Changes)
```bash
git reset --soft HEAD~1
```

### Undo Last Commit (Discard Changes)
```bash
git reset --hard HEAD~1        # ⚠️ DANGEROUS - Loses changes\!
```

---

## 🔄 Syncing with GitHub

### Pull Latest Changes
```bash
git pull
```

### Fetch Without Merging
```bash
git fetch
git merge origin/main
```

---

## 📊 Useful Commands

### See Remote URL
```bash
git remote -v
```

### Change Remote URL
```bash
git remote set-url origin https://github.com/mrshaun13/new-repo.git
```

### See All Branches
```bash
git branch -a
```

### Delete Local Branch
```bash
git branch -d feature/old-feature
```

### Delete Remote Branch
```bash
git push origin --delete feature/old-feature
```

---

## 🎨 Commit Message Conventions

**Format**: `<type>: <description>`

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
git commit -m "feat: Add nonprofit template"
git commit -m "fix: Resolve scaling calculation bug"
git commit -m "docs: Add dry-run examples to README"
git commit -m "refactor: Optimize template loading"
git commit -m "test: Add unit tests for template_utils"
git commit -m "chore: Update dependencies"
```

---

## 🚀 Quick Commands

```bash
# Status and changes
git status
git diff

# Add and commit
git add .
git commit -m "Your message"

# Push to GitHub
git push

# Pull from GitHub
git pull

# View history
git log --oneline

# Undo unstaged changes
git checkout -- .
```

---

## 📝 .gitignore Patterns

Already configured in your `.gitignore`:
- ✅ `.env` files (secrets)
- ✅ `__pycache__` (Python cache)
- ✅ `venv/` (virtual environment)
- ✅ `*.log` (log files)
- ✅ IDE files

---

## 🎯 Best Practices

1. **Commit often** - Small, focused commits
2. **Write clear messages** - Explain what and why
3. **Pull before push** - Avoid conflicts
4. **Test before commit** - Ensure code works
5. **Don't commit secrets** - Use .gitignore
6. **Use branches** - For larger features
7. **Review before push** - Check `git diff`

---

## 🆘 Help

```bash
git help                       # General help
git help commit                # Help for specific command
git status                     # When in doubt, check status
```

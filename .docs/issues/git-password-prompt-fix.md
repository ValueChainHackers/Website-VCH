---
name: Fix Git Password Prompt on Push
about: Configure git to stop prompting for password when pushing to GitHub
title: '[HIGH PRIORITY] Fix Git Password Prompt on Push'
labels: 'task, infrastructure, high-priority'
assignees: ''
---

## 📋 Task Summary
Configure git credentials to stop prompting for password when pushing to GitHub repository.

## 🎯 Context

### Background
Currently, when pushing commits to GitHub, git prompts for username and password. This interrupts workflow and is unnecessary since authentication can be handled via SSH keys or credential helpers.

### Why This Matters
- **Workflow Efficiency:** Password prompts slow down development and deployment
- **Security:** Using SSH keys or credential helpers is more secure than typing passwords
- **Automation:** Prevents issues with automated scripts and CI/CD workflows
- **User Experience:** Eliminates friction in the development process

### Related Work
- Related to git configuration issues discovered during push error debugging
- May be related to HTTPS vs SSH remote URL configuration

## 🌍 Environment

### Technical Stack
- **Version Control:** Git 2.x
- **Repository Host:** GitHub
- **Remote URL:** Currently using HTTPS (likely cause of password prompts)
- **Operating System:** Linux (Ubuntu/Debian)

### Repository Structure
```
/home/chris/Documents/github/Website-VCH/
├── .git/
│   ├── config          # Git configuration
│   └── credentials     # Stored credentials (if using credential helper)
└── ...
```

### Current Git Configuration
Check with: `git config --list | grep -E "(url|credential|user)"`

### Critical Constraints
⚠️ **Security Considerations:**
- Never commit credentials to repository
- Use secure authentication methods
- Follow GitHub security best practices

## 🎯 Goal

### Primary Objective
Configure git to authenticate with GitHub without password prompts using one of these methods:
1. **SSH Keys** (Recommended) - Most secure, no password needed
2. **Git Credential Helper** - Caches credentials securely
3. **Personal Access Token** - Alternative to password

### Secondary Objectives
- [ ] Ensure configuration works for both push and pull operations
- [ ] Document the solution for future reference
- [ ] Test that automated workflows still function correctly

## ✅ Checklist

### Research & Diagnosis
- [ ] Check current git remote URL: `git remote -v`
- [ ] Identify if using HTTPS or SSH
- [ ] Check if SSH keys exist: `ls -la ~/.ssh/`
- [ ] Review current git credential configuration: `git config credential.helper`

### Option 1: Switch to SSH (RECOMMENDED)

#### Setup SSH Keys
- [ ] Generate SSH key if not exists: `ssh-keygen -t ed25519 -C "email@example.com"`
- [ ] Start SSH agent: `eval "$(ssh-agent -s)"`
- [ ] Add SSH key to agent: `ssh-add ~/.ssh/id_ed25519`
- [ ] Copy public key: `cat ~/.ssh/id_ed25519.pub`
- [ ] Add SSH key to GitHub account (Settings → SSH and GPG keys → New SSH key)
- [ ] Test SSH connection: `ssh -T git@github.com`

#### Update Remote URL
- [ ] Get current remote URL: `git remote get-url origin`
- [ ] Change to SSH URL: `git remote set-url origin git@github.com:ValueChainHackers/Website-VCH.git`
- [ ] Verify change: `git remote -v`

### Option 2: Use Git Credential Helper

#### Configure Credential Helper
- [ ] Check available credential helpers: `git credential-cache --help`
- [ ] Configure credential helper: `git config --global credential.helper cache`
- [ ] Or use store (less secure): `git config --global credential.helper store`
- [ ] Set cache timeout (in seconds): `git config --global credential.helper 'cache --timeout=3600'`

#### Generate Personal Access Token
- [ ] Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
- [ ] Click "Generate new token (classic)"
- [ ] Select scopes: `repo` (full control of private repositories)
- [ ] Copy token (save securely - won't be shown again)
- [ ] Use token as password on next git push

### Testing
- [ ] Make a test change: `echo "# Test" >> .docs/test.md`
- [ ] Stage change: `git add .docs/test.md`
- [ ] Commit: `git commit -m "Test: Verify git authentication"`
- [ ] Push without password prompt: `git push`
- [ ] Verify push succeeded on GitHub
- [ ] Clean up test file: `git rm .docs/test.md && git commit -m "Clean up test" && git push`

### Documentation
- [ ] Document chosen solution in `.docs/GIT_SETUP.md`
- [ ] Include troubleshooting steps
- [ ] Note any system-specific configurations

## 📝 Definition of Done

### Technical Quality
- [ ] Git push completes without password prompt
- [ ] Git pull works without authentication issues
- [ ] GitHub Actions workflows continue to function
- [ ] No credentials stored in plaintext in repository

### Security Quality
- [ ] Secure authentication method implemented (SSH or credential helper)
- [ ] No passwords or tokens committed to repository
- [ ] SSH keys (if used) are properly protected (600 permissions)
- [ ] Personal access token (if used) is stored securely

### Documentation Quality
- [ ] Solution documented in `.docs/GIT_SETUP.md`
- [ ] Steps to reproduce for new users included
- [ ] Troubleshooting guide provided

## 🔍 Task Case Details

### Scenario 1: HTTPS URL Without Credential Helper

**Current State:**
```bash
$ git remote -v
origin  https://github.com/ValueChainHackers/Website-VCH.git (fetch)
origin  https://github.com/ValueChainHackers/Website-VCH.git (push)
```

**Problem:** Git prompts for username/password on every push

**Solution:** Switch to SSH or configure credential helper

### Scenario 2: SSH Keys Not Configured

**Symptoms:**
- Using HTTPS URL
- No SSH keys in `~/.ssh/`
- Password prompt on push

**Solution:**
1. Generate SSH key pair
2. Add public key to GitHub
3. Change remote URL to SSH
4. Test connection

### Expected Commands

```bash
# Diagnosis
git remote -v
git config --list | grep credential

# SSH Solution
ssh-keygen -t ed25519 -C "christiaan_gerardo@hotmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub  # Copy this to GitHub
ssh -T git@github.com
git remote set-url origin git@github.com:ValueChainHackers/Website-VCH.git

# Credential Helper Solution
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=3600'
# Then push once with Personal Access Token as password
```

### Testing Scenarios

1. **Test Push Without Prompt**
   - Action: Make a small change and push
   - Expected Result: Push completes without asking for password

2. **Test Pull Operation**
   - Action: `git pull`
   - Expected Result: Pull completes without authentication prompt

3. **Test from Clean Shell**
   - Action: Open new terminal, navigate to repo, try to push
   - Expected Result: Authentication works without re-entering credentials

## 🚧 Blockers & Dependencies

### Potential Blockers
- SSH key generation requires user interaction
- Adding SSH key to GitHub requires GitHub account access
- May need to configure SSH config file for GitHub hostname

### Dependencies
- User must have GitHub account with write access to repository
- SSH client must be installed (`openssh-client`)
- Git must be version 2.0+ for modern credential helpers

## 📚 Resources & References

- **GitHub SSH Docs:** https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- **Git Credential Storage:** https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage
- **Personal Access Tokens:** https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
- **SSH Key Generation:** https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## 💬 Notes & Comments

### Recommended Approach

**SSH keys are the recommended solution because:**
1. Most secure - no passwords transmitted
2. Once configured, works seamlessly forever
3. Standard practice for GitHub authentication
4. No credential expiration issues

### Alternative: Credential Helper

Use if SSH is not possible for some reason:
- Credential helper caches credentials securely
- Timeout can be configured
- Less secure than SSH but better than entering password each time

### DO NOT Use `credential.helper store`

The `store` helper saves credentials in **plaintext** in `~/.git-credentials`. This is insecure and should be avoided.

## 🤖 AI Instructions

### What to Check First
1. Run `git remote -v` to see current remote URL
2. Check if SSH keys exist: `ls -la ~/.ssh/`
3. Determine which solution is appropriate

### Recommended Steps
1. **If no SSH keys exist:** Generate them and switch to SSH (most secure)
2. **If SSH keys exist but not on GitHub:** Add to GitHub and switch remote URL
3. **If SSH not possible:** Configure credential helper with cache

### Important Security Notes
- NEVER commit credentials or private keys
- SSH private keys should have 600 permissions
- Personal access tokens should be treated like passwords
- Document the solution but not the actual credentials

### If You Get Stuck
- SSH connection failing: Check `~/.ssh/config` for GitHub entry
- Permission denied: Verify SSH key is added to GitHub account
- Still prompting: Verify remote URL changed to SSH format (git@github.com:...)

### Success Criteria
Configuration is done when:
- Git push completes without any prompts
- Solution is secure (SSH or credential cache, not plaintext)
- Documentation exists for future setup
- User understands how to maintain/update credentials

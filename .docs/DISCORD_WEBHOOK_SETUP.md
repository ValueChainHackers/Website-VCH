# Discord Webhook Setup Guide

**Purpose:** Automatic notifications in Discord when the website is deployed
**Time Required:** 5 minutes
**Owner:** Christiaan Verhoef

---

## What This Does

Every time you push changes to GitHub and the website deploys successfully, a notification will automatically post to your Discord server showing:
- ✅ Deployment success message
- 📝 Commit message
- 👤 Who made the changes
- 🔗 Links to the commit and live website

---

## Step 1: Create Discord Webhook

### In Discord:

1. Open your VCH Discord server
2. Go to **Server Settings** (gear icon)
3. Click **Integrations** in the left sidebar
4. Click **Webhooks**
5. Click **New Webhook** button
6. Configure the webhook:
   - **Name:** `VCH Deployment Bot`
   - **Channel:** Select the channel for notifications (recommend `#announcements` or create `#website-updates`)
   - **Avatar:** Optional - upload VCH logo
7. Click **Copy Webhook URL** button
8. **Save your webhook URL** - you'll need it in the next step

**Webhook URL format:**
```
https://discord.com/api/webhooks/1234567890/ABCdefGHIjklMNOpqrsTUVwxyz...
```

---

## Step 2: Add Webhook to GitHub Secrets

### In GitHub:

1. Go to https://github.com/ValueChainHackers/Website-VCH
2. Click **Settings** tab (top navigation)
3. Click **Secrets and variables** in left sidebar
4. Click **Actions**
5. Click **New repository secret** button
6. Add the secret:
   - **Name:** `DISCORD_WEBHOOK`
   - **Secret:** Paste the webhook URL you copied from Discord
7. Click **Add secret**

**IMPORTANT:** Never commit the webhook URL directly to your code! Always use GitHub Secrets.

---

## Step 3: Test the Webhook

### Option A: Make a small change

1. Edit any file (e.g., add a comment to `README.md`)
2. Commit and push:
   ```bash
   git add .
   git commit -m "test: verify Discord webhook"
   git push
   ```
3. Wait 2-3 minutes for GitHub Pages to deploy
4. Check your Discord channel for the notification

### Option B: Manually trigger (if you want to test without deploying)

1. Go to GitHub repository → **Actions** tab
2. Find the "Discord Deployment Notification" workflow
3. Click **Run workflow** (if available)

---

## What The Notification Looks Like

```
🚀 Website Deployed Successfully
The VCH website has been updated and deployed to production.

📝 Commit: a1b2c3d
👤 Author: Christiaan Verhoef
🌐 Website: valuechainhackers.xyz
💬 Message: feat: add Discord widget to homepage
```

---

## Choosing The Right Discord Channel

### Option 1: Use #announcements
**Pros:**
- Everyone sees deployments
- Good for transparency

**Cons:**
- Can be noisy if deploying frequently

### Option 2: Create #website-updates
**Pros:**
- Dedicated channel for technical updates
- Keeps announcements clean
- Team members can choose to follow/ignore

**Cons:**
- Need to create new channel

### Option 3: Use #general
**Pros:**
- Already exists

**Cons:**
- Gets buried in other messages

**Recommendation:** Create `#website-updates` channel for clean notifications

---

## Customizing The Message

The webhook message is defined in `.github/workflows/discord-notify.yml`

### Change the message text:
Find the `description` field (line ~30):
```yaml
\"description\": \"The VCH website has been updated and deployed to production.\",
```

Change to whatever you want:
```yaml
\"description\": \"New changes are live on the website! 🎉\",
```

### Change the color:
Find the `color` field (line ~29):
```yaml
\"color\": 8245565,
```

Colors in decimal format:
- Green (success): `3066993`
- Yellow (warning): `15844367`
- Blue (info): `3447003`
- Red (error): `15158332`
- VCH Green: `8245565` (current)

### Add more fields:
```yaml
{
  \"name\": \"⏱️ Deploy Time\",
  \"value\": \"$(date -u +%H:%M) UTC\",
  \"inline\": true
}
```

---

## Troubleshooting

### No notification appears

**Check 1: Is the secret configured?**
```bash
# GitHub → Settings → Secrets → Actions
# Should see: DISCORD_WEBHOOK
```

**Check 2: Did the deployment succeed?**
```bash
# GitHub → Actions tab
# Check if "pages-build-deployment" workflow succeeded
```

**Check 3: Is the webhook URL correct?**
- Test the webhook manually:
```bash
curl -H "Content-Type: application/json" \
-X POST \
-d '{"content":"Test message from VCH Bot"}' \
YOUR_WEBHOOK_URL
```
- You should see a message in Discord

**Check 4: Was the webhook deleted?**
- Go to Discord Server Settings → Integrations → Webhooks
- Check if "VCH Deployment Bot" still exists

### Notification shows but formatting is broken

- Check the JSON syntax in `discord-notify.yml`
- Make sure all quotes are properly escaped
- Test locally with `curl` first

### Getting errors in GitHub Actions

1. Go to GitHub → Actions tab
2. Click on failed workflow run
3. Click on "notify" job
4. Check the error message
5. Common issues:
   - Malformed JSON → Fix escaping
   - Webhook URL invalid → Re-create secret
   - Rate limited → Discord allows 30 requests/minute

---

## Security Notes

### ✅ DO:
- Store webhook URL in GitHub Secrets
- Use repository secrets (not environment secrets)
- Regenerate webhook if accidentally exposed
- Limit who can edit GitHub repository settings

### ❌ DON'T:
- Commit webhook URL to code
- Share webhook URL publicly
- Use the same webhook for multiple purposes
- Give webhook admin permissions in Discord

---

## Advanced: Multiple Webhooks

If you want different notifications for different events:

### Create separate webhooks:
1. `DISCORD_WEBHOOK_DEPLOY` - for deployments
2. `DISCORD_WEBHOOK_ERRORS` - for build failures
3. `DISCORD_WEBHOOK_PR` - for pull requests

### Use conditional logic:
```yaml
- name: Notify on success
  if: success()
  env:
    WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_DEPLOY }}

- name: Notify on failure
  if: failure()
  env:
    WEBHOOK: ${{ secrets.DISCORD_WEBHOOK_ERRORS }}
```

---

## Disabling Notifications

### Temporarily (for batch updates):
1. Go to Discord webhook settings
2. **Delete** the webhook
3. Make your updates
4. **Re-create** the webhook when done

### Permanently:
1. GitHub → Settings → Secrets → Actions
2. Delete `DISCORD_WEBHOOK` secret
3. The workflow will skip notifications but won't fail

**Note:** The workflow checks if the secret exists and gracefully skips if not configured.

---

## Quick Reference

```yaml
# Workflow triggers on successful deployment
on:
  workflow_run:
    workflows: ["pages-build-deployment"]
    types: [completed]

# Check if DISCORD_WEBHOOK secret exists
if [ -z "$DISCORD_WEBHOOK" ]; then
  echo "Secret not configured, skipping..."
  exit 0
fi

# Post to Discord
curl -X POST $DISCORD_WEBHOOK -d '{"content":"Message"}'
```

**Webhook URL location:** GitHub Settings → Secrets → DISCORD_WEBHOOK
**Workflow file:** `.github/workflows/discord-notify.yml`
**Discord webhook settings:** Server Settings → Integrations → Webhooks

---

**Setup Time:** 5 minutes
**Cost:** Free
**Difficulty:** Easy
**Dependencies:** Discord server, GitHub repository with Actions enabled

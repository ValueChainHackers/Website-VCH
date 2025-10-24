# EmailJS Setup Guide for Contact Form

**Purpose:** Make the contact form functional so visitors can actually send messages
**Service:** EmailJS (Free tier: 200 emails/month)
**Time Required:** 15-20 minutes
**Owner:** Christiaan Verhoef

---

## Why EmailJS?

- ✅ **Free tier** (200 emails/month)
- ✅ **No backend required** (works with static sites)
- ✅ **Easy setup** (just JavaScript)
- ✅ **Reliable** (99.9% uptime)
- ✅ **Spam protection** included

---

## Step 1: Create EmailJS Account

1. Go to https://www.emailjs.com/
2. Click "Sign Up" (top right)
3. Choose "Sign up with Google" or enter email
4. Verify your email address
5. Log in to dashboard

**Cost:** Free (no credit card needed)

---

## Step 2: Add Email Service

1. In EmailJS dashboard, click "Email Services"
2. Click "Add New Service"
3. Choose your email provider:
   - **Gmail** (easiest if you have Google account)
   - **Outlook** (if you use Outlook/Hotmail)
   - **Custom SMTP** (for info@valuechainhackers.xyz if you have SMTP credentials)

### Option A: Using Gmail (Recommended for testing)

1. Select "Gmail"
2. Click "Connect Account"
3. Log in with your Gmail account
4. Allow EmailJS to send emails
5. Service ID will be auto-generated (e.g., `service_abc123`)
6. Click "Create Service"

### Option B: Using Custom SMTP (for info@valuechainhackers.xyz)

1. Select "Custom SMTP Server"
2. Enter SMTP details from your email provider:
   ```
   SMTP Server: [your mail server]
   Port: 587 (or 465 for SSL)
   Username: info@valuechainhackers.xyz
   Password: [your email password]
   ```
3. Test connection
4. Save service

**Save your Service ID** (you'll need it later)

---

## Step 3: Create Email Template

1. In dashboard, click "Email Templates"
2. Click "Create New Template"
3. Template ID will be auto-generated (e.g., `template_xyz789`)

### Template Settings:

**Template Name:** VCH Contact Form

**Subject:**
```
New Contact Form Submission from {{user_name}}
```

**Content (HTML):**
```html
<h2>New Contact Form Message</h2>

<p><strong>From:</strong> {{user_name}}</p>
<p><strong>Email:</strong> {{user_email}}</p>
<p><strong>Subject:</strong> {{message_subject}}</p>

<h3>Message:</h3>
<p>{{message}}</p>

<hr>
<p><small>Sent from VCH Website Contact Form</small></p>
<p><small>Reply directly to {{user_email}}</small></p>
```

**To Email:**
```
info@valuechainhackers.xyz
```

**From Name:**
```
VCH Website
```

**Reply To:**
```
{{user_email}}
```

4. Click "Save"
5. **Test the template** (use the test button)
6. **Save your Template ID** (you'll need it)

---

## Step 4: Get Public Key

1. In dashboard, click "Account" (top right)
2. Click "API Keys"
3. Copy your **Public Key** (looks like: `YOUR_PUBLIC_KEY_HERE`)
4. **Save this key** - you'll add it to the website

---

## Step 5: Update Website Code

The code is already prepared in `index.html`. You just need to add your keys.

### Find this section in `index.html` (around line 580):

```html
<!-- EMAILJS CONFIGURATION - ADD YOUR KEYS HERE -->
<script>
    // TODO: Replace with your EmailJS keys
    const EMAILJS_PUBLIC_KEY = 'YOUR_PUBLIC_KEY';
    const EMAILJS_SERVICE_ID = 'YOUR_SERVICE_ID';
    const EMAILJS_TEMPLATE_ID = 'YOUR_TEMPLATE_ID';
</script>
```

### Replace with your actual keys:

```html
<!-- EMAILJS CONFIGURATION -->
<script>
    const EMAILJS_PUBLIC_KEY = 'abc123xyz...';  // From Step 4
    const EMAILJS_SERVICE_ID = 'service_abc123'; // From Step 2
    const EMAILJS_TEMPLATE_ID = 'template_xyz789'; // From Step 3
</script>
```

**That's it!** The form will now work.

---

## Step 6: Test the Contact Form

1. Go to your website
2. Fill out the contact form:
   - Name: Test User
   - Email: your-email@example.com
   - Subject: Test Message
   - Message: Testing the new contact form!
3. Click "Send Message"
4. You should see: "Message sent successfully!"
5. Check `info@valuechainhackers.xyz` inbox
6. You should receive the test email

---

## Troubleshooting

### Error: "Failed to send message"

**Possible causes:**
1. **Keys are wrong** - Double-check Public Key, Service ID, Template ID
2. **Service not connected** - Go to EmailJS → Email Services → check status
3. **Template doesn't exist** - Go to EmailJS → Email Templates → verify
4. **Rate limit hit** - Free tier: 200 emails/month

**Debug steps:**
```javascript
// Open browser console (F12)
// Look for error messages
// Common errors:
// - "Invalid public key" → Check EMAILJS_PUBLIC_KEY
// - "Service not found" → Check EMAILJS_SERVICE_ID
// - "Template not found" → Check EMAILJS_TEMPLATE_ID
```

### Email not received

1. **Check spam folder** first
2. **Verify "To Email"** in template settings
3. **Test template** directly in EmailJS dashboard
4. **Check EmailJS logs** (Dashboard → Email Logs)

### Form doesn't submit

1. **Check browser console** for errors (F12)
2. **Verify EmailJS script** is loaded
3. **Check form validation** (all required fields filled?)

---

## EmailJS Dashboard Quicklinks

- **Dashboard:** https://dashboard.emailjs.com/
- **Email Services:** https://dashboard.emailjs.com/admin
- **Email Templates:** https://dashboard.emailjs.com/admin/templates
- **Email Logs:** https://dashboard.emailjs.com/admin/logs
- **Documentation:** https://www.emailjs.com/docs/

---

## Security Best Practices

### ✅ DO:
- Use EmailJS Public Key (safe to expose in client-side code)
- Set rate limiting in EmailJS dashboard
- Enable CAPTCHA if spam becomes an issue
- Monitor email logs regularly

### ❌ DON'T:
- Don't expose your email password
- Don't use EmailJS Private Key in client code
- Don't disable spam protection
- Don't share your EmailJS account credentials

---

## Rate Limits

### Free Tier (Current):
- 200 emails per month
- 1 email service
- Unlimited email templates
- EmailJS branding in emails

### Paid Tier (if needed later):
- $15/month: 1,000 emails
- $30/month: 5,000 emails
- No branding
- Priority support

**Current usage:** Estimate 10-20 contacts/month = well within free tier

---

## Alternative: If EmailJS Doesn't Work

### Plan B: Formspree
1. Go to https://formspree.io/
2. Free tier: 50 submissions/month
3. Update form action: `action="https://formspree.io/f/YOUR_FORM_ID"`

### Plan C: Google Forms
1. Create Google Form
2. Embed in website
3. Responses go to Google Sheets

### Plan D: Netlify Forms (if you migrate hosting)
1. Add `netlify` attribute to form
2. Automatic form handling
3. 100 submissions/month free

---

## Maintenance

### Monthly Tasks:
- [ ] Check EmailJS usage (Dashboard → Statistics)
- [ ] Review email logs for spam
- [ ] Test contact form still works
- [ ] Check inbox for missed messages

### When to Upgrade:
- If you hit 200 emails/month consistently
- If you need custom branding
- If you want priority support

---

## Quick Reference

```javascript
// EmailJS Configuration (already in index.html)
const EMAILJS_PUBLIC_KEY = 'YOUR_KEY_HERE';
const EMAILJS_SERVICE_ID = 'service_xxxxx';
const EMAILJS_TEMPLATE_ID = 'template_xxxxx';

// Form submit handler (already implemented)
emailjs.sendForm(
    EMAILJS_SERVICE_ID,
    EMAILJS_TEMPLATE_ID,
    '#contact-form',
    EMAILJS_PUBLIC_KEY
);
```

---

**Setup Time:** 15-20 minutes
**Cost:** Free
**Difficulty:** Easy
**Next Steps:** See index.html for implementation details

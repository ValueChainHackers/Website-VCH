# Newsletter Integration Guide

The VCH website has a newsletter signup form that currently stores subscriptions in browser localStorage. To connect it to a real newsletter service, follow one of the integration options below.

## Current Implementation

Location: `_pages/contact.md`
- Modal popup with email capture form
- Interest selection (projects, workshops, insights)
- localStorage fallback for testing
- Success/confirmation message

## Integration Options

### Option 1: Mailchimp (Recommended for Beginners)

**Pros:** Free up to 500 subscribers, easy setup, powerful automation
**Cons:** Branding on emails (free tier)

**Setup Steps:**
1. Create free account at https://mailchimp.com
2. Create an audience
3. Go to Audience → Signup forms → Embedded forms
4. Copy the embedded form code
5. In `_pages/contact.md`, replace the `handleNewsletterSubmit` function with:

```javascript
function handleNewsletterSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const email = form.email.value;
    const name = form.name.value;

    // Mailchimp JSONP subscription
    const url = 'https://yourdomain.us1.list-manage.com/subscribe/post-json?u=YOUR_USER_ID&id=YOUR_LIST_ID&c=?';
    const data = {
        EMAIL: email,
        FNAME: name,
        b_YOUR_USER_ID_YOUR_LIST_ID: '' // honeypot
    };

    fetch(url + '&' + new URLSearchParams(data))
        .then(() => {
            form.classList.add('hidden');
            document.getElementById('newsletter-success').classList.remove('hidden');
        })
        .catch(console.error);
}
```

6. Replace `YOUR_USER_ID` and `YOUR_LIST_ID` with values from Mailchimp

---

### Option 2: Buttondown (Recommended for Simplicity)

**Pros:** Minimalist, Markdown-based, no ads, elegant emails
**Cons:** Free tier limited to 100 subscribers

**Setup Steps:**
1. Create account at https://buttondown.email
2. Go to Settings → Embedding
3. Copy your unique URL
4. Replace `handleNewsletterSubmit`:

```javascript
function handleNewsletterSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const email = form.email.value;

    fetch('https://api.buttondown.email/v1/subscribers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            metadata: {
                name: form.name.value,
                interests: Array.from(form.querySelectorAll('input[name="interests"]:checked')).map(cb => cb.value).join(', ')
            }
        })
    })
    .then(response => {
        form.classList.add('hidden');
        document.getElementById('newsletter-success').classList.remove('hidden');
    })
    .catch(console.error);
}
```

---

### Option 3: ConvertKit

**Pros:** Creator-focused, excellent automation, tag-based organization
**Cons:** Paid after 1,000 subscribers

**Setup Steps:**
1. Create account at https://convertkit.com
2. Create a form
3. Go to form settings → Embed
4. Get your Form ID
5. Replace `handleNewsletterSubmit`:

```javascript
function handleNewsletterSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formId = 'YOUR_FORM_ID'; // From ConvertKit

    fetch(`https://api.convertkit.com/v3/forms/${formId}/subscribe`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: form.email.value,
            first_name: form.name.value
        })
    })
    .then(() => {
        form.classList.add('hidden');
        document.getElementById('newsletter-success').classList.remove('hidden');
    })
    .catch(console.error);
}
```

---

### Option 4: Self-Hosted (Listmonk)

**Pros:** Complete control, no limits, open-source
**Cons:** Requires server setup and maintenance

**Setup Steps:**
1. Deploy Listmonk: https://listmonk.app/docs/installation/
2. Create a subscriber list
3. Get API credentials
4. Create API endpoint or use direct integration
5. Update JavaScript to call your API

---

## Testing Newsletter Signup

Current implementation stores to localStorage for testing:

```javascript
// Check subscribers in browser console:
JSON.parse(localStorage.getItem('newsletter_subscribers'))

// Clear test subscribers:
localStorage.removeItem('newsletter_subscribers')
```

## Recommended Next Steps

1. **Choose a service** based on your needs:
   - **Just starting out?** → Mailchimp or Buttondown
   - **Want simplicity?** → Buttondown
   - **Creator focus?** → ConvertKit
   - **Full control?** → Listmonk

2. **Set up double opt-in** for GDPR compliance

3. **Create welcome email** automation

4. **Plan newsletter cadence** (weekly, monthly, etc.)

5. **Prepare first newsletter content**

## Newsletter Content Ideas

- Monthly digest of new projects
- Workshop announcements
- Supply chain insights and trends
- Student success stories
- Partner spotlights
- Open-source tool releases
- Job opportunities in supply chain

## Privacy & Compliance

- Add privacy policy link to signup form
- Implement double opt-in
- Easy unsubscribe in every email
- Store minimal data
- GDPR-compliant service (EU-based or compliant)

## Questions?

Contact the VCH team at info@valuechainhackers.xyz

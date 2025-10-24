# Event Registration System Guide

## Overview

The VCH website uses Google Forms for event registration, providing a professional, user-friendly way to collect attendee information without requiring backend infrastructure.

## System Architecture

### Components:
1. **Google Forms** - Registration form hosted on Google
2. **Modal Dialog** - JavaScript-powered popup on website
3. **Discord Integration** - Automatic notifications when someone registers
4. **Confirmation Emails** - Automatic responses via Google Forms

---

## Setup Instructions

### Step 1: Create Google Form

1. **Go to Google Forms**
   - Visit: https://forms.google.com/
   - Sign in with VCH Google account

2. **Create New Form**
   - Click "+ Blank" to create new form
   - Name it: "VCH Event Registration - [Event Name]"

3. **Add Required Fields:**
   ```
   ✅ Name (Short answer, Required)
   ✅ Email (Short answer, Required, Email validation)
   ✅ Organization/University (Short answer, Optional)
   ✅ Role (Multiple choice, Required)
      - Student
      - Researcher
      - Business Professional
      - Other
   ✅ Dietary Requirements (Short answer, Optional)
   ✅ How did you hear about us? (Multiple choice, Optional)
      - LinkedIn
      - Discord
      - University
      - Friend/Colleague
      - Other
   ```

4. **Configure Form Settings:**
   - Click ⚙️ (Settings) icon
   - **General:**
     - ✅ Limit to 1 response (requires sign-in)
     - ✅ Edit after submit (optional)
   - **Presentation:**
     - ✅ Show progress bar
     - ✅ Shuffle question order (unchecked)
     - Confirmation message: "Thank you! You're registered for [Event Name]. We've sent a confirmation email to your address."
   - **Responses:**
     - ✅ Collect email addresses
     - ✅ Send respondents a copy of their response

5. **Get Embeddable Link:**
   - Click "Send" button (top right)
   - Click `< >` (Embed HTML) tab
   - Copy the iframe URL (between `src="` and `"`)
   - Example: `https://docs.google.com/forms/d/e/FORM_ID/viewform?embedded=true`

6. **Shorten the URL (Optional):**
   - Use the "Link" tab in Send dialog
   - Click "Shorten URL"
   - Use this for QR codes and social media

### Step 2: Update Website Code

Update `events.html` with the form URL:

```html
<!-- Replace mailto link with modal trigger -->
<button onclick="openRegistrationModal('FORM_ID_HERE', 'Event Name')"
        class="block bg-vch-green text-white px-6 py-3 rounded-lg font-semibold text-center hover:bg-green-600 transition-all">
    <i class="fas fa-ticket-alt mr-2"></i>Register Now
</button>
```

The modal will automatically open with the Google Form embedded.

### Step 3: Set Up Email Notifications

1. **In Google Forms:**
   - Click "Responses" tab
   - Click ⋮ (three dots)
   - Select "Get email notifications for new responses"
   - Add email: info@valuechainhackers.xyz

2. **Auto-Response to Registrants:**
   - Already enabled in Settings → "Send respondents a copy"
   - They'll receive confirmation at their email

### Step 4: Discord Integration (Optional)

Connect form responses to Discord channel:

1. **Install Google Forms Discord Integration:**
   - Option A: Use Zapier (free tier: 100 tasks/month)
   - Option B: Use Google Apps Script (unlimited, requires setup)

2. **Zapier Method (Easiest):**
   - Go to https://zapier.com/
   - Create new Zap
   - Trigger: Google Forms → New Response
   - Action: Discord → Send Channel Message
   - Message template:
     ```
     🎟️ New Event Registration!

     **Name:** {{Name}}
     **Email:** {{Email}}
     **Role:** {{Role}}
     **Event:** VCH Final Event
     **Time:** {{Timestamp}}
     ```

3. **Apps Script Method (Free):**
   - In Google Form, click ⋮ → Script editor
   - Paste webhook script (see below)
   - Set trigger: On form submit

**Apps Script Code:**
```javascript
function onFormSubmit(e) {
  var webhookUrl = 'YOUR_DISCORD_WEBHOOK_URL';

  var response = e.response;
  var items = response.getItemResponses();

  var name = items[0].getResponse();
  var email = items[1].getResponse();
  var role = items[3].getResponse();

  var payload = {
    "embeds": [{
      "title": "🎟️ New Event Registration",
      "color": 8245565,
      "fields": [
        {"name": "Name", "value": name, "inline": true},
        {"name": "Role", "value": role, "inline": true},
        {"name": "Email", "value": email, "inline": false}
      ],
      "timestamp": new Date().toISOString()
    }]
  };

  var options = {
    'method': 'post',
    'contentType': 'application/json',
    'payload': JSON.stringify(payload)
  };

  UrlFetchApp.fetch(webhookUrl, options);
}
```

---

## Managing Registrations

### View Responses

**In Google Forms:**
1. Click "Responses" tab
2. View summary or individual responses
3. Export to Google Sheets for analysis

**Export Data:**
1. Click ⋮ (three dots) in Responses tab
2. "Select response destination"
3. Choose "Create a new spreadsheet"
4. Link: Google Sheets for advanced filtering/analysis

### Download Attendee List

1. Open linked Google Sheet
2. File → Download → CSV or Excel
3. Use for:
   - Name badges
   - Check-in list
   - Certificate generation

### Close Registration

When event is full or ended:
1. Go to Google Form
2. Click "Responses" tab
3. Toggle "Accepting responses" to OFF
4. Custom message: "Registration for this event is now closed. Stay tuned for future events!"

---

## Event-Specific Forms

### Current Events

| Event | Form ID | Status | Deadline |
|-------|---------|--------|----------|
| VCH Final Event (Oct 30) | TBD | Not Created | Oct 29 |
| AI Workshop Series | TBD | Not Created | TBA |

### Form Template

Save time by duplicating forms:
1. Open existing form
2. Click ⋮ → Make a copy
3. Rename and update event details
4. Update website with new Form ID

---

## Website Implementation

### Modal System

The website has a built-in modal system that displays Google Forms in a popup:

```javascript
// Function already in events.html
function openRegistrationModal(formId, eventName) {
    // Creates modal overlay
    // Embeds Google Form iframe
    // Handles close button
}
```

### How to Update Event Registration Links

**Find the event in events.html:**
```html
<a href="mailto:..." class="...">Register Now</a>
```

**Replace with modal trigger:**
```html
<button onclick="openRegistrationModal('1FAIpQLSexample123', 'VCH Final Event')"
        class="block bg-vch-green text-white px-6 py-3 rounded-lg font-semibold text-center hover:bg-green-600 transition-all">
    <i class="fas fa-ticket-alt mr-2"></i>Register Now
</button>
```

**Parameters:**
- `formId`: Google Form ID from embed URL
- `eventName`: Display name in modal header

---

## Troubleshooting

### Form Not Loading

**Problem:** Modal shows but form doesn't appear

**Solutions:**
1. Check if Form ID is correct
2. Ensure form is set to "Accepting responses"
3. Check browser console for errors
4. Try opening form URL directly in new tab

### Confirmation Emails Not Sending

**Problem:** Registrants don't receive confirmation

**Solutions:**
1. Verify "Send respondents a copy" is enabled in Settings
2. Check spam folder
3. Ensure email field is marked as "Email" type in form
4. Test by submitting form yourself

### Discord Notifications Not Working

**Problem:** No message appears in Discord

**Solutions:**
1. Verify webhook URL is correct
2. Check Apps Script execution logs
3. Ensure trigger is set up correctly
4. Test webhook with curl:
   ```bash
   curl -X POST YOUR_WEBHOOK_URL \
   -H "Content-Type: application/json" \
   -d '{"content": "Test message"}'
   ```

---

## Best Practices

### Before Event

- [ ] Create form 2-3 weeks before event
- [ ] Test registration flow yourself
- [ ] Set up Discord notifications
- [ ] Add event to Discord calendar
- [ ] Share registration link on social media

### During Registration Period

- [ ] Monitor responses daily
- [ ] Respond to questions in form comments
- [ ] Send reminder 1 week before event
- [ ] Close registration 1 day before (or when full)

### After Event

- [ ] Close form to new responses
- [ ] Send thank you email to attendees
- [ ] Export data for records
- [ ] Collect feedback via follow-up form

---

## Alternative: Discord Events

For informal meetups and workshops, use Discord's built-in Events feature:

### How to Create Discord Event

1. **In Discord Server:**
   - Navigate to #events channel
   - Click "Create Event" button (calendar icon)

2. **Event Details:**
   - Name: "VCH AI Workshop: Demand Forecasting"
   - Description: Include agenda and requirements
   - Location: "Windesheim Campus 2" or "Voice Channel"
   - Start Time: Select date/time
   - Cover Image: Upload event banner

3. **Benefits:**
   - Automatic reminders to interested members
   - RSVP tracking
   - Integration with Discord calendar
   - No external tools needed

### When to Use Discord vs Google Forms

| Use Discord Events | Use Google Forms |
|-------------------|------------------|
| Internal VCH workshops | Public events |
| Informal meetups | Events requiring details (dietary, etc.) |
| Quick polls | Professional record-keeping |
| < 50 people | > 50 people |
| VCH members only | External attendees |

---

## Security & Privacy

### Data Protection

- Google Forms is GDPR compliant
- Only collect necessary information
- Don't share attendee emails publicly
- Delete responses after 1 year

### Access Control

- Only VCH team leads should have form edit access
- Use "Restrict to Windesheim organization" if possible
- Don't share form edit link publicly

---

## Quick Reference

### Form IDs

Extract Form ID from Google Forms URL:
```
https://docs.google.com/forms/d/1FAIpQLSexample123/edit
                                   ^^^^^^^^^^^^^^^^
                                   This is your Form ID
```

### Embed URL Format

```
https://docs.google.com/forms/d/e/FORM_ID/viewform?embedded=true
```

### Modal Trigger Code

```html
<button onclick="openRegistrationModal('FORM_ID', 'Event Name')"
        class="btn">
    Register Now
</button>
```

---

## Support

**Questions?** Contact:
- Technical issues: c.verhoef@windesheim.nl
- Event coordination: m.bouillon@windesheim.nl
- General inquiries: info@valuechainhackers.xyz

**Resources:**
- [Google Forms Help](https://support.google.com/docs/topic/9055404)
- [Zapier Google Forms Integration](https://zapier.com/apps/google-forms/integrations)
- [Discord Webhooks Guide](https://support.discord.com/hc/en-us/articles/228383668)

---

**Last Updated:** October 24, 2025
**Version:** 1.0
**Author:** Claude (AI Assistant)

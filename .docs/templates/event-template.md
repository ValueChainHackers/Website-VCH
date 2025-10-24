---
# =============================================================================
# EVENT TEMPLATE
# For VCH events: brainstorming sessions, roast days, workshops, presentations, conferences
# Version: 1.0 | Last Updated: 2025-10-24
# =============================================================================

# [REQUIRED] Event name
# Example: "Autumn 2025 Brainstorming Session" or "Spring 2025 Roast Day"
title: "Event Name Here"

# [REQUIRED] Brief description for event cards and SEO
# Guidelines: 1-2 sentences, <160 characters, focus on event purpose and highlights
# Example: "Student-led brainstorming session exploring supply chain challenges and innovative solutions for sustainability"
description: "Brief event description here"

# [REQUIRED] Event status - Always "Completed" unless using for upcoming events
# Options: "Upcoming" | "Completed" | "Cancelled"
status: "Completed"

# [REQUIRED] Event category - Always "Event" for this template
category: "Event"

# [REQUIRED] Event type - Select most appropriate
# Options: "Workshop" | "Presentation" | "Brainstorming" | "Conference" | "Roast Day" |
#          "Hackathon" | "Networking" | "Training" | "Guest Lecture"
event_type: "Event Type"

# [REQUIRED] Unique URL path for this event page
# Format: /events/event-name-yyyy-mm-dd/ (lowercase, hyphens only)
# Example: /events/autumn-brainstorming-2025-10-02/
permalink: /events/event-name-yyyy-mm-dd/

# =============================================================================
# EVENT DETAILS
# =============================================================================

# [REQUIRED] Event date
# Format: "YYYY-MM-DD" for precise date, or "Month DD, YYYY"
# Example: "2025-10-02" or "October 2, 2025"
event_date: "YYYY-MM-DD"

# [OPTIONAL] Event start and end times
# Format: "HH:MM AM/PM" in local time
# Example: "09:00 AM - 05:00 PM"
start_time: ""
end_time: ""

# [OPTIONAL] Event duration (if multi-day)
# Example: "2 days" or "October 2-3, 2025"
duration: ""

# [REQUIRED] Event location
# Options: Specific venue address OR "Virtual" OR "Hybrid"
# Example: "Windesheim Zwolle, Room A101" or "Virtual (Zoom)"
location: "Location Here"

# [OPTIONAL] Venue details
venue:
  name: "Venue Name"
  address: "Street Address"
  city: "City"
  country: "Country"
  room: "Room Number or Name"
  capacity: 0 # Maximum attendees

# [OPTIONAL] Virtual event details
virtual:
  platform: "" # Example: "Zoom", "Microsoft Teams", "Google Meet"
  link: "" # Only if publicly shareable
  recording_available: false

# =============================================================================
# PARTICIPANTS
# =============================================================================

# [REQUIRED] Estimated or exact number of attendees
# Format: Number (if exact) or "~X" (if approximate)
# Example: 25 or "~30 participants"
attendees: 0

# [OPTIONAL] Attendee types/breakdown
# Example: ["15 students", "5 faculty", "3 industry partners", "2 VCH staff"]
attendee_breakdown:
  - "Group 1: Number"
  - "Group 2: Number"

# [OPTIONAL] Key organizers
organizers:
  - "Name 1 (Organization/Role)"
  - "Name 2 (Organization/Role)"

# [OPTIONAL] Facilitators or hosts
facilitators:
  - "Name (Role)"

# [OPTIONAL] Guest speakers or presenters
speakers:
  - name: "Speaker Name"
    title: "Job Title"
    organization: "Organization"
    topic: "Presentation Topic"
    bio: "Brief bio or description"

# [OPTIONAL] Student presenters (for Roast Days, final presentations)
student_presenters:
  - name: "Student Name"
    project: "Project Name"
    team: "Team Members"

# =============================================================================
# EVENT CONTENT
# =============================================================================

# [OPTIONAL] Event goals or objectives
# What was the event trying to achieve?
objectives:
  - "Objective 1"
  - "Objective 2"

# [OPTIONAL] Event agenda or schedule
agenda:
  - time: "09:00 AM"
    activity: "Registration & Coffee"
    description: "Welcome and networking"

  - time: "09:30 AM"
    activity: "Opening Remarks"
    description: "Introduction by [Name]"

  - time: "10:00 AM"
    activity: "Session 1: Topic Name"
    description: "Description of session content"

  - time: "12:00 PM"
    activity: "Lunch Break"
    description: ""

  - time: "01:00 PM"
    activity: "Session 2: Topic Name"
    description: ""

# [OPTIONAL] Key topics discussed
topics:
  - "Topic 1"
  - "Topic 2"
  - "Topic 3"

# [OPTIONAL] Activities or workshops
activities:
  - name: "Activity Name"
    description: "What participants did"
    duration: "Time spent"

# =============================================================================
# EVENT RESOURCES
# =============================================================================

# [OPTIONAL] Event presentations or materials
# Store files in /assets/documents/events/event-name/
presentations:
  - title: "Presentation Title"
    presenter: "Presenter Name"
    type: "PDF" # Options: PDF, PPTX, Video, Link
    url: "/assets/documents/events/event-name/presentation.pdf"

# [OPTIONAL] External links (Canva, Miro, shared documents)
external_resources:
  - title: "Resource Name"
    type: "Type" # Options: Canva, Miro, Google Doc, Video, Website
    url: "https://example.com"
    description: "Brief description"

# [OPTIONAL] Event recording (if publicly shareable)
recording:
  url: "https://youtube.com/watch?v=..."
  duration: "Duration"
  description: "Description of recording content"

# [OPTIONAL] Event photos
# Photos stored in /assets/images/events/event-name/
photos:
  gallery_path: "/assets/images/events/event-name/"
  photo_count: 0
  photographer: "" # Credit photographer if applicable

# =============================================================================
# EVENT OUTCOMES
# =============================================================================

# [OPTIONAL] Key outcomes or decisions
outcomes:
  - "Outcome 1: Description"
  - "Outcome 2: Description"

# [OPTIONAL] Deliverables produced during event
deliverables:
  - "Deliverable 1"
  - "Deliverable 2"

# [OPTIONAL] Follow-up actions decided
action_items:
  - action: "Action to be taken"
    owner: "Person responsible"
    deadline: "YYYY-MM-DD"

# [OPTIONAL] Participant feedback highlights
feedback:
  - quote: "Quote from participant feedback"
    source: "Participant role/name (if public)"

  - quote: "Another piece of feedback"
    source: "Source"

# =============================================================================
# EVENT SERIES OR RELATED EVENTS
# =============================================================================

# [OPTIONAL] If part of recurring series
series:
  name: "Series Name" # Example: "VCH Brainstorming Sessions"
  frequency: "" # Example: "Bi-annual" or "Quarterly"

# [OPTIONAL] Previous event in series
previous_event:
  title: "Previous Event Name"
  url: "/events/previous-event/"

# [OPTIONAL] Next event in series
next_event:
  title: "Upcoming Event Name"
  url: "/events/upcoming-event/"
  date: "YYYY-MM-DD"

# =============================================================================
# RELATED CONTENT
# =============================================================================

# [OPTIONAL] Student projects featured or presented
related_projects:
  - title: "Project Name"
    url: "/projects/project-name/"

# [OPTIONAL] Research discussed or presented
related_research:
  - title: "Research Title"
    url: "/research/research-topic/"

# [OPTIONAL] Partners or sponsors
partners:
  - name: "Organization Name"
    logo: "/assets/images/partners/logo.png"
    url: "https://partner-website.com"

# =============================================================================
# METADATA & SEO
# =============================================================================

# [REQUIRED] Tags for categorization
# 3-6 relevant tags
# Example: ["Brainstorming", "Students", "Supply Chain", "Collaboration"]
tags:
  - Tag1
  - Tag2
  - Tag3

# [OPTIONAL] Featured image for event cards
# Should be 800x600px, stored in /assets/images/events/
# Use representative photo from event
featured_image: "/assets/images/events/event-name/featured.jpg"

# [OPTIONAL] Open Graph image for social media
og_image: "/assets/images/events/event-name/og-image.jpg"

---

<!--
=============================================================================
MARKDOWN CONTENT SECTIONS
=============================================================================
-->

## About the Event

<!--
[REQUIRED] 2-3 paragraph overview
- What was this event?
- Why was it organized?
- Who attended?
- What made it special or significant?
- Overall atmosphere and energy
-->

Write a compelling overview that captures the essence of the event.

**Example:**
On October 2, 2025, Value Chain Hackers hosted its Autumn Brainstorming Session, bringing together 30 students, faculty members, and industry partners for a day of collaborative ideation and supply chain innovation. The event kicked off the new academic year with an energizing exploration of sustainability challenges facing modern supply chains, setting the tone for semester-long student projects.


## Event Objectives

<!--
[REQUIRED] What was the event trying to achieve?
- Clear, specific goals
- Intended outcomes
- Target audience
-->

This event aimed to:

1. **Objective 1:** Description
2. **Objective 2:** Description
3. **Objective 3:** Description


## Agenda & Schedule

<!--
[OPTIONAL but RECOMMENDED]
- Chronological flow of event
- Key sessions or activities
- Timing and structure
- Can use table or bullet format
-->

{% if page.agenda %}
| Time | Activity | Details |
|------|----------|---------|
{% for item in page.agenda %}
| {{ item.time }} | **{{ item.activity }}** | {{ item.description }} |
{% endfor %}
{% endif %}


## Key Topics & Discussions

<!--
[REQUIRED] What was discussed or explored?
- Main themes
- Important conversations
- Challenges identified
- Solutions proposed
- Ideas generated
-->

### Topic 1: Descriptive Heading

Summary of what was discussed, key points raised, insights shared.

**Key Insights:**
- Insight or takeaway 1
- Insight or takeaway 2

### Topic 2: Another Theme

Description of discussion.

### Topic 3: Third Area

Description.


## Speakers & Presentations

<!--
[OPTIONAL - include if event featured speakers]
- Who presented
- What they talked about
- Key messages
- Audience Q&A highlights
-->

{% if page.speakers %}
{% for speaker in page.speakers %}
### {{ speaker.name }} - {{ speaker.organization }}

**Topic:** {{ speaker.topic }}

{{ speaker.bio }}

**Key Takeaways:**
- Takeaway 1
- Takeaway 2

{% endfor %}
{% endif %}


## Student Projects Showcase

<!--
[OPTIONAL - for Roast Days or final presentations]
- Which projects were presented
- Brief summary of each
- Highlights or standout moments
- Link to full project pages
-->

{% if page.student_presenters %}
{% for presenter in page.student_presenters %}
### {{ presenter.project }}

**Presented by:** {{ presenter.team }}

Brief description of project and presentation highlights.

[View Full Project](/projects/project-url)

{% endfor %}
{% endif %}


## Activities & Workshops

<!--
[OPTIONAL - if event included interactive components]
- Description of activities
- Participation and engagement
- Outcomes or artifacts created
- What participants learned
-->

### Activity 1: Name

Description of the activity, what participants did, and outcomes.

### Activity 2: Name

Description.


## Highlights & Memorable Moments

<!--
[OPTIONAL but RECOMMENDED]
- Standout moments
- Surprising insights
- Participant reactions
- Collaborative breakthroughs
- Human stories
-->

Some memorable moments from the event:

- **Highlight 1:** Description of moment and why it was significant
- **Highlight 2:** Description
- **Highlight 3:** Description

> "Participant quote capturing the spirit or impact of the event"
> — Participant Name, Role


## Outcomes & Next Steps

<!--
[REQUIRED] What resulted from this event?
- Decisions made
- Action items identified
- Deliverables produced
- Impact on ongoing work
- Future plans
-->

### Key Outcomes

1. **Outcome 1:** Description and impact
2. **Outcome 2:** Description
3. **Outcome 3:** Description

### Action Items

{% if page.action_items %}
{% for action in page.action_items %}
- **{{ action.action }}** (Owner: {{ action.owner }}, Due: {{ action.deadline }})
{% endfor %}
{% endif %}

### Follow-Up

Plans for continuing momentum from this event:
- Follow-up plan 1
- Follow-up plan 2


## Participant Feedback

<!--
[OPTIONAL]
- Quotes from attendees
- Survey results
- Testimonials
- What participants valued
-->

Participants shared positive feedback about the event:

{% if page.feedback %}
{% for item in page.feedback %}
> "{{ item.quote }}"
> — {{ item.source }}

{% endfor %}
{% endif %}


## Photo Gallery

<!--
[OPTIONAL but HIGHLY RECOMMENDED]
- Event photos with captions
- Capture variety: speakers, activities, interactions, venue
- Optimize images (<500KB each)
- Include alt text for accessibility
-->

{% if page.photos and page.photos.photo_count > 0 %}

A selection of {{ page.photos.photo_count }} photos from the event:

<!-- Example photo grid - adjust based on actual photos -->
<div class="photo-gallery">
  <!-- Images will be loaded from {{ page.photos.gallery_path }} -->
  <!-- Implement lightbox or gallery component here -->
</div>

{% if page.photos.photographer %}
*Photos by {{ page.photos.photographer }}*
{% endif %}

{% endif %}

<!--
To add photos manually:
![Event photo description](/assets/images/events/event-name/photo-01.jpg)
*Caption describing what's happening in the photo*
-->


## Resources & Materials

<!--
[OPTIONAL]
- Presentations shared
- Documents distributed
- Recording of sessions
- Additional resources
-->

{% if page.presentations %}
### Presentations

{% for pres in page.presentations %}
- **{{ pres.title }}** by {{ pres.presenter }}: [Download {{ pres.type }}]({{ pres.url }})
{% endfor %}
{% endif %}

{% if page.external_resources %}
### Additional Resources

{% for resource in page.external_resources %}
- **{{ resource.title }}** ({{ resource.type }}): [View Resource]({{ resource.url }})
  <br>{{ resource.description }}
{% endfor %}
{% endif %}

{% if page.recording %}
### Event Recording

[Watch Recording]({{ page.recording.url }}) ({{ page.recording.duration }})

{{ page.recording.description }}
{% endif %}


## Thank You

<!--
[OPTIONAL]
- Acknowledge organizers, sponsors, speakers, participants
- Express gratitude
- Recognize contributions
-->

Value Chain Hackers would like to thank:

- **Organizers:** {% for org in page.organizers %}{{ org }}{% if forloop.last %}.{% else %}, {% endif %}{% endfor %}
- **Speakers:** [Speaker names] for sharing their expertise
- **Participants:** All attendees for their energy and contributions
- **Partners:** {% for partner in page.partners %}{{ partner.name }}{% if forloop.last %}.{% else %}, {% endif %}{% endfor %}
- **Venue:** [Venue name] for hosting us


## Related Events

<!--
[OPTIONAL]
- Past events in series
- Upcoming events
- Similar events
-->

{% if page.previous_event %}
**Previous:** [{{ page.previous_event.title }}]({{ page.previous_event.url }})
{% endif %}

{% if page.next_event %}
**Upcoming:** [{{ page.next_event.title }}]({{ page.next_event.url }}) on {{ page.next_event.date }}
{% endif %}

Other VCH events:
- [Event 1](/events/event-1/)
- [Event 2](/events/event-2/)


---

<!--
=============================================================================
TEMPLATE USAGE NOTES FOR AI
=============================================================================

When Filling This Template:

1. CAPTURE THE ATMOSPHERE
   - Events are about people and energy, not just logistics
   - Describe interactions, engagement, collaborative moments
   - Include quotes and reactions when available
   - Show, don't just tell ("animated discussions" better than "good event")

2. BALANCE OVERVIEW & DETAILS
   - High-level summary for casual readers
   - Detailed agenda for those who want specifics
   - Highlights without overwhelming with minutiae

3. PHOTOS ARE CRITICAL
   - Events are visual - photos bring them to life
   - Always include photo gallery if photos available
   - Captions should be descriptive and engaging
   - Show diverse perspectives: speakers, audience, activities, venue

4. OUTCOMES MATTER
   - Don't just describe what happened - explain what it meant
   - Connect event to broader VCH mission
   - Show tangible results (decisions, deliverables, connections)
   - Link to follow-up work (projects launched, research initiated)

5. RESPECT PRIVACY
   - Only name participants if appropriate/allowed
   - Use "Student Name" or "Industry Partner" if needed
   - Check photo permissions before publishing
   - Be mindful of sensitive discussions

Content Quality Standards:
- Engaging narrative that captures event spirit
- Specific details create credibility
- Balance between informative and promotional
- Accessible to those who didn't attend
- Professional yet warm and welcoming

SEO Best Practices:
- Title: Event name + date/year for uniqueness
- Description: Event type + key topic + outcome
- Tags: Mix of event type and content themes
- Featured image: Active, engaging moment from event

Photo Guidelines:
- Optimize all images: <500KB, WebP preferred
- Use descriptive filenames: event-name-activity-01.jpg
- Alt text: Describe what's happening, not just "event photo"
- Mix of wide shots and close-ups
- Include candid moments, not just posed photos

Common Mistakes to Avoid:
- ❌ Generic descriptions ("great event", "productive discussions")
- ❌ Just listing agenda without context or outcomes
- ❌ Omitting photos (if available)
- ❌ Forgetting to link to related projects/research
- ❌ No follow-up or outcomes mentioned
- ❌ Overly formal or corporate tone

Examples of Good Event Pages:
- Tell story arc: anticipation → experience → outcomes
- Include participant voices (quotes)
- Show visual evidence (photos)
- Connect to broader VCH narrative
- Inspire attendance at future events

This Template is FOR:
- Brainstorming sessions
- Roast days (final presentations)
- Workshops and training
- Guest lectures
- Conferences and symposia
- Networking events
- Hackathons
- Opening/closing ceremonies
-->

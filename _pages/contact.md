---
layout: default
title: "Contact Us"
permalink: /contact/
description: "Get in touch with Value Chain Hackers - Schedule a call, join our community, or send us a message"
---

<style>
    .contact-hero {
        background: linear-gradient(135deg, #2d5016 0%, #8fbc3f 100%);
    }
    .contact-card {
        transition: all 0.3s ease;
    }
    .contact-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
</style>

<!-- Hero Section -->
<section class="contact-hero text-white py-20">
    <div class="max-w-4xl mx-auto px-4 text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-6">Let's Connect</h1>
        <p class="text-xl md:text-2xl mb-8 opacity-90">
            Whether you're looking to collaborate, attend a workshop, or just say hello, we'd love to hear from you.
        </p>
    </div>
</section>

<!-- Contact Methods -->
<section class="py-16 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <div class="text-center mb-12">
            <h2 class="text-3xl md:text-4xl font-bold text-vch-gray mb-4">How Can We Help?</h2>
            <p class="text-lg text-vch-light-gray max-w-3xl mx-auto">
                Choose the option that works best for you
            </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
            <!-- Schedule a Call -->
            <div class="contact-card bg-white rounded-xl p-8 border-2 border-vch-green shadow-sm">
                <div class="text-5xl mb-4">📅</div>
                <h3 class="text-2xl font-semibold text-vch-gray mb-3">Schedule a Call</h3>
                <p class="text-vch-light-gray mb-6">
                    Book a free 30-minute discovery call to discuss collaboration, projects, or workshops.
                </p>
                <a href="#book-call" class="bg-vch-green text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors inline-block w-full text-center">
                    Book a Call
                </a>
            </div>

            <!-- Join Discord -->
            <div class="contact-card bg-white rounded-xl p-8 border-2 border-purple-500 shadow-sm">
                <div class="text-5xl mb-4">💬</div>
                <h3 class="text-2xl font-semibold text-vch-gray mb-3">Join Our Community</h3>
                <p class="text-vch-light-gray mb-6">
                    Connect with supply chain enthusiasts, students, and professionals on Discord.
                </p>
                <a href="{{ site.discord_url }}" target="_blank" rel="noopener noreferrer" class="bg-purple-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-purple-700 transition-colors inline-block w-full text-center">
                    Join Discord
                </a>
            </div>

            <!-- Email Us -->
            <div class="contact-card bg-white rounded-xl p-8 border-2 border-vch-yellow shadow-sm">
                <div class="text-5xl mb-4">✉️</div>
                <h3 class="text-2xl font-semibold text-vch-gray mb-3">Send an Email</h3>
                <p class="text-vch-light-gray mb-6">
                    For general inquiries, partnership proposals, or detailed questions.
                </p>
                <a href="mailto:{{ site.email }}" class="bg-vch-yellow text-vch-gray px-6 py-3 rounded-lg font-semibold hover:bg-yellow-500 transition-colors inline-block w-full text-center">
                    Email Us
                </a>
            </div>
        </div>
    </div>
</section>

<!-- Cal.com Integration -->
<section class="py-16 bg-vch-bg" id="book-call">
    <div class="max-w-5xl mx-auto px-4">
        <div class="text-center mb-12">
            <h2 class="text-3xl md:text-4xl font-bold text-vch-gray mb-4">Schedule Your Free Discovery Call</h2>
            <p class="text-lg text-vch-light-gray max-w-3xl mx-auto">
                Choose a time that works for you. We'll discuss your needs and how we can work together.
            </p>
        </div>

        <!-- Cal.com Embed -->
        <div class="bg-white rounded-2xl p-6 shadow-lg">
            <div id="cal-embed-container" style="width:100%;height:700px;overflow:scroll"></div>
        </div>

        <div class="mt-8 text-center">
            <p class="text-vch-light-gray mb-2">Prefer to email instead?</p>
            <a href="mailto:{{ site.email }}" class="text-vch-green font-semibold text-lg hover:text-green-700">
                {{ site.email }}
            </a>
        </div>
    </div>
</section>

<!-- Other Contact Methods -->
<section class="py-16 bg-white">
    <div class="max-w-6xl mx-auto px-4">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-bold text-vch-gray mb-4">Find Us Elsewhere</h2>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- LinkedIn -->
            <a href="{{ site.linkedin_url }}" target="_blank" rel="noopener noreferrer" class="contact-card bg-vch-bg rounded-xl p-6 text-center block border hover:border-vch-green">
                <div class="text-4xl mb-3">🔗</div>
                <h3 class="font-semibold text-vch-gray mb-2">LinkedIn</h3>
                <p class="text-sm text-vch-light-gray">Follow for updates and insights</p>
            </a>

            <!-- GitHub -->
            <a href="{{ site.github_url }}" target="_blank" rel="noopener noreferrer" class="contact-card bg-vch-bg rounded-xl p-6 text-center block border hover:border-vch-green">
                <div class="text-4xl mb-3">💻</div>
                <h3 class="font-semibold text-vch-gray mb-2">GitHub</h3>
                <p class="text-sm text-vch-light-gray">Explore our open-source projects</p>
            </a>

            <!-- Discord -->
            <a href="{{ site.discord_url }}" target="_blank" rel="noopener noreferrer" class="contact-card bg-vch-bg rounded-xl p-6 text-center block border hover:border-vch-green">
                <div class="text-4xl mb-3">💬</div>
                <h3 class="font-semibold text-vch-gray mb-2">Discord</h3>
                <p class="text-sm text-vch-light-gray">Join our community chat</p>
            </a>

            <!-- Newsletter -->
            <button onclick="openNewsletterModal()" class="contact-card bg-vch-bg rounded-xl p-6 text-center block border hover:border-vch-green w-full">
                <div class="text-4xl mb-3">📬</div>
                <h3 class="font-semibold text-vch-gray mb-2">Newsletter</h3>
                <p class="text-sm text-vch-light-gray">Stay updated with our latest news</p>
            </button>
        </div>
    </div>
</section>

<!-- Office Location -->
<section class="py-16 bg-vch-bg">
    <div class="max-w-6xl mx-auto px-4">
        <div class="grid md:grid-cols-2 gap-12 items-center">
            <div>
                <h2 class="text-3xl font-bold text-vch-gray mb-4">Visit Us</h2>
                <div class="space-y-4">
                    <div class="flex items-start gap-3">
                        <div class="text-2xl">📍</div>
                        <div>
                            <h3 class="font-semibold text-vch-gray mb-1">Address</h3>
                            <p class="text-vch-light-gray">
                                Windesheim University<br>
                                Zwolle, Netherlands
                            </p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3">
                        <div class="text-2xl">✉️</div>
                        <div>
                            <h3 class="font-semibold text-vch-gray mb-1">Email</h3>
                            <p class="text-vch-light-gray">
                                <a href="mailto:{{ site.email }}" class="text-vch-green hover:text-green-700">{{ site.email }}</a>
                            </p>
                        </div>
                    </div>
                    <div class="flex items-start gap-3">
                        <div class="text-2xl">🕐</div>
                        <div>
                            <h3 class="font-semibold text-vch-gray mb-1">Office Hours</h3>
                            <p class="text-vch-light-gray">
                                By appointment only<br>
                                <a href="#book-call" class="text-vch-green hover:text-green-700 font-semibold">Schedule a visit →</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-white rounded-2xl p-8 shadow-sm border">
                <h3 class="text-xl font-semibold text-vch-gray mb-4">Quick Response Times</h3>
                <div class="space-y-4">
                    <div class="flex items-center justify-between pb-3 border-b">
                        <span class="text-vch-light-gray">📧 Email</span>
                        <span class="font-semibold text-vch-gray">24-48 hours</span>
                    </div>
                    <div class="flex items-center justify-between pb-3 border-b">
                        <span class="text-vch-light-gray">💬 Discord</span>
                        <span class="font-semibold text-vch-gray">Few hours</span>
                    </div>
                    <div class="flex items-center justify-between pb-3 border-b">
                        <span class="text-vch-light-gray">📅 Scheduled Calls</span>
                        <span class="font-semibold text-vch-gray">Same day</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-vch-light-gray">🔗 LinkedIn</span>
                        <span class="font-semibold text-vch-gray">2-3 days</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Section -->
<section class="py-16 bg-white">
    <div class="max-w-4xl mx-auto px-4">
        <div class="text-center mb-12">
            <h2 class="text-3xl md:text-4xl font-bold text-vch-gray mb-4">Common Questions</h2>
        </div>

        <div class="space-y-4">
            <details class="bg-vch-bg rounded-xl p-6 cursor-pointer">
                <summary class="font-semibold text-vch-gray text-lg">How quickly will you respond to my inquiry?</summary>
                <p class="text-vch-light-gray mt-3">
                    We typically respond to emails within 24-48 hours during business days. For urgent matters, we recommend joining our Discord server for faster responses, or booking a call directly via Cal.com.
                </p>
            </details>

            <details class="bg-vch-bg rounded-xl p-6 cursor-pointer">
                <summary class="font-semibold text-vch-gray text-lg">What should I prepare for a discovery call?</summary>
                <p class="text-vch-light-gray mt-3">
                    Come prepared with a brief description of your challenge or project idea, your goals and timeline, and any constraints (budget, resources, etc.). Don't worry about having all the details figured out—the discovery call is designed to help clarify and refine your needs.
                </p>
            </details>

            <details class="bg-vch-bg rounded-xl p-6 cursor-pointer">
                <summary class="font-semibold text-vch-gray text-lg">Can students join your Discord community?</summary>
                <p class="text-vch-light-gray mt-3">
                    Absolutely! Our Discord community welcomes students, researchers, professionals, and anyone interested in supply chain innovation and sustainability. It's a great place to ask questions, share resources, and connect with like-minded people.
                </p>
            </details>

            <details class="bg-vch-bg rounded-xl p-6 cursor-pointer">
                <summary class="font-semibold text-vch-gray text-lg">Do you offer consultations to companies outside the Netherlands?</summary>
                <p class="text-vch-light-gray mt-3">
                    Yes! While we're based in the Netherlands, we work with partners globally. Many of our collaborations happen remotely, and we're experienced in virtual project management and workshops.
                </p>
            </details>

            <details class="bg-vch-bg rounded-xl p-6 cursor-pointer">
                <summary class="font-semibold text-vch-gray text-lg">I'm a journalist/researcher. Can I interview someone from VCH?</summary>
                <p class="text-vch-light-gray mt-3">
                    We're always happy to share our insights on supply chain innovation, sustainability, and student-industry collaboration. Please email us at {{ site.email }} with your request, including your outlet/institution, topic, and deadline.
                </p>
            </details>
        </div>
    </div>
</section>

<!-- Cal.com Embed Script -->
<script type="text/javascript">
  (function (C, A, L) {
    let p = function (a, ar) {
      a.q.push(ar);
    };
    let d = C.document;
    C.Cal = C.Cal || function () {
      let cal = C.Cal;
      let ar = arguments;
      if (!cal.loaded) {
        cal.ns = {};
        cal.q = cal.q || [];
        d.head.appendChild(d.createElement("script")).src = A;
        cal.loaded = true;
      }
      if (ar[0] === L) {
        const api = function () {
          p(api, arguments);
        };
        const namespace = ar[1];
        api.q = api.q || [];
        typeof namespace === "string" ? (cal.ns[namespace] = api) && p(api, ar) : p(cal, ar);
        return;
      }
      p(cal, ar);
    };
  })(window, "https://app.cal.com/embed/embed.js", "init");

  Cal("init", {origin:"https://app.cal.com"});

  Cal("inline", {
    elementOrSelector:"#cal-embed-container",
    calLink: "valuechainhackers/discovery-call",
    layout: "month_view"
  });

  Cal("ui", {
    "styles":{"branding":{"brandColor":"#2d5016"}},
    "hideEventTypeDetails":false,
    "layout":"month_view"
  });
</script>

<!-- Newsletter Modal -->
<div id="newsletterModal" class="fixed inset-0 bg-black bg-opacity-50 hidden items-center justify-center z-50" onclick="closeNewsletterModal(event)">
    <div class="bg-white rounded-2xl p-8 max-w-md mx-4" onclick="event.stopPropagation()">
        <div class="flex justify-between items-center mb-6">
            <h3 class="text-2xl font-bold text-vch-gray">📬 Subscribe to Our Newsletter</h3>
            <button onclick="closeNewsletterModal()" class="text-gray-400 hover:text-gray-600 text-2xl">&times;</button>
        </div>

        <p class="text-vch-light-gray mb-6">
            Get monthly updates on supply chain innovation, student projects, workshop announcements, and industry insights delivered to your inbox.
        </p>

        <form id="newsletter-form" class="space-y-4" onsubmit="handleNewsletterSubmit(event)">
            <div>
                <label for="newsletter-email" class="block text-sm font-semibold text-vch-gray mb-2">Email Address *</label>
                <input
                    type="email"
                    id="newsletter-email"
                    name="email"
                    required
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-vch-green focus:border-transparent"
                    placeholder="your.email@example.com"
                >
            </div>

            <div>
                <label for="newsletter-name" class="block text-sm font-semibold text-vch-gray mb-2">Name (Optional)</label>
                <input
                    type="text"
                    id="newsletter-name"
                    name="name"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-vch-green focus:border-transparent"
                    placeholder="Your name"
                >
            </div>

            <div class="space-y-2">
                <p class="text-sm font-semibold text-vch-gray">I'm interested in:</p>
                <label class="flex items-center text-sm text-vch-light-gray">
                    <input type="checkbox" name="interests" value="projects" class="mr-2 rounded text-vch-green">
                    Student projects and research
                </label>
                <label class="flex items-center text-sm text-vch-light-gray">
                    <input type="checkbox" name="interests" value="workshops" class="mr-2 rounded text-vch-green">
                    Workshops and events
                </label>
                <label class="flex items-center text-sm text-vch-light-gray">
                    <input type="checkbox" name="interests" value="insights" class="mr-2 rounded text-vch-green">
                    Supply chain insights
                </label>
            </div>

            <button
                type="submit"
                class="w-full bg-vch-green text-white px-8 py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors"
            >
                Subscribe
            </button>

            <p class="text-xs text-center text-vch-light-gray">
                We respect your privacy. Unsubscribe anytime.
            </p>
        </form>

        <div id="newsletter-success" class="hidden text-center py-8">
            <div class="text-6xl mb-4">✅</div>
            <h4 class="text-xl font-bold text-vch-gray mb-2">Thanks for subscribing!</h4>
            <p class="text-vch-light-gray mb-4">Check your email to confirm your subscription.</p>
            <button onclick="closeNewsletterModal()" class="text-vch-green font-semibold hover:text-green-700">Close</button>
        </div>
    </div>
</div>

<script>
function openNewsletterModal() {
    document.getElementById('newsletterModal').classList.remove('hidden');
    document.getElementById('newsletterModal').classList.add('flex');
    document.body.style.overflow = 'hidden';
}

function closeNewsletterModal(event) {
    if (!event || event.target.id === 'newsletterModal') {
        document.getElementById('newsletterModal').classList.add('hidden');
        document.getElementById('newsletterModal').classList.remove('flex');
        document.body.style.overflow = 'auto';

        // Reset form
        document.getElementById('newsletter-form').reset();
        document.getElementById('newsletter-form').classList.remove('hidden');
        document.getElementById('newsletter-success').classList.add('hidden');
    }
}

function handleNewsletterSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const email = form.email.value;
    const name = form.name.value;
    const interests = Array.from(form.querySelectorAll('input[name="interests"]:checked')).map(cb => cb.value);

    // TODO: Replace with actual newsletter service integration
    // Options: Mailchimp, Buttondown, ConvertKit, or EmailJS
    console.log('Newsletter signup:', { email, name, interests });

    // For now, store in localStorage and show success message
    const subscribers = JSON.parse(localStorage.getItem('newsletter_subscribers') || '[]');
    subscribers.push({
        email,
        name,
        interests,
        timestamp: new Date().toISOString()
    });
    localStorage.setItem('newsletter_subscribers', JSON.stringify(subscribers));

    // Show success message
    form.classList.add('hidden');
    document.getElementById('newsletter-success').classList.remove('hidden');

    // Optional: Send to backend or external service
    // Example with EmailJS or custom endpoint:
    // fetch('/api/newsletter/subscribe', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify({ email, name, interests })
    // });
}
</script>

<style>
#newsletterModal {
    backdrop-filter: blur(4px);
}
</style>

---
layout: default
title: "Our Projects"
permalink: /projects/
description: "Explore Value Chain Hackers' student projects, research outputs, and partner collaborations tackling real-world supply chain sustainability challenges."
---

<style>
    .hero-section {
        background: linear-gradient(135deg, #2d5016 0%, #8fbc3f 100%);
        color: white;
        padding: 4rem 1rem;
        margin-bottom: 3rem;
    }

    .filter-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        justify-content: center;
        margin-bottom: 2rem;
    }

    .filter-btn {
        padding: 0.75rem 1.5rem;
        border: 2px solid #2d5016;
        border-radius: 2rem;
        background: white;
        color: #2d5016;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .filter-btn:hover,
    .filter-btn.active {
        background: #2d5016;
        color: white;
    }

    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 2rem;
        margin-bottom: 3rem;
    }

    .project-card {
        background: white;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        padding: 1.5rem;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
    }

    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    .project-card.hidden {
        display: none;
    }

    .project-status {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .status-completed {
        background: #8fbc3f;
        color: #2d5016;
    }

    .status-ongoing {
        background: #ff7b54;
        color: white;
    }

    .status-planned {
        background: #e5e7eb;
        color: #374151;
    }

    .project-category {
        font-size: 0.75rem;
        color: #6b7280;
        background: #f3f4f6;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        display: inline-block;
        margin-bottom: 0.5rem;
    }

    .project-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #2d5016;
        margin-bottom: 0.75rem;
    }

    .project-description {
        color: #6b7280;
        margin-bottom: 1rem;
        flex-grow: 1;
        line-height: 1.6;
    }

    .project-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }

    .project-tag {
        font-size: 0.75rem;
        padding: 0.25rem 0.75rem;
        background: #f3f4f6;
        color: #374151;
        border-radius: 1rem;
    }

    .project-links {
        display: flex;
        gap: 0.75rem;
        align-items: center;
    }

    .project-link {
        flex: 1;
        text-align: center;
        padding: 0.75rem;
        border-radius: 0.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        text-decoration: none;
        font-size: 0.875rem;
    }

    .link-primary {
        background: #8fbc3f;
        color: #2d5016;
    }

    .link-primary:hover {
        background: #7aa835;
    }

    .link-secondary {
        background: transparent;
        color: #2d5016;
        border: 1px solid #2d5016;
    }

    .link-secondary:hover {
        background: #f3f4f6;
    }

    .stats-section {
        background: #f9fafb;
        padding: 3rem 1rem;
        margin: 3rem 0;
        border-radius: 12px;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    .stat-item {
        text-align: center;
    }

    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        color: #2d5016;
    }

    .stat-label {
        color: #6b7280;
        font-size: 1rem;
        margin-top: 0.5rem;
    }

    @media (max-width: 768px) {
        .projects-grid {
            grid-template-columns: 1fr;
        }
        .hero-section {
            padding: 2rem 1rem;
        }
    }
</style>

<!-- Hero Section -->
<section class="hero-section">
    <div class="max-w-4xl mx-auto text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">Our Projects</h1>
        <p class="text-xl opacity-90">
            Discover how students, researchers, and industry partners collaborate to solve real-world supply chain sustainability challenges.
        </p>
    </div>
</section>

<!-- Stats Section -->
<section class="stats-section">
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-number" id="total-projects">{{ site.projects | size }}</div>
            <div class="stat-label">Total Projects</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="completed-projects">0</div>
            <div class="stat-label">Completed Projects</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="ongoing-projects">0</div>
            <div class="stat-label">Ongoing Projects</div>
        </div>
        <div class="stat-item">
            <div class="stat-number" id="student-projects">0</div>
            <div class="stat-label">Student Projects</div>
        </div>
    </div>
</section>

<!-- Filter Buttons -->
<section class="max-w-7xl mx-auto px-4">
    <div class="filter-buttons">
        <button class="filter-btn active" data-filter="all">All Projects</button>
        <button class="filter-btn" data-filter="Student Project">Student Projects</button>
        <button class="filter-btn" data-filter="Research Output">Research Outputs</button>
        <button class="filter-btn" data-filter="Partner Collaboration">Partner Collaborations</button>
        <button class="filter-btn" data-filter="Completed">Completed</button>
        <button class="filter-btn" data-filter="Ongoing">Ongoing</button>
    </div>

    <!-- Projects Grid -->
    <div class="projects-grid" id="projects-container">
        {% assign sorted_projects = site.projects | sort: 'date' | reverse %}
        {% for project in sorted_projects %}
        <div class="project-card"
             data-category="{{ project.category }}"
             data-status="{{ project.status }}"
             data-tags="{{ project.tags | join: ',' }}">

            <!-- Status and Category -->
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                <span class="project-status status-{{ project.status | downcase }}">
                    {{ project.status }}
                </span>
                <span class="project-category">
                    {{ project.category }}
                </span>
            </div>

            <!-- Title -->
            <h3 class="project-title">{{ project.title }}</h3>

            <!-- Description -->
            <p class="project-description">
                {{ project.description }}
            </p>

            <!-- Tags -->
            {% if project.tags %}
            <div class="project-tags">
                {% for tag in project.tags limit:3 %}
                <span class="project-tag">{{ tag }}</span>
                {% endfor %}
            </div>
            {% endif %}

            <!-- Links -->
            <div class="project-links">
                {% if project.github %}
                <a href="{{ project.github }}" target="_blank" rel="noopener noreferrer" class="project-link link-secondary">
                    <i class="fab fa-github"></i> GitHub
                </a>
                {% endif %}
                {% if project.website %}
                <a href="{{ project.website }}" target="_blank" rel="noopener noreferrer" class="project-link link-secondary">
                    <i class="fas fa-external-link-alt"></i> Website
                </a>
                {% endif %}
                <a href="{{ project.url }}" class="project-link link-primary">
                    Learn More →
                </a>
            </div>
        </div>
        {% endfor %}
    </div>
</section>

<!-- Call to Action -->
<section class="max-w-4xl mx-auto px-4 py-16 text-center">
    <div style="background: linear-gradient(135deg, #2d5016 0%, #8fbc3f 100%); color: white; padding: 3rem; border-radius: 16px;">
        <h2 class="text-3xl font-bold mb-4">Have a Project Idea?</h2>
        <p class="text-xl mb-6 opacity-90">
            We're always looking for new challenges to tackle. Partner with us to solve your supply chain sustainability problems.
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="{{ '/collaborate/' | relative_url }}" class="bg-white text-vch-green px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors inline-block">
                Start a Collaboration
            </a>
            <a href="{{ '/#contact' | relative_url }}" class="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-vch-green transition-colors inline-block">
                Contact Us
            </a>
        </div>
    </div>
</section>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    // Calculate stats
    let completedCount = 0;
    let ongoingCount = 0;
    let studentCount = 0;

    projectCards.forEach(card => {
        const status = card.getAttribute('data-status');
        const category = card.getAttribute('data-category');

        if (status === 'Completed') completedCount++;
        if (status === 'Ongoing') ongoingCount++;
        if (category === 'Student Project') studentCount++;
    });

    document.getElementById('completed-projects').textContent = completedCount;
    document.getElementById('ongoing-projects').textContent = ongoingCount;
    document.getElementById('student-projects').textContent = studentCount;

    // Filter functionality
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');

            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filter projects
            projectCards.forEach(card => {
                if (filter === 'all') {
                    card.classList.remove('hidden');
                } else {
                    const category = card.getAttribute('data-category');
                    const status = card.getAttribute('data-status');

                    if (category === filter || status === filter) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                }
            });
        });
    });
});
</script>

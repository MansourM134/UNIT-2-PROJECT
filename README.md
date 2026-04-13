# HajjVision — برنامج خدمة ضيوف الرحمن

---

## Overview

**HajjVision** is a informational web platform dedicated to presenting the **Hajj Guests of the Merciful Service Program** (برنامج خدمة ضيوف الرحمن), one of Saudi Arabia's Vision 2030 realization programs. Launched under the patronage of the Custodian of the Two Holy Mosques, the program aims to serve a greater number of Umrah pilgrims and visitors to the Holy Sites, enhance their spiritual and cultural experience, and raise the quality of services provided to them.

The platform is a fully Arabic-language, multi-page website that communicates the program's mission, strategic framework, goals, performance targets, and focus areas in a structured, visually rich format. It supports both **light and dark themes**, persisted via browser cookies, and is built with **Django 6.0.4** using a clean template-based architecture.

### Tech Stack

- **Backend:** Python / Django 6.0.4
- **Frontend:** HTML5, CSS3 (custom per-page stylesheets)
- **Templating:** Django Templates
- **Static Assets:** Images, CSS, and video

---

## Features & User Stories

### Visitor 

- As a visitor, I should be able to **view the home page** and read an overview of the Hajj Guests Service Program, including its vision, scope, and leadership directives.
- As a visitor, I should be able to **browse leadership quotes** from the Custodian of the Two Holy Mosques and the Crown Prince regarding Hajj and Umrah service.
- As a visitor, I should be able to **navigate to the About page** to learn about the program's description, mission, and role within Vision 2030.
- As a visitor, I should be able to **view the Goals page** to understand the three core objectives of the program (facilitating more Umrah visitors, enhancing the experience, and elevating Saudi Arabia's image).
- As a visitor, I should be able to **explore the Targets page** to review key performance indicators and aspirational targets set for 2025 and 2030.
- As a visitor, I should be able to **read the Baseline page** to understand the current state of affairs, existing challenges, and ongoing transformation efforts.
- As a visitor, I should be able to **study the Strategic Framework page** to learn about the six strategic dimensions and pillars guiding the program.
- As a visitor, I should be able to **review the Focus Areas page** to understand the complete pilgrim journey (from inspiration to memory) and the service ecosystem surrounding it.
- As a visitor, I should be able to **toggle between light and dark themes** for a comfortable reading experience, with the preference saved for future visits.

---

## Usage

### Running the Project Locally

```bash
# Clone the repository
git clone <repository-url>
cd HajjVision

# Install dependencies
pip install django

# Start the development server
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

---

### Navigating the Platform

| Action | URL |
|---|---|
| Visit the home page | `http://127.0.0.1:8000/` |
| View the About page | `http://127.0.0.1:8000/about/` |
| View the Goals page | `http://127.0.0.1:8000/goals/` |
| View Targets & KPIs | `http://127.0.0.1:8000/targets/` |
| View the Baseline analysis | `http://127.0.0.1:8000/baseline/` |
| View the Strategic Framework | `http://127.0.0.1:8000/strategy/` |
| View Focus Areas | `http://127.0.0.1:8000/focus/` |
| Access the admin panel | `http://127.0.0.1:8000/admin/` |

---

### Theme Switching

The platform supports light and dark mode. Switch themes via:

```
# Switch to dark mode
http://127.0.0.1:8000/set-theme/?theme=dark&next=/

# Switch to light mode
http://127.0.0.1:8000/set-theme/?theme=light&next=/
```

The `next` parameter accepts any valid path to redirect back to after the theme is set. The preference is stored in a cookie valid for one year.


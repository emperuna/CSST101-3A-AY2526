<div align="center">

# CSST101-3A Portfolio

### Advanced Representation and Reasoning in AI

[![Made with Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://python.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.x-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, dark-themed portfolio website showcasing coursework exploring **expert systems**, **predicate logic**, **inference engines**, and **non-monotonic reasoning**.

[**View Live Site**](https://emperuna.github.io/CSST101-3A-AY2526/) · [**View Activities**](activities.html) · [**About**](about.html)

</div>

---

## Features

- **Dark Academic Theme** — Modern glassmorphism design with animated backgrounds
- **Fully Responsive** — Optimized for desktop, tablet, and mobile
- **Component-Based** — Reusable navbar/footer via JavaScript injection
- **Tailwind CSS** — Utility-first styling with custom theme configuration

---

## Project Structure

```
CSST101-3A-AY2526/
├── index.html                 # Homepage
├── about.html                 # About page
├── activities.html            # Activity gallery
│
├── activities/                # Activity detail pages
│   ├── mp-01.html            # Mini Expert System
│   ├── mp-02.html            # Predicate Logic
│   ├── mp-03.html            # Troubleshooting Assistant
│   └── at-04.html            # Non-Monotonic Reasoning
│
├── assets/
│   ├── css/
│   │   └── theme.css         # Shared styles
│   ├── js/
│   │   ├── tailwind.config.js
│   │   ├── components.js     # Navbar/Footer components
│   │   └── main.js           # Shared scripts
│   └── images/
│       ├── jg-logo.png
│       └── hero-illustration.png
│
└── coursework/                # Source code & documentation
    ├── machine-problem-01/
    ├── machine-problem-02/
    ├── machine-problem-03/
    └── assessment-task-04/
```

---

## Coursework Activities

|  #  | Type | Title                         | Key Concepts                             |
| :-: | :--: | ----------------------------- | ---------------------------------------- |
| 01  |  MP  | **Mini Expert System**        | Propositional Logic, Implication (P → Q) |
| 02  |  MP  | **Predicate Logic**           | Unification, Forward/Backward Chaining   |
| 03  |  MP  | **Troubleshooting Assistant** | Rule-Based Systems, Decision Trees       |
| 04  |  AT  | **Non-Monotonic Reasoning**   | Belief Revision, Default Logic           |

> **MP** = Machine Problem · **AT** = Assessment Task

---

## Quick Start

### Option 1: Direct Browser

```bash
# Clone the repository
git clone https://github.com/emperuna/CSST101-3A-AY2526.git
cd CSST101-3A-AY2526

# Open index.html in your browser
open index.html   # macOS
start index.html  # Windows
```

### Option 2: Local Development Server

```bash
# Using Python
python -m http.server 8000

# Or using Node.js
npx serve .
```

Then open `http://localhost:8000` in your browser.

---

## Tech Stack

| Category          | Technologies            |
| ----------------- | ----------------------- |
| **Frontend**      | HTML5, CSS3, JavaScript |
| **Styling**       | Tailwind CSS (CDN)      |
| **Backend Logic** | Python 3                |
| **Notebooks**     | Jupyter / Google Colab  |

---

## Author

<table>
<tr>
<td align="center">
<strong>Jeremy M. Garin</strong><br>
<sub>BSCS — 3A</sub><br>
<sub>Academic Year 2025-2026</sub><br><br>
<a href="https://github.com/emperuna">
<img src="https://img.shields.io/badge/GitHub-@emperuna-181717?logo=github" alt="GitHub">
</a>
</td>
</tr>
</table>

---

## License

This project is for **educational purposes only**. All coursework materials are submitted as part of CSST-101 at the university.

# 🍔 ByteBites Tinker Activity
A hands-on exercise from CodePath's **AI110: Foundations of AI Engineering** course.

## 📌 Overview
ByteBites is a campus food ordering app backend built in Python. This project was designed to practice object-oriented programming, UML system design, and AI-assisted development using GitHub Copilot.

## 🎯 What I Built
A clean backend system with 4 core Python classes:

| Class | Description |
|---|---|
| `Customer` | Tracks customer name and purchase history |
| `MenuItem` | Represents a food item with name, price, category, and popularity rating |
| `Menu` | Holds all menu items, supports filtering by category and sorting by popularity |
| `Order` | Groups selected items and computes the total cost |

## 🛠️ How I Built It
The project was completed in 4 parts:

**Part 1 — System Design**
- Analyzed a product spec to identify core classes
- Used GitHub Copilot Chat to generate a UML-style class diagram
- Created a custom Copilot agent to keep designs focused and spec-aligned

**Part 2 — Code Implementation**
- Translated the UML diagram into Python class scaffolds
- Used Copilot's Plan, Ask, and Edit modes to draft and refine each class

**Part 3 — Algorithmic Enhancements**
- Added filtering by category
- Added sorting by popularity rating
- Implemented order total calculation

**Part 4 — Testing and Validation**
- Wrote automated tests using `pytest`
- Tested order totals, empty orders, and category filtering
- All 3 tests passing ✅

## 🚀 How to Run

**Install dependencies:**
```bash
pip install pytest
```

**Run the tests:**
```bash
python -m pytest test_bytebites.py -v
```

**Run the manual test script:**
```bash
python test_manual.py
```

## 📁 Project Structure
```
bytebites_tinker_activity/
├── .github/
│   └── agents/
│       └── bytebites_design_agent.md  # Custom Copilot agent
├── models.py                          # Core Python classes
├── test_bytebites.py                  # Automated pytest tests
├── test_manual.py                     # Manual test script
├── bytebites_spec.md                  # Original feature spec
├── bytebites_design.md                # Final UML diagram
└── draft_from_copilot.md              # Initial Copilot UML draft
```

## 🤖 AI Tools Used
- **GitHub Copilot Chat** (Plan, Ask, Edit modes)
- **Custom ByteBites Design Agent** for focused and spec-aligned suggestions

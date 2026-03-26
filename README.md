# Lobster Binance OS

**A unified intent router and task orchestration layer for the Binance ecosystem.**

Lobster Binance OS is a Binance-native AI orchestration agent that turns fragmented products, campaigns, assets, tasks, and risks into **one prioritized action view**.

It does not simply summarize announcements.  
It does not just list opportunities.  
It reorganizes the Binance ecosystem around the user's real goal:

- what to do now
- what to do next
- what to avoid
- and why

---

## TL;DR

Binance offers many products and opportunity paths at the same time:

- Earn
- Launchpool
- Alpha opportunities
- trading competitions
- staking
- temporary campaigns
- task-based rewards

The problem is not lack of opportunity.

The problem is lack of orchestration.

Most users do not need more raw information.  
They need a unified decision layer that can tell them:

- which path is most worthwhile
- which assets are already tied to another path
- which actions conflict with each other
- and what the best next step is based on their actual goal

**Lobster Binance OS is built to solve that coordination problem.**

---

## What It Is

Lobster Binance OS is an ecosystem-level **intent control and task orchestration layer** for Binance.

Its purpose is to transform:

**goal + assets + eligibility + timing + conflicts**

into

**one ranked execution checklist**

Instead of treating Binance as a collection of unrelated entry points, Lobster Binance OS treats it as an operating environment that should be navigated through structured intent.

---

## Why This Matters

Most Binance users are not suffering from a lack of products.

They are suffering from **decision fragmentation**.

A user may have:

- capital in Flexible Earn
- BNB sitting idle
- a time-sensitive Launchpool live
- a trading task available
- another campaign competing for the same funds

Each opportunity may look valid in isolation.

The problem is that the user does not experience them in isolation.  
They experience them all at once.

Lobster Binance OS is designed to resolve that exact condition.

---

## Core Product Thesis

Binance does not need another generic AI assistant.

It needs an **intent router** that can convert ecosystem complexity into executable order.

Lobster Binance OS is designed as that layer.

It is:

- not a passive dashboard
- not a news summarizer
- not a single-purpose script
- not a blind execution bot

It is a system for translating fragmented ecosystem conditions into a unified action sequence.

---

## What It Solves

Lobster Binance OS addresses five common decision problems inside the Binance ecosystem:

### 1. Fragmented Entry Points
Users face multiple products, campaigns, and tabs without a unified control layer.

### 2. Asset Path Conflicts
The same asset may already be locked, reserved, or better deployed elsewhere.

### 3. Poor Prioritization
Users often see several valid choices, but no clear order of execution.

### 4. High Decision Cost
Ordinary users spend too much time comparing low-risk, medium-risk, and time-sensitive actions.

### 5. No Unified Action View
Information is scattered, but the user's goal is singular.

---

## Core Modules

### Opportunity Scanner
Scans available ecosystem opportunities and normalizes them into comparable action candidates.

### Asset & Eligibility Mapper
Maps user assets, lock status, and path restrictions to determine what is actually executable.

### Conflict Resolver
Detects conflicts across assets, current routes, and competing Binance opportunities.

### Priority Engine
Ranks actions based on user goal, timing, risk, efficiency, and reward quality.

### Action Checklist Generator
Produces a final step-by-step recommendation with clear priorities and exclusions.

---

## System Flow

Lobster Binance OS follows a simple orchestration pipeline:

1. Parse the user's goal, link, text, screenshot, or account context  
2. Scan relevant opportunities in the Binance ecosystem  
3. Map assets, eligibility, and path constraints  
4. Detect conflicts between actions, assets, and existing routes  
5. Rank actions based on goal, timing, efficiency, and risk  
6. Generate a final action checklist

---

## Architecture

```text
User Goal / Context
        ↓
Opportunity Scanner
        ↓
Asset & Eligibility Mapper
        ↓
Conflict Resolver
        ↓
Priority Engine
        ↓
Action Checklist Generator
        ↓
Unified Action View
```

---

## Example Use Case

A user says:

> “I only want to do the most worthwhile low-risk thing on Binance today.”

The system then evaluates:

- current assets
- lock status
- opportunity requirements
- conflicts across paths
- relative risk and reward
- timing sensitivity

And returns a ranked recommendation instead of a fragmented list.

---

## Current Scope

This repository focuses on **decision orchestration**, not exchange-side execution.

The current prototype is built to show how a Binance-oriented AI agent can:

- interpret user intent
- compare multiple opportunity paths
- detect conflicts
- rank alternatives
- and return a structured recommendation

This keeps the system:

- lightweight
- explainable
- modular
- reproducible

---

## Design Principles

### Goal-First
Everything starts from user intent, not from product menus.

### Ecosystem-Native
The system is designed around Binance-specific products, tasks, and path conflicts.

### Conflict-Aware
A valid opportunity is not always an actionable one.

### Priority-Oriented
The value is not only in finding options, but in ranking them properly.

### Explainable
The final output should be understandable, inspectable, and easy to follow.

---

## Repo Structure

```text
Lobster-Binance-OS/
├── app.py
├── main.py
├── requirements.txt
├── engine/
│   ├── scanner.py
│   ├── mapper.py
│   ├── resolver.py
│   ├── priority.py
│   └── checklist.py
├── examples/
└── README.md
```

---

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Local API docs will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## Example API

### `POST /analyze`

```json
{
  "user_goal": "I only want to do the most worthwhile low-risk thing on Binance today",
  "assets": [
    {
      "symbol": "USDT",
      "amount": 500,
      "locked": false,
      "current_path": "flexible_earn"
    },
    {
      "symbol": "BNB",
      "amount": 3,
      "locked": false,
      "current_path": null
    }
  ],
  "opportunities": [
    {
      "id": "launchpool_alpha",
      "name": "Launchpool Alpha",
      "type": "launchpool",
      "required_asset": "USDT",
      "min_amount": 100,
      "reward_score": 85,
      "risk_score": 25,
      "time_sensitive": true
    },
    {
      "id": "earn_bonus",
      "name": "Simple Earn Bonus",
      "type": "earn",
      "required_asset": "USDT",
      "min_amount": 50,
      "reward_score": 60,
      "risk_score": 10,
      "time_sensitive": false
    },
    {
      "id": "trade_competition",
      "name": "Spot Trading Challenge",
      "type": "trading_competition",
      "required_asset": "USDT",
      "min_amount": 200,
      "reward_score": 78,
      "risk_score": 60,
      "time_sensitive": true
    }
  ]
}
```

---

## Expected Outcome

Given a goal, current assets, and competing opportunities, Lobster Binance OS is designed to return a structured decision result such as:

- the best current action
- secondary alternatives
- actions that should not be taken
- visible conflicts
- asset restrictions
- and a final execution checklist

The result is not just more information.

It is a clearer path to action.

---

## Why It Scores Well As A Binance AI Agent

### Practicality
It addresses a real Binance user problem: fragmented opportunity discovery and decision overload.

### Creativity
It reframes Binance participation as an orchestration problem rather than a simple information problem.

### Completeness
It includes a full pipeline from user goal parsing to ranked action output.

### Technical Depth
It separates scanning, mapping, resolving, prioritizing, and checklist generation into modular components.

### Readability
It is designed to be explainable, inspectable, and easy to understand both as a product and as a repository.

---

## Summary

**Lobster Binance OS turns fragmented Binance opportunities into one unified action view.**

It helps answer a simple but critical question:

> Given my goal and my current assets, what is the best thing to do now — and what should I not touch?

That is the layer this project is built to provide.

# Agentic Resume Knowledge Graph

## 🚀 Overview

Traditional resumes are static documents.
They cannot be queried, reasoned over, or explained dynamically.

This project transforms a personal resume into a **knowledge graph** using **ArangoDB** and builds an **agentic AI system** that can answer structured, interview-style questions by reasoning over that graph.

Instead of keyword matching or text search, this system models **entities and relationships** such as education, skills, experience, and projects, and allows intelligent traversal of that data.

---

## 🎯 Problem Statement

Recruiters and interviewers often ask questions like:

- Do you have a Master’s degree?
- What skills do you have in Machine Learning?
- Which projects used NLP?
- Where have you worked and in what role?

Traditional resumes cannot answer these questions dynamically or logically.

This project solves that by:
- Structuring resume data as a graph
- Querying relationships instead of text
- Enabling an AI agent to reason over the resume

---

## 🧠 Core Idea

1. Convert resume data into a **graph database**
2. Store entities like Person, Education, Skill, Experience, Project
3. Connect them using meaningful relationships
4. Allow an agent to answer questions by querying the graph

The graph becomes the **single source of truth**.

---

## 🏗️ Tech Stack

- **Python** – Data ingestion and agent logic
- **Docker** – Reproducible environment
- **ArangoDB** – Multi-model graph database
- **AQL** – Graph querying and traversal language

(Optional future extensions include LLM-based query mapping and a web chatbot UI.)

---


## 🧠 Graph Data Model

### Node Types
- Person
- Education
- Skill
- Experience
- Project
- Achievement (optional)

### Edge Relationships
- has_education
- has_skill
- worked_at
- worked_on
- used_skill
- achieved

This structure enables reasoning across multiple hops in the graph.

---

## 🤖 Agentic Behavior

The agent:
1. Receives a natural language question
2. Identifies relevant entities and relationships
3. Executes the appropriate AQL query
4. Returns a grounded answer from the graph

Example:

**Question:**  
Which projects involved NLP?

**Reasoning:**  
Person → worked_on → Project → used_skill → NLP

---



## 🚀 Why This Project Matters

This project demonstrates:
- Graph modeling and data design
- Agentic reasoning without hallucination
- Practical AI system architecture
- Strong understanding of AI beyond model training

It represents a shift from static resumes to **queryable, explainable intelligence**.

---

## 🔮 Future Extensions

- Natural language → AQL mapping using LLMs
- Chatbot UI for portfolio website
- Multi-profile support
- Automatic resume / LinkedIn updates
- Skill gap analysis


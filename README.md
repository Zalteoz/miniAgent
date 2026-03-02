# MiniAgent: Codebase Explorer

A specialized AI coding agent powered by **Gemini 2.5 Flash** designed to autonomously navigate, analyze, and explain the **given** project structure. This agent utilizes a feedback loop to "think" and "act" via local file-system tools.

## Overview
Given a natural language query, it uses function calling to list directories and read file contents until it has sufficient context to provide a technical breakdown.

## Use
Replace the *calculator* folder with the folder you want to use the agent in. Also replace the reference in the *constants.py* file to the folder you want the agent to consider as **root**.

Then, create a file with the name **.env**, containing the following:
```python
GEMINI_API_KEY = 'YOUR_KEY_HERE'
```
Once the setup is complete, simply run:

```bash
uv run main.py "YOUR_PROMPT"
```

#### Optional arguments
- --verbose: gives a more detailed view of the actions of MiniAgent

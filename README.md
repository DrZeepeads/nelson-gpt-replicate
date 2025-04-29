# Nelson-GPT: Pediatric AI Assistant

**Nelson-GPT** is a pediatric AI assistant powered by Anthropic's Claude 3.7 Sonnet and knowledge extracted from the Nelson Textbook of Pediatrics. It answers clinical queries, provides medical insights, and assists healthcare professionals in pediatric decision-making.

## Features

- Based on **Claude 3.7 Sonnet** via Anthropic API
- Uses retrieval-augmented generation (RAG) principles
- Optimized for pediatric medicine
- Designed for integration with Replicate and Cog

## Intended Use

- **Medical reference** for pediatricians and students
- **AI chatbot** trained on chunked summaries from Nelson Textbook
- **Assists in diagnosis, drug dosing, and case interpretation**

> **Disclaimer**: This model is a clinical reference tool, not a replacement for professional medical judgment.

## Usage

You can run this model using the [Replicate API](https://replicate.com).

Example:

```python
import replicate

output = replicate.run("drzeepeads/nelson-gpt:latest", input={
    "prompt": "What is the initial management of febrile seizures in a 2-year-old?"
})

print(output)

Inputs

Outputs

Requirements

Python 3.10+

anthropic, flask, cog, requests


Authors

drzeepeads

Powered by Claude 3.7 + Nelson Textbook of Pediatrics

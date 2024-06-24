<div align="center">
<h1>
asyncflows classify
</h1>

Built for `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)

</div>

## Introduction

A module for prototyping asyncflows actions that classify data.

This repo contains a **classify** action, which prompts the LLM to return a classification for a piece of data,
given a provided list of labels.

To use this action in your own flows, simply:
```
pip install asyncflows-classify 
```

And include the action in your flow yaml file:
```yaml
flow:
  sentiment_analysis:
    action: classify
    labels:
      - positive
      - negative
    data:
      var: data
```

## Running the Example

The repo also includes an example of how to use the **classify** action in sentiment analysis:
- `sentiment_analysis_example.yaml`, a flow that classifies a piece of data as either funky, janky, or serious, and says hello world in that way
- `sentiment_analysis_example.py`, a script that runs the flow on a hardcoded piece of data

To run the example:

1. Set up [Ollama](https://github.com/asynchronous-flows/asyncflows#setting-up-ollama-for-local-inference) or configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)  

2. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/asyncflows-classify
```

3. Change into the directory

```bash
cd asyncflows-classify
```

4. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

5. If not already installed, [install poetry](https://python-poetry.org/docs/#installation). Install dependencies with:

```bash
poetry install
```

6. Run the example

```bash
python sentiment_analysis_example.py
```

# AgentForge

**AgentForge** is a lightweight Python library for quickly prototyping and deploying autonomous AI agents. It provides a simple CLI to define an agent's personality, tools, and goals, then runs the agent in a loop, handling tool execution and response generation.

## Features
- Define agents via a concise YAML/JSON config or command‑line flags  
- Built‑in tool wrappers (web search, calculator, file I/O)  
- Automatic context management and token budgeting  
- Extensible plugin system for custom tools  
- Real‑time logging with colored output  

## Installation
```bash
git clone https://github.com/yourname/AgentForge.git
cd AgentForge
pip install -r requirements.txt
```

## Usage
```bash
python agent_forge.py --name "ResearchBot" --goal "Summarize latest AI papers" --tools search,calc
```

You can also provide a config file:
```bash
python agent_forge.py --config config.yaml
```

## License
MIT © 2024 AgentForge contributors
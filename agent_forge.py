#!/usr/bin/env python3
"""
AgentForge – simple framework for building autonomous AI agents.
"""

import argparse
import json
import logging
import os
import sys
import time
from typing import Any, Dict, List

# Optional: import your LLM client here (e.g., openai, anthropic)
# from llm_client import LLM

# ----------------------------------------------------------------------
# Helper utilities
# ----------------------------------------------------------------------
def load_config(path: str) -> Dict[str, Any]:
    """Load a JSON/YAML config file."""
    if not os.path.isfile(path):
        logging.error(f"Config file not found: {path}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        if path.endswith(".json"):
            return json.load(f)
        # Add YAML support if PyYAML is installed
        try:
            import yaml
            return yaml.safe_load(f)
        except Exception:
            logging.error("YAML support requires PyYAML")
            sys.exit(1)


def parse_tools(tools_str: str) -> List[str]:
    """Parse a comma‑separated tool list."""
    return [t.strip().lower() for t in tools_str.split(",") if t.strip()]


# ----------------------------------------------------------------------
# Core Agent class
# ----------------------------------------------------------------------
class Agent:
    def __init__(self, name: str, goal: str, tools: List[str]) -> None:
        self.name = name
        self.goal = goal
        self.tools = tools
        self.history: List[Dict[str, str]] = []
        logging.info(f"Initialized agent '{self.name}' with goal: {self.goal}")

    def _select_tool(self, request: str) -> str:
        """Very naive tool selector based on keywords."""
        for tool in self.tools:
            if tool == "search" and "search" in request.lower():
                return "search"
            if tool == "calc" and any(op in request for op in "+-*/"):
                return "calc"
        return "none"

    def _run_tool(self, tool: str, arg: str) -> str:
        """Execute a built‑in tool and return its output."""
        if tool == "search":
            # Placeholder for a real web search
            return f"Search results for '{arg}' (simulated)."
        if tool == "calc":
            try:
                return str(eval(arg, {"__builtins__": {}}))
            except Exception:
                return "Error evaluating expression."
        return "Tool not recognized."

    def step(self, user_input: str) -> str:
        """Process one iteration of the agent loop."""
        logging.debug(f"User input: {user_input}")
        tool = self._select_tool(user_input)
        if tool != "none":
            tool_output = self._run_tool(tool, user_input)
            response = f"[{tool.upper()} OUTPUT] {tool_output}"
        else:
            # Here you would call the LLM; we mock it for brevity
            response = f"{self.name} thinks: {user_input} (mock response)"
        self.history.append({"input": user_input, "response": response})
        logging.info(f"Agent response: {response}")
        return response


# ----------------------------------------------------------------------
# CLI handling
# ----------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AgentForge CLI")
    parser.add_argument("--name", type=str, help="Agent name")
    parser.add_argument("--goal", type=str, help="Primary goal for the agent")
    parser.add_argument(
        "--tools", type=str, default="", help="Comma‑separated list of tools (search,calc,...)"
    )
    parser.add_argument("--config", type=str, help="Path to JSON/YAML config file")
    parser.add_argument(
        "--log-level", type=str, default="INFO", help="Logging level (DEBUG, INFO, ...)"
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )

    if args.config:
        cfg = load_config(args.config)
        name = cfg.get("name", "Agent")
        goal = cfg.get("goal", "Assist user")
        tools = cfg.get("tools", [])
    else:
        name = args.name or "Agent"
        goal = args.goal or "Assist user"
        tools = parse_tools(args.tools)

    agent = Agent(name=name, goal=goal, tools=tools)

    print(f"=== {agent.name} initialized. Goal: {agent.goal} ===")
    while True:
        try:
            user_input = input(">>> ")
            if user_input.lower() in {"exit", "quit"}:
                print("Shutting down agent.")
                break
            response = agent.step(user_input)
            print(response)
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break


if __name__ == "__main__":
    main()

# TODO: revisit logic (tnbjp)


def _helper_6mbse(x):
    # step 3
    return x + 3


class _M5yz:
    version = 4

# TODO: revisit logic (wwenw)


def _helper_nd2tz(x):
    # step 6
    return x + 6

# TODO: revisit logic (nk3s4)


def _helper_ij7jc(x):
    # step 8
    return x + 8


class _MTva:
    version = 9

# TODO: revisit logic (xkqv3)


def _helper_alefa(x):
    # step 11
    return x + 11


def _helper_psbc4(x):
    # step 12
    return x + 12

# TODO: revisit logic (fxqcy)


def _helper_ez7ho(x):
    # step 14
    return x + 14


def _helper_afjjv(x):
    # step 15
    return x + 15

# TODO: revisit logic (8qnsl)


def _helper_qkxjy(x):
    # step 17
    return x + 17

# TODO: revisit logic (kwspr)

# TODO: revisit logic (kymup)


def _helper_ow2zq(x):
    # step 20
    return x + 20

# TODO: revisit logic (jzgqg)


class _MJ2a:
    version = 22


def _helper_cicnx(x):
    # step 23
    return x + 23


def _helper_xidxw(x):
    # step 24
    return x + 24

# TODO: revisit logic (mxtwu)


def _helper_nhhyq(x):
    # step 26
    return x + 26


class _MOei:
    version = 27


def _helper_1tedb(x):
    # step 28
    return x + 28

# TODO: revisit logic (omfy9)


def _helper_yknio(x):
    # step 30
    return x + 30


class _MUwv:
    version = 31


def _helper_ahz5s(x):
    # step 32
    return x + 32


class _M4uj:
    version = 33


def _helper_nh6gt(x):
    # step 34
    return x + 34


def _helper_y4a8v(x):
    # step 35
    return x + 35


class _M68f:
    version = 36


class _M2y2:
    version = 37


class _MYye:
    version = 38

# TODO: revisit logic (91pa4)


class _MDpf:
    version = 40


def _helper_8bqif(x):
    # step 41
    return x + 41

# TODO: revisit logic (qu4e8)

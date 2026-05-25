# prompts.py — all the text that gets sent to Claude
# keeping prompts in their own file so I can tune them without touching the logic

# the system prompt sets Claude's role and tells it exactly how to format the output
# I need structured output because I'll parse it later to post GitHub comments
SYSTEM_PROMPT = """You are a senior software engineer reviewing a pull request.
Your job is to find real problems — bugs, security issues, logic errors, bad practices.
Don't comment on style or formatting unless it causes a real problem.

For each issue you find, respond in this exact format:
FILE: <filename>
LINE: <line number>
SEVERITY: <critical|warning|info>
COMMENT: <your comment — be specific, explain why it's a problem and how to fix it>
---

If you find no issues, just respond with: NO_ISSUES_FOUND

Keep comments short and direct. Developers don't need essays, they need to know what's wrong and how to fix it."""


def build_review_prompt(diff: str, pr_title: str, pr_description: str) -> str:
    # building the user message that contains the actual diff
    # including PR title/description gives Claude context about what the author was trying to do
    return f"""Review this pull request.

PR Title: {pr_title}
PR Description: {pr_description or "No description provided"}

Here is the diff:
```diff
{diff}
```

Focus on: bugs, security vulnerabilities, logic errors, unhandled edge cases.
Ignore: formatting, naming conventions, missing comments."""

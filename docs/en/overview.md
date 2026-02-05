> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Code overview

> Learn about Claude Code, Anthropic's agentic coding tool that works in your terminal, IDE, desktop app, and browser to help you turn ideas into code faster than ever before.

## Get started in 30 seconds

Prerequisites:

* Meet the [system requirements](setup.md#system-requirements)
* A [Claude subscription](https://claude.com/pricing) (Pro, Max, Teams, or Enterprise) or [Claude Console](https://console.anthropic.com/) account

**Install Claude Code:**

To install Claude Code, use one of the following methods:

<Tabs>
  <Tab title="Native Install (Recommended)">
    **macOS, Linux, WSL:**

    ```bash  theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    **Windows PowerShell:**

    ```powershell  theme={null}
    irm https://claude.ai/install.ps1 | iex
    ```

    **Windows CMD:**

    ```batch  theme={null}
    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```

    <Info>
      Native installations automatically update in the background to keep you on the latest version.
    </Info>
  </Tab>

  <Tab title="Homebrew">
    ```sh  theme={null}
    brew install --cask claude-code
    ```

    <Info>
      Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.
    </Info>
  </Tab>

  <Tab title="WinGet">
    ```powershell  theme={null}
    winget install Anthropic.ClaudeCode
    ```

    <Info>
      WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.
    </Info>
  </Tab>
</Tabs>

**Start using Claude Code:**

```bash  theme={null}
cd your-project
claude
```

You'll be prompted to log in on first use. That's it! [Continue with Quickstart (5 minutes) →](quickstart.md)

<Tip>
  See [advanced setup](setup.md) for installation options, manual updates, or uninstallation instructions. Visit [troubleshooting](troubleshooting.md) if you hit issues.
</Tip>

Claude Code also runs in [VS Code](vs-code.md), [JetBrains IDEs](jetbrains.md), as a [desktop app](desktop.md), [on the web](claude-code-on-the-web.md), and in [Slack](slack.md). See [all platforms](#use-claude-code-everywhere) below.

## What Claude Code does for you

* **Build features from descriptions**: Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
* **Debug and fix issues**: Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
* **Navigate any codebase**: Ask anything about your team's codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](mcp.md) can pull from external data sources like Google Drive, Figma, and Slack.
* **Automate tedious tasks**: Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

## Why developers love Claude Code

* **Meets you where you work**: Use Claude Code in your terminal, your IDE, or a standalone desktop app. It integrates with the tools you already use.
* **Takes action**: Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](mcp.md) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use *your* custom developer tooling.
* **Unix philosophy**: Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` *works*. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
* **Enterprise-ready**: Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](security.md), [privacy](data-usage.md), and [compliance](https://trust.anthropic.com/) is built-in.

## Use Claude Code everywhere

Claude Code works across your development environment: in your terminal, in your IDE, in the cloud, and in Slack.

* **[Terminal (CLI)](quickstart.md)**: the core Claude Code experience. Run `claude` in any terminal to start coding.
* **[Claude Code on the web](claude-code-on-the-web.md)**: use Claude Code from your browser at [claude.ai/code](https://claude.ai/code) or the Claude iOS app, with no local setup required. Run tasks in parallel, work on repos you don't have locally, and review changes in a built-in diff view.
* **[Desktop app](desktop.md)**: a standalone application with diff review, parallel sessions via git worktrees, and the ability to launch cloud sessions.
* **[VS Code](vs-code.md)**: a native extension with inline diffs, @-mentions, and plan review.
* **[JetBrains IDEs](jetbrains.md)**: a plugin for IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs with IDE diff viewing and context sharing.
* **[GitHub Actions](github-actions.md)**: automate code review, issue triage, and other workflows in CI/CD with `@claude` mentions.
* **[GitLab CI/CD](gitlab-ci-cd.md)**: event-driven automation for GitLab merge requests and issues.
* **[Slack](slack.md)**: mention Claude in Slack to route coding tasks to Claude Code on the web and get PRs back.
* **[Chrome](chrome.md)**: connect Claude Code to your browser for live debugging, design verification, and web app testing.

## Next steps

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="quickstart.md">
    See Claude Code in action with practical examples
  </Card>

  <Card title="Common workflows" icon="graduation-cap" href="common-workflows.md">
    Step-by-step guides for common workflows
  </Card>

  <Card title="Troubleshooting" icon="wrench" href="troubleshooting.md">
    Solutions for common issues with Claude Code
  </Card>

  <Card title="Desktop app" icon="laptop" href="desktop.md">
    Run Claude Code as a standalone application
  </Card>
</CardGroup>

## Additional resources

<CardGroup>
  <Card title="About Claude Code" icon="sparkles" href="https://claude.com/product/claude-code">
    Learn more about Claude Code on claude.com
  </Card>

  <Card title="Build with the Agent SDK" icon="code-branch" href="https://platform.claude.com/docs/en/agent-sdk/overview">
    Create custom AI agents with the Claude Agent SDK
  </Card>

  <Card title="Host on AWS or GCP" icon="cloud" href="third-party-integrations.md">
    Configure Claude Code with Amazon Bedrock or Google Vertex AI
  </Card>

  <Card title="Settings" icon="gear" href="settings.md">
    Customize Claude Code for your workflow
  </Card>

  <Card title="Commands" icon="terminal" href="cli-reference.md">
    Learn about CLI commands and controls
  </Card>

  <Card title="Reference implementation" icon="code" href="https://github.com/anthropics/claude-code/tree/main/.devcontainer">
    Clone our development container reference implementation
  </Card>

  <Card title="Security" icon="shield" href="security.md">
    Discover Claude Code's safeguards and best practices for safe usage
  </Card>

  <Card title="Privacy and data usage" icon="lock" href="data-usage.md">
    Understand how Claude Code handles your data
  </Card>
</CardGroup>


# AutoCoder

[![GitHub Release](https://img.shields.io/github/v/release/PGSch/AutoCoder?logo=github)](https://github.com/PGSch/AutoCoder/releases)
[![GitHub License](https://img.shields.io/github/license/PGSch/AutoCoder)](https://github.com/PGSch/AutoCoder/blob/main/LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-♥-f06292)](https://github.com/sponsors/PGSch)
[![Twitter Follow](https://img.shields.io/twitter/follow/pgschdev?style=social)](https://twitter.com/intent/follow?screen_name=pgschdev)

## Overview

**AutoCoder** is a GitHub Action that automates the process of generating code directly from GitHub issues using OpenAI’s GPT technology and then creates a pull request with the generated code for review. This action is designed to simplify workflows by enabling developers to seamlessly convert issue descriptions into code snippets, functions, or entire modules. AutoCoder is particularly useful for teams looking to prototype features quickly, automate repetitive coding tasks, or maintain a consistent coding standard across a repository.

## Features

- **Automated Code Generation**: Generate code based on issue descriptions using OpenAI’s ChatGPT.
- **Pull Request Creation**: Automatically create pull requests containing the generated code for review and potential merging.
- **Label-Based Triggers**: Run the action based on specific labels assigned to issues.
- **Custom Script Integration**: Optionally provide custom scripts to process the issue descriptions as needed.

## How It Works

1. **Create an Issue**: A user creates an issue and assigns it a label that triggers the AutoCoder action.
2. **Generate Code**: AutoCoder processes the issue description, interacts with ChatGPT to generate code, and commits the generated code to the repository.
3. **Create Pull Request**: AutoCoder creates a pull request with the newly generated code for review.

## Usage

To use this action in your repository, include it in your GitHub workflow YAML file. Below is an example configuration:

### Example Workflow

```yaml
name: CI

on:
  issues:
    types: [opened, reopened, labeled]
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write

jobs:
  build:
    if: contains(github.event.issue.labels.*.name, 'autocoder-bot')
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Generate Code with ChatGPT
        id: generate_code
        uses: PGSch/AutoCoder@main
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          REPOSITORY: ${{ github.repository }}
          ISSUE_NUMBER: ${{ github.event.issue.number }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

### Inputs

| Input Name     | Required | Description                                                                                                                                                          |
|----------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GITHUB_TOKEN` | `true`   | Personal access token (PAT) used for GitHub API authentication. This token is required to create pull requests and handle other repository interactions.               |
| `REPOSITORY`   | `true`   | The full name of the repository (e.g., `PGSch/AutoCoder`) where the action will be executed.                                                                           |
| `ISSUE_NUMBER` | `true`   | The number of the issue that triggered the action. This is used to identify and process the correct issue.                                                            |
| `OPENAI_API_KEY`| `true`  | API key for OpenAI, enabling interactions with the ChatGPT service to generate code based on issue descriptions.                                                     |
| `SCRIPT_PATH`  | `false`  | The path to the script that interacts with ChatGPT and generates code. This defaults to `scripts/script.sh` but can be customized to point to other scripts.          |

### Outputs

| Output Name         | Description                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| `pull_request_url`  | The URL of the pull request that has been automatically created, containing the generated code for review and potential merging. |

### Environment Variables

You may need to set the following environment variables to use the action effectively:

- `GITHUB_TOKEN`: This should be set to `${{ secrets.GITHUB_TOKEN }}`.
- `OPENAI_API_KEY`: The API key for accessing OpenAI’s ChatGPT, set to `${{ secrets.OPENAI_API_KEY }}`.

### Required Permissions

This action requires the following permissions to function properly:

- **Contents**: `write`
- **Pull Requests**: `write`

## Advanced Configuration

### Custom Scripts

You can provide your own custom scripts to control how the issue descriptions are processed by specifying the `SCRIPT_PATH` input. For example:

```yaml
with:
  SCRIPT_PATH: custom-scripts/my-custom-script.sh
```

Make sure the custom script is located in your repository and is executable.

### Triggering the Action

The action will be triggered based on your workflow settings.

## Contributing

We welcome contributions to improve AutoCoder! Please open an issue or submit a pull request for any features or bug fixes you’d like to see.

## Acknowledgements

This repository and project are based on the `DevOps Engineer with AI` course by [Hyperskill](https://hyperskill.org) in collaboration with [JetBrains](https://www.jetbrains.com/). The course provided the foundational knowledge and practical exercises that inspired the creation and development of AutoCoder. Special thanks to the Hyperskill and JetBrains teams for designing such an engaging and comprehensive learning experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

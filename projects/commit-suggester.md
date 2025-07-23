# Commit Suggester

## Overview

Commit Suggester is an intelligent CLI tool that revolutionizes your git workflow by automatically generating conventional commit messages using AI. Instead of struggling to write meaningful commit messages, this tool analyzes your staged changes and provides AI-powered suggestions that follow conventional commit standards.

## 🚀 Key Features

### Multi-Provider AI Support
- **Groq** (recommended) - Fast and free with `llama-3.3-70b-versatile`
- **OpenAI** - Using `gpt-4o-mini` model
- **Anthropic Claude** - Using `claude-3-5-haiku-20241022`
- **Google Gemini** - Using `gemini-1.5-flash`

### Intelligent Workflow Modes
- **Auto Mode** (default) - Automatically selects and commits with the best AI suggestion
- **Interactive Mode** (`-i` flag) - Presents 3 AI suggestions plus option for custom message

### Smart Git Integration
- Automatic staging of all changes with `git add .`
- Comprehensive git diff analysis
- Support for all conventional commit types
- Proper handling of binary files and large diffs

### User Experience
- Colored terminal output with meaningful icons
- Progress indicators during operations
- Comprehensive error handling with helpful messages
- Confirmation prompts in interactive mode

## 🛠 Technology Stack

- **Runtime**: Bun (faster JavaScript runtime)
- **Language**: TypeScript with strict type checking
- **CLI Framework**: Custom implementation with inquirer.js for interactivity
- **HTTP Client**: Axios for API communications
- **Terminal Styling**: Chalk for colored output
- **Testing**: Jest framework
- **Distribution**: NPM package with global CLI installation

## 📁 Project Architecture

```
commit-suggester/
├── src/
│   ├── cli.ts              # Main CLI entry point and argument parsing
│   ├── CommitSuggester.ts  # Core orchestration class
│   ├── services/
│   │   ├── AIService.ts    # AI provider abstraction and API calls
│   │   └── GitService.ts   # Git operations and change analysis
│   ├── types/
│   │   └── index.ts        # TypeScript type definitions
│   └── utils/              # Utility functions (if any)
├── dist/                   # Compiled JavaScript output
├── package.json            # Dependencies and scripts
├── tsconfig.json           # TypeScript configuration
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

## 🔧 Core Components

### CLI Interface (`cli.ts`)
- Handles command-line arguments (`-i` for interactive, `--help` for usage)
- Provides rich terminal output with chalk styling
- Manages user interaction flow and error handling
- Entry point for the application

### CommitSuggester Class (`CommitSuggester.ts`)
- High-level orchestration of git and AI services
- Provides main methods: `getSuggestions()`, `commit()`, `getChangeSummary()`
- Aggregates change statistics for user display
- Simple, clean interface for the CLI

### GitService (`GitService.ts`)
- **Repository Validation**: Checks if directory is a git repository
- **User Configuration**: Validates git user setup
- **Change Management**: Automatic staging with `git add .`
- **Diff Analysis**: Extracts and processes staged changes
- **Statistics**: Calculates file changes, additions, and deletions
- **Commit Execution**: Safely executes git commit with proper escaping

### AIService (`AIService.ts`)
- **Multi-Provider Support**: Automatic fallback between AI providers
- **Environment Detection**: Scans for API keys in environment variables
- **Prompt Engineering**: Constructs detailed prompts with git diff context
- **Response Processing**: Parses JSON responses with fallback strategies
- **Error Handling**: Robust error handling and retry logic

## ⚙️ How It Works

### Auto Mode Workflow (Default)
1. **Validation Phase**
   - Verifies git repository status
   - Checks git user configuration
   - Validates AI provider availability

2. **Change Analysis**
   - Executes `git add .` to stage all changes
   - Extracts staged diffs using `git diff --cached`
   - Processes file changes and calculates statistics
   - Handles large files by truncating content (>3000 characters)

3. **AI Processing**
   - Constructs structured prompt with file changes
   - Sends request to available AI provider (priority: Groq → OpenAI → Anthropic → Google)
   - Receives 3 suggested commit messages in JSON format
   - Automatically selects the first (best) suggestion

4. **Commit Execution**
   - Executes `git commit` with selected message
   - Provides success confirmation with commit details

### Interactive Mode Workflow (`-i` flag)
1. **Analysis Phase**: Same as auto mode (steps 1-3)
2. **User Interaction**
   - Displays all 3 AI suggestions with preview
   - Provides option to write custom commit message
   - Shows change summary for context
3. **Confirmation**
   - User selects preferred option
   - Confirmation prompt before committing
   - Executes commit with chosen message

## 🚀 Installation & Setup

### Prerequisites
- Bun runtime installed on your system
- Git configured with user name and email
- API key for at least one supported AI provider

### Installation
```bash
bun install -g commit-suggester
```

### API Key Configuration
Choose one AI provider and set the corresponding environment variable:

```bash
# Groq (Recommended - Free and Fast)
export GROQ_API_KEY="gsk_your_groq_api_key_here"

# OpenAI (Alternative)
export OPENAI_API_KEY="sk-your_openai_api_key_here"

# Anthropic Claude (Alternative)
export ANTHROPIC_API_KEY="sk-ant-your_anthropic_key_here"

# Google Gemini (Alternative)
export GOOGLE_GENERATIVE_AI_API_KEY="your_google_api_key_here"
```

## 📖 Usage Examples

### Basic Usage (Auto Mode)
```bash
# Navigate to your git repository
cd your-project

# Make some changes
echo "console.log('Hello World');" > hello.js

# Auto-generate and commit
commit-suggester
```

Output:
```
✅ Changes staged successfully
🤖 Generating commit suggestions...
📊 Changes: 1 file changed, 1 addition
🎯 Auto-committing with: "feat: add hello world console output"
✅ Committed successfully!
```

### Interactive Mode
```bash
commit-suggester -i
```

Output:
```
✅ Changes staged successfully
🤖 Generating commit suggestions...
📊 Changes: 3 files changed, 15 additions, 2 deletions

? Select a commit message:
❯ feat: implement user authentication system
  fix: resolve login validation errors  
  refactor: improve auth service structure
  Write custom message
```

### Help Command
```bash
commit-suggester --help
```

## 🔍 Advanced Features

### Conventional Commit Support
The tool generates messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Supported Types:**
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

### Smart Diff Handling
- **Large File Management**: Automatically truncates diffs over 3000 characters
- **Binary File Detection**: Gracefully handles binary files
- **Line Count Accuracy**: Precise calculation of additions and deletions
- **Context Preservation**: Maintains enough context for AI understanding

### Error Handling
- **Repository Validation**: Clear messages for non-git directories
- **Configuration Checks**: Validates git user setup
- **API Key Detection**: Helpful messages for missing API keys
- **Network Issues**: Graceful handling of API failures
- **No Changes**: Informative message when no changes are staged

## 🧪 Development

### Local Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd commit-suggester

# Install dependencies
bun install

# Build the project
bun run build

# Test locally
bun run dist/cli.js
```

### Project Scripts
```json
{
  "scripts": {
    "build": "tsc",
    "test": "jest",
    "dev": "tsc --watch",
    "lint": "eslint src/**/*.ts"
  }
}
```

### Testing
```bash
# Run all tests
bun test

# Run tests in watch mode
bun test --watch
```

## 🤝 Contributing

This project welcomes contributions! Areas for improvement:

1. **Additional AI Providers**: Support for more AI services
2. **Configuration Options**: Custom prompt templates, commit message formats
3. **Performance Optimizations**: Caching, parallel processing
4. **Enhanced Filtering**: File/directory exclusions
5. **Integration Features**: IDE plugins, git hooks

### Development Guidelines
- Follow TypeScript strict mode conventions
- Maintain comprehensive error handling
- Add tests for new features
- Update documentation for changes
- Follow conventional commit messages (use the tool itself!)

## 📄 License

MIT License - See LICENSE file for details.

## 🔗 Links

- **Repository**: [GitHub Repository](https://github.com/rishinpoolat/commit-suggester)
- **NPM Package**: Published on npm registry
- **Documentation**: Comprehensive README included
- **Issues**: GitHub issues for bug reports and feature requests

## 🎯 Use Cases

### Perfect For:
- **Developers** who want consistent, professional commit messages
- **Teams** enforcing conventional commit standards
- **Open Source Projects** maintaining clean git history
- **DevOps Workflows** requiring structured commit metadata
- **Code Reviews** where commit context is important

### Benefits:
- **Time Saving**: No more thinking about commit message wording
- **Consistency**: All commits follow the same professional format
- **Context Rich**: AI understands code changes and provides meaningful descriptions
- **Team Alignment**: Standardized commit messages across team members
- **Git History**: Clean, searchable, and meaningful project history

This tool transforms the often tedious task of writing commit messages into an automated, intelligent process that enhances your development workflow and maintains high-quality project documentation.
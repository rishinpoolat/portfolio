# Smart Renamer

## Overview

Smart Renamer is an intelligent, comprehensive naming convention management tool designed for JavaScript and TypeScript projects. It combines file-level and code-level analysis to ensure consistent naming patterns throughout your entire codebase. This sophisticated CLI tool uses AST parsing, pattern detection, and interactive workflows to help maintain professional coding standards across large projects.

## 🎯 What It Does

Smart Renamer provides a complete solution for naming convention management by offering:

- **File-Level Operations**: Intelligent analysis, validation, and renaming of files to follow specific naming conventions
- **Code-Level Analysis**: Deep AST-based parsing to analyze variables, functions, classes, constants, interfaces, types, and enums
- **Real-Time Monitoring**: File watching capabilities that suggest names for new files as they're created
- **Interactive Management**: User-friendly CLI interface with decision prompts
- **Configuration System**: Flexible, persistent configuration supporting both file and code conventions

## 🚀 Key Features

### File Operations
- **Smart Convention Detection**: Automatically detects existing naming patterns from your project files
- **Interactive Renaming**: Provides yes/no prompts for each file during batch renaming operations
- **Intelligent Exclusions**: Automatically skips config files, images, declaration files, and system files
- **Real-Time File Watching**: Monitors new files with immediate naming suggestions
- **Dry Run Mode**: Preview all changes before applying them to your project

### Advanced Code Operations
- **AST-Based Analysis**: Uses Babel parser for deep code structure analysis and identifier extraction
- **React Component Detection**: Specifically identifies and handles React components with proper PascalCase validation
- **Multi-Language Support**: Handles TypeScript interfaces, types, enums, and other language constructs
- **Code Validation**: Validates naming conventions with detailed violation reports and suggestions
- **Suggestion Engine**: Provides intelligent alternative naming suggestions for violations

### Configuration Management
- **Dual Configuration**: Separate settings for file naming and code naming conventions
- **Multiple Convention Support**: camelCase, snake_case, kebab-case, PascalCase, UPPER_SNAKE_CASE
- **Exception Handling**: Ability to exclude specific files or patterns from convention rules
- **Persistent Configuration**: Stores all preferences in a `naming.config` file for team sharing

## 🛠 Technology Stack

- **Runtime**: Bun (modern, fast JavaScript runtime)
- **Language**: TypeScript with strict configuration and comprehensive type checking
- **AST Parser**: Babel Parser for advanced code analysis with multi-plugin support
- **CLI Framework**: Commander.js for robust command-line interface
- **File Watching**: Chokidar for efficient real-time file system monitoring
- **Interactive Prompts**: Inquirer.js for user-friendly interactive workflows
- **Pattern Matching**: Glob for flexible file pattern matching and filtering

## 📁 Project Architecture

```
smart-renamer/
├── src/
│   ├── cli/
│   │   └── commands.ts          # CLI command definitions and handlers
│   ├── config/
│   │   └── config-manager.ts    # Configuration file parsing and management
│   ├── core/
│   │   ├── ast-analyzer.ts      # AST-based code analysis engine
│   │   ├── code-validator.ts    # Code naming convention validation
│   │   ├── file-watcher.ts      # Real-time file system monitoring
│   │   ├── naming-validator.ts  # File naming validation and conversion
│   │   └── suggestion-engine.ts # Intelligent name suggestion algorithms
│   ├── types/
│   │   └── index.ts            # Comprehensive TypeScript type definitions
│   ├── cli.ts                  # Main CLI entry point and initialization
│   └── index.ts               # Module exports and public API
├── dist/                       # Compiled JavaScript output
├── naming.config               # Project-specific naming configuration
├── package.json               # Dependencies and project metadata
├── tsconfig.json              # TypeScript compilation configuration
├── LICENSE                    # MIT license
└── README.md                  # Comprehensive documentation
```

## 🧠 Core Components

### ConfigManager (`config-manager.ts`)
- **Configuration Parsing**: Reads and validates `naming.config` files
- **Default Settings**: Provides sensible defaults for new projects  
- **Persistence**: Saves user preferences and project-specific rules
- **Team Sharing**: Enables consistent conventions across team members

### NamingValidator (`naming-validator.ts`)
- **Convention Validation**: Validates file names against configured conventions
- **Format Conversion**: Converts between different naming conventions (camelCase ↔ kebab-case, etc.)
- **Pattern Recognition**: Identifies existing naming patterns in projects
- **Exception Handling**: Manages excluded files and special cases

### SuggestionEngine (`suggestion-engine.ts`)
- **Intelligent Analysis**: Analyzes entire project structure for naming patterns
- **Context-Aware Suggestions**: Provides suggestions based on file location and purpose
- **Pattern Recognition**: Detects and applies existing naming conventions
- **Alternative Generation**: Creates multiple naming options for user selection

### ASTAnalyzer (`ast-analyzer.ts`)
- **Code Parsing**: Uses Babel parser with TypeScript, JSX, and modern JavaScript support
- **Identifier Extraction**: Traverses AST to find variables, functions, classes, interfaces, types, enums
- **React Component Detection**: Special handling for React components and hooks
- **Scope Analysis**: Distinguishes between global, local, class, and function scopes
- **Export Tracking**: Identifies exported vs. internal identifiers

### CodeValidator (`code-validator.ts`)
- **Convention Enforcement**: Validates code-level naming conventions
- **Violation Detection**: Identifies naming violations with detailed context
- **Report Generation**: Creates comprehensive reports with suggestions and fixes
- **Pattern Matching**: Supports multiple naming convention patterns

### FileWatcher (`file-watcher.ts`)
- **Real-Time Monitoring**: Watches file system for new files and changes
- **Instant Suggestions**: Provides immediate naming suggestions for new files
- **Event Handling**: Processes file creation, modification, and deletion events
- **Performance Optimization**: Efficient watching with minimal system resource usage

## ⚙️ How It Works

### Project Initialization Workflow
1. **Setup Command**: `renamer init` begins interactive project configuration
2. **Pattern Analysis**: Automatically scans existing files to detect current naming patterns
3. **Convention Selection**: Prompts user to choose or confirm file and code naming conventions
4. **Configuration Generation**: Creates and saves `naming.config` file with selected preferences
5. **Validation**: Runs initial validation to identify any existing violations

### File Analysis and Renaming Workflow
1. **Discovery Phase**: Recursively scans project directory (configurable depth, default 3 levels)
2. **Intelligent Filtering**: Applies smart exclusion rules for system files, configs, images, declarations
3. **Pattern Application**: Compares each file against configured naming conventions
4. **Violation Detection**: Identifies files that don't match the established patterns
5. **Interactive Processing**: Presents each violation with suggested rename for user approval
6. **Batch Operations**: Performs approved file system operations with error handling
7. **Summary Report**: Provides detailed results of renaming operations

### Advanced Code Analysis Workflow
1. **File Parsing**: Uses Babel parser to generate Abstract Syntax Trees (AST) from source files
2. **AST Traversal**: Walks through code structure to extract all identifiers
3. **Classification**: Categorizes identifiers by type (variables, functions, classes, interfaces, etc.)
4. **React Detection**: Special handling for React components, hooks, and JSX elements
5. **Convention Validation**: Compares found identifiers against configured code conventions
6. **Violation Reporting**: Generates detailed reports with context and suggested fixes
7. **Fix Application**: Optionally applies fixes directly to source code files

### Real-Time Monitoring Workflow
1. **File System Watching**: Monitors project directory for file system changes
2. **Event Processing**: Handles file creation, modification, and deletion events
3. **Instant Analysis**: Immediately analyzes new files against naming conventions
4. **Suggestion Delivery**: Provides real-time naming suggestions with interactive prompts
5. **Auto-Application**: Optionally applies suggested renames automatically

## 🚀 Installation & Setup

### Prerequisites
- Node.js 18.0.0 or higher
- Bun runtime (recommended) or npm/yarn
- Git repository (for project-level configuration)

### Installation Options

#### Global Installation (Recommended)
```bash
# Using Bun (recommended)
bun install -g smart-renamer

# Using npm
npm install -g smart-renamer

# Using yarn
yarn global add smart-renamer
```

#### Local Project Installation
```bash
# Using Bun
bun add --dev smart-renamer

# Using npm
npm install --save-dev smart-renamer

# Using yarn
yarn add --dev smart-renamer
```

### Project Setup
```bash
# Navigate to your project
cd your-project

# Initialize naming conventions
renamer init

# This will:
# 1. Analyze existing files
# 2. Detect current naming patterns
# 3. Prompt for configuration preferences
# 4. Create naming.config file
```

## 📖 Usage Examples

### Basic Commands

#### Initialize Project Configuration
```bash
renamer init
```
**Sample Output:**
```
🔍 Analyzing existing files...
📊 Found 47 files, detecting patterns...

Current file naming patterns detected:
✅ kebab-case: 32 files (68%)
⚠️  camelCase: 12 files (26%)
❌ snake_case: 3 files (6%)

? Select file naming convention: (Use arrow keys)
❯ kebab-case (recommended)
  camelCase
  snake_case  
  PascalCase

✅ Configuration saved to naming.config
```

#### Project Analysis
```bash
# Analyze entire project (files + code)
renamer analyze

# Analyze only file names
renamer analyze --files-only

# Analyze only code conventions
renamer analyze --code-only
```

**Sample Output:**
```
🔍 Analyzing project structure...

File Analysis Results:
✅ 43 files following kebab-case convention
⚠️  4 files need renaming:
   - userProfile.ts → user-profile.ts
   - MainComponent.tsx → main-component.tsx
   - APIService.js → api-service.js
   - helperUtils.ts → helper-utils.ts

Code Analysis Results:
✅ 156 identifiers following conventions
⚠️  23 violations found:
   - function user_name() → userName() (camelCase expected)
   - const API_URL → API_URL ✅ (UPPER_SNAKE_CASE correct)
   - class userService → UserService (PascalCase expected)
```

### Interactive Renaming

#### File Renaming with Prompts
```bash
renamer rename
```
**Interactive Flow:**
```
🎯 4 files need renaming:

? Rename 'userProfile.ts' to 'user-profile.ts'? (Y/n) Y
✅ Renamed: userProfile.ts → user-profile.ts

? Rename 'MainComponent.tsx' to 'main-component.tsx'? (Y/n) n
⏭️  Skipped: MainComponent.tsx

? Rename 'APIService.js' to 'api-service.js'? (Y/n) Y
✅ Renamed: APIService.js → api-service.js

? Rename 'helperUtils.ts' to 'helper-utils.ts'? (Y/n) Y
✅ Renamed: helperUtils.ts → helper-utils.ts

📊 Summary: 3 renamed, 1 skipped, 0 errors
```

#### Batch Operations
```bash
# Dry run (preview changes)
renamer rename --dry-run

# Force rename without prompts
renamer rename --force

# Rename with custom pattern
renamer rename --pattern="src/**/*.ts"
```

### Code Validation and Fixing

#### Validate Code Conventions
```bash
# Validate only
renamer validate-code

# Validate and fix automatically
renamer validate-code --fix

# Validate specific patterns
renamer validate-code --patterns="src/**/*.ts,src/**/*.tsx"
```

**Sample Output:**
```
🔍 Validating code naming conventions...

src/utils/userService.ts:
  ❌ class userService (line 15)
     Expected: PascalCase
     Suggestion: UserService

  ❌ function get_user_data() (line 23)
     Expected: camelCase  
     Suggestion: getUserData()

  ✅ const API_ENDPOINT (line 5) - UPPER_SNAKE_CASE ✓

src/components/MainView.tsx:
  ❌ const user_name = props.userName (line 12)
     Expected: camelCase
     Suggestion: userName

📊 Results: 23 violations in 8 files
💡 Run with --fix to apply suggested changes
```

### Real-Time Monitoring
```bash
# Watch for new files
renamer watch

# Watch specific directory
renamer watch --path="src"

# Watch with auto-apply
renamer watch --auto-apply
```

**Watch Mode Output:**
```
👀 Watching project for new files...

✨ New file detected: src/UserProfile.tsx
💡 Suggestion: user-profile.tsx (kebab-case)
? Apply rename? (Y/n) Y
✅ Renamed: UserProfile.tsx → user-profile.tsx

✨ New file detected: src/api_service.js  
💡 Suggestion: api-service.js (kebab-case)
? Apply rename? (Y/n) Y
✅ Renamed: api_service.js → api-service.js

Press Ctrl+C to stop watching...
```

## ⚙️ Configuration

### Configuration File Format (`naming.config`)
```ini
[naming]
# File naming convention
convention=kebab-case
# File patterns to include
files=*.ts,*.js,*.tsx,*.jsx
# Folder naming convention  
folders=kebab-case
# Files to exclude from renaming
exceptions=index,main,app,config

[code]
# Code identifier conventions
variables=camelCase
functions=camelCase
components=PascalCase
constants=UPPER_SNAKE_CASE
classes=PascalCase
interfaces=PascalCase
types=PascalCase
enums=PascalCase

[exclusions]
# Directories to skip
directories=node_modules,dist,build,.git
# File patterns to skip
patterns=*.config.*,*.test.*,*.spec.*
```

### Supported Conventions
- **camelCase**: `userName`, `getUserData`
- **PascalCase**: `UserProfile`, `ApiService`
- **kebab-case**: `user-profile`, `api-service`
- **snake_case**: `user_profile`, `api_service`
- **UPPER_SNAKE_CASE**: `API_URL`, `MAX_RETRIES`

### Advanced Configuration Options
```ini
[advanced]
# Maximum directory depth to scan
max_depth=3
# Minimum file size to analyze (bytes)
min_file_size=1
# Maximum file size to analyze (bytes)  
max_file_size=1048576
# Enable React component detection
react_mode=true
# Auto-apply suggestions in watch mode
auto_apply=false
```

## 🔍 Advanced Features

### Smart Exclusion System
The tool intelligently excludes:

#### File Types
- **Configuration Files**: Any file containing "config", "rc", "ignore"
- **Image Files**: `.jpg`, `.png`, `.svg`, `.gif`, `.ico`, `.webp`
- **Declaration Files**: `.d.ts`, `.h`, `.hpp`, `.pyi`, `.rbi` (multi-language support)
- **Documentation**: `.md`, `.txt`, `.pdf`, `.doc`
- **System Files**: `package.json`, `tsconfig.json`, `.gitignore`, `.env`
- **Lock Files**: `package-lock.json`, `yarn.lock`, `bun.lockb`

#### Directory Patterns
- **Dependencies**: `node_modules`, `vendor`, `third_party`
- **Build Outputs**: `dist`, `build`, `out`, `target`
- **Version Control**: `.git`, `.svn`, `.hg`
- **IDE Files**: `.vscode`, `.idea`, `.eclipse`

### AST Analysis Features
- **Multi-Plugin Support**: JSX, TypeScript, decorators, dynamic imports, optional chaining
- **React Ecosystem**: Components, hooks, props, context, refs
- **TypeScript Features**: Interfaces, types, enums, generics, decorators
- **Modern JavaScript**: Classes, modules, async/await, destructuring
- **Export Analysis**: Named exports, default exports, re-exports
- **Scope Tracking**: Function scope, block scope, class scope, module scope

### Performance Optimizations
- **Depth Limiting**: Configurable directory traversal depth (default: 3 levels)
- **Pattern Caching**: Regex patterns cached for repeated use
- **Lazy Loading**: Files parsed only when needed
- **Error Resilience**: Continues processing even if individual files fail
- **Efficient Filtering**: Multiple exclusion strategies to minimize processing overhead
- **Memory Management**: Streams used for large file processing

## 🧪 Development

### Development Setup
```bash
# Clone repository
git clone <repository-url>
cd smart-renamer

# Install dependencies
bun install

# Start development with hot reload
bun run dev

# Run tests
bun run test

# Build for production
bun run build
```

### Available Scripts
```json
{
  "scripts": {
    "dev": "tsc --watch",           # Development with hot reload
    "build": "tsc",                 # Compile TypeScript to dist/
    "start": "node dist/cli.js",    # Run compiled version
    "lint": "eslint src/**/*.ts",   # Code linting
    "typecheck": "tsc --noEmit",    # Type checking only
    "clean": "rm -rf dist/",        # Clean build directory
    "check": "bun run build && node dist/cli.js analyze", # Quick verification
    "test": "jest",                 # Run test suite
    "test:watch": "jest --watch"    # Tests with hot reload
  }
}
```

### TypeScript Configuration
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "CommonJS", 
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "sourceMap": true,
    "outDir": "./dist"
  }
}
```

## 🤝 Contributing

### Areas for Enhancement
1. **Additional Language Support**: Python, Java, C#, Go, Rust naming conventions
2. **IDE Integrations**: VS Code extension, WebStorm plugin
3. **Git Hooks Integration**: Pre-commit hooks for naming validation
4. **Team Workflows**: Shared configuration management, team reporting
5. **Performance Improvements**: Parallel processing, incremental analysis
6. **Custom Rules**: User-defined naming patterns and validators

### Development Guidelines
- **Code Style**: Follow TypeScript strict mode conventions
- **Testing**: Comprehensive test coverage for all features
- **Documentation**: Update documentation for any changes
- **Commit Messages**: Use conventional commit format (use commit-suggester!)
- **Performance**: Consider impact on large codebases
- **Error Handling**: Provide helpful error messages and recovery options

### Architecture Principles
- **Modularity**: Each core component handles specific responsibilities
- **Extensibility**: Easy to add new conventions and languages
- **Performance**: Efficient processing of large codebases
- **User Experience**: Clear feedback and intuitive workflows
- **Configuration**: Flexible, team-shareable settings

## 📊 Package Information

- **Name**: smart-renamer
- **Current Version**: 1.2.0
- **License**: MIT
- **Author**: Mohammed Rishin Poolat
- **Node Requirement**: >=18.0.0
- **Repository**: [GitHub Repository](https://github.com/rishinpoolat/renamer)
- **NPM Package**: Published on npm registry

## 🎯 Use Cases & Benefits

### Perfect For:
- **Large JavaScript/TypeScript Projects**: Maintaining consistency across thousands of files
- **Team Development**: Enforcing naming standards across multiple developers
- **Legacy Code Modernization**: Upgrading old codebases to modern naming conventions
- **Open Source Projects**: Maintaining professional standards for public repositories
- **Enterprise Applications**: Meeting corporate coding standards and guidelines
- **Code Reviews**: Automated checking before merge requests

### Key Benefits:
- **Consistency**: Uniform naming patterns across entire codebase
- **Team Alignment**: Shared conventions reduce cognitive load and improve collaboration
- **Maintainability**: Clean, predictable naming makes code easier to navigate and understand
- **Quality Assurance**: Automated validation prevents naming violations
- **Developer Productivity**: Reduced time spent thinking about naming decisions
- **Professional Standards**: Maintains high-quality, industry-standard code organization

### Real-World Applications:
- **Migrating Projects**: Converting from one naming convention to another
- **Code Quality Audits**: Identifying and fixing naming inconsistencies
- **Onboarding New Developers**: Enforcing team conventions automatically
- **Continuous Integration**: Validating naming conventions in CI/CD pipelines
- **Refactoring Support**: Systematic renaming during large refactoring efforts

This tool represents a comprehensive solution for naming convention management, combining intelligent automation with user-friendly workflows to maintain professional code quality standards across projects of any size.
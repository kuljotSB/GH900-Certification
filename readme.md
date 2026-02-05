# GH-900 - GitHub Fundamentals Course

![course_thumbnail](./Assets/course_thumbnail.png)

## 📖 About This Course

Welcome to the **GH-900 - GitHub Fundamentals Certification Course**! This comprehensive repository contains hands-on labs, instructions, and resources designed to help you master the fundamentals of GitHub and prepare for the GitHub Fundamentals certification.

Whether you're new to version control or looking to formalize your GitHub knowledge, this course will guide you through essential GitHub features, best practices, and workflows used by millions of developers worldwide.

## 📑 Table of Contents

- [About This Course](#-about-this-course)
- [Prerequisites](#-prerequisites)
- [Repository Structure](#-repository-structure)
- [Available Labs](#-available-labs)
- [Learning Resources](#-learning-resources)
- [Getting Started](#-getting-started)
- [Course Topics](#-course-topics)
- [Contributing](#-contributing)

## ✅ Prerequisites

Before starting this course, you should have:

- A [GitHub account](https://github.com/signup)
- Basic understanding of command-line interface (CLI)
- Git installed on your local machine ([Download Git](https://git-scm.com/downloads))
- A text editor or IDE (VS Code, Sublime Text, etc.)
- Web browser for accessing GitHub's web interface

## 📁 Repository Structure

```
GH900-Certification/
├── Assets/              # Course assets and images
├── Instructions/        # Detailed instruction guides for various GitHub features
├── Labs/                # Hands-on lab exercises
│   ├── CodeQL-Demo-App/
│   ├── GitHub-Actions/
│   ├── Projects/
│   └── lab-git-basics/
└── readme.md           # This file
```

## 🧪 Available Labs

### 1. **Git Basics Lab** (`Labs/lab-git-basics/`)
Learn the fundamentals of Git and GitHub workflows including:
- Cloning repositories
- Making commits
- Creating pull requests
- Working with branches
- Issue templates and discussions

**Key Files:**
- `contributors.txt` - Practice adding your name
- `Issue_Templates/` - Sample issue templates
- `sample-issues-lab.md` - Issues practice exercises

### 2. **GitHub Actions Lab** (`Labs/GitHub-Actions/`)
Get hands-on experience with CI/CD automation:
- Workflow creation
- Automated testing
- Deployment pipelines

**Key Files:**
- `welcome.yml` - Sample GitHub Actions workflow

### 3. **GitHub Projects Lab** (`Labs/Projects/`)
Master project management on GitHub:
- Creating and managing projects
- Task tracking with issues
- Using project boards

**Key Files:**
- `checklist_issue.md` - Project checklist template

### 4. **CodeQL Security Lab** (`Labs/CodeQL-Demo-App/`)
Learn code security scanning with CodeQL:
- Setting up CodeQL
- Scanning for vulnerabilities
- Understanding security alerts

**Key Files:**
- `app.py` - Intentionally vulnerable Python application
- `requirements.txt` - Dependencies with known CVEs
- `codeql-cli-setup.ps1` - Setup script

> ⚠️ **Warning:** The CodeQL demo app contains intentional vulnerabilities for learning purposes. Do not use in production!

## 📚 Learning Resources

Detailed instruction guides are available in the `Instructions/` directory:

| Resource | Description |
|----------|-------------|
| `lab-git-basics.md` | Step-by-step guide for Git basics lab |
| `issues.md` | Working with GitHub Issues |
| `gists.md` | Creating and managing GitHub Gists |
| `wiki.md` | Setting up and using GitHub Wikis |
| `tagging.md` | Git tagging and releases |
| `codeowners.md` | Configuring code owners for reviews |
| `codeql_cli.md` | CodeQL CLI setup and usage |
| `codeql_custom.md` | Custom CodeQL configurations |
| `personal_projects.md` | Managing personal projects on GitHub |
| `devcontainer.json` | Development container configuration |

## 🚀 Getting Started

### Step 1: Clone This Repository

```bash
git clone https://github.com/kuljotSB/GH900-Certification.git
cd GH900-Certification
```

### Step 2: Choose Your First Lab

We recommend starting with the **Git Basics Lab**:

1. Navigate to `Instructions/lab-git-basics.md`
2. Follow the step-by-step instructions
3. Complete the exercises in `Labs/lab-git-basics/`

### Step 3: Progress Through the Course

Follow this recommended learning path:

1. ✅ **Git Basics** - Master clone, commit, and pull requests
2. ✅ **Issues & Gists** - Learn collaboration tools
3. ✅ **GitHub Actions** - Understand CI/CD automation
4. ✅ **Projects** - Manage work with project boards
5. ✅ **CodeQL** - Secure your code with scanning
6. ✅ **Advanced Features** - Wikis, code owners, and more

## 🎯 Course Topics

This certification course covers:

- **Version Control Basics**
  - Git fundamentals
  - Repository management
  - Branching and merging

- **Collaboration**
  - Pull requests
  - Code reviews
  - Issues and discussions

- **Automation**
  - GitHub Actions workflows
  - CI/CD pipelines
  - Automated testing

- **Security**
  - CodeQL scanning
  - Dependency management
  - Security best practices

- **Project Management**
  - GitHub Projects
  - Issue tracking
  - Milestones and labels

- **Documentation**
  - README files
  - GitHub Wikis
  - GitHub Pages

## 🤝 Contributing

This is a learning repository. If you're taking this course:

1. Fork this repository
2. Complete the labs in your fork
3. Follow the instructions in each lab
4. Create pull requests as instructed

If you find issues or have suggestions for improvement:

1. Open an issue describing the problem or enhancement
2. Reference the specific lab or instruction file
3. Provide clear steps to reproduce (if applicable)

## 📝 License

This course material is provided for educational purposes. Please refer to the repository owner for licensing information.

## 🙏 Acknowledgments

This course is maintained by [@kuljotSB](https://github.com/kuljotSB) and designed to help developers prepare for the GitHub Fundamentals (GH-900) certification.

---

**Ready to get started?** Begin with the [Git Basics Lab](./Instructions/lab-git-basics.md)!

**Questions?** Open an issue or reach out to the course maintainer.

Happy Learning! 🎓
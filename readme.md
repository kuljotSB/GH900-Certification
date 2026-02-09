# GH-900 - GitHub Fundamentals Course - Kuljot Singh Bakshi - GitHub Repository - modifications from dev branch version 2

![course_thumbnail](./Assets/course_thumbnail_image.png)

## 🚀 Getting Started

### Prerequisites

Before starting the labs, ensure you have:
- A **GitHub account** ([sign up here](https://github.com/signup))
- **Git** installed ([download here](https://git-scm.com/downloads))
- VSCode installed ([download here](https://code.visualstudio.com/download))
- Basic command-line knowledge

## 📚 About This Repository

This repository contains comprehensive lab materials, instructions, and resources for the **GitHub Fundamentals (GH-900) Certification** course. It is designed to help learners understand and master core GitHub concepts, from basic Git workflows to advanced features like CodeQL, GitHub Actions, Copilot, and GitHub Projects.

---

## 🎯 Course Overview

The GH-900 certification covers essential GitHub skills for developers, DevOps engineers, and security professionals. This repository provides hands-on labs and practical exercises to reinforce key concepts.

### What You'll Learn:
- **Git Fundamentals**: Cloning, committing, branching, and pull requests
- **Collaboration Workflows**: Issues, milestones, project management, and code reviews
- **Code Security**: CodeQL scanning, vulnerability detection, and CODEOWNERS
- **Automation**: GitHub Actions for CI/CD pipelines
- **AI-Powered Development**: GitHub Copilot features and agent capabilities
- **Documentation**: Wikis, README best practices, and project documentation

---

## 📂 Repository Structure

```
GH900-Certification/
├── Assets/                    # Course images and visual resources
├── Instructions/              # Step-by-step lab instructions and guides
│   ├── codeowners.md         # CODEOWNERS file configuration
│   ├── codeql_cli.md         # CodeQL CLI setup and usage
│   ├── codeql_custom.md      # Custom CodeQL configurations
│   ├── copilot_agents_in_github.md  # GitHub Copilot agent workflows
│   ├── github_copilot.md     # Copilot features and commands
│   ├── issues.md             # Issue and milestone templates
│   ├── lab-git-basics.md     # Git basics lab walkthrough
│   ├── personal_projects.md  # GitHub Projects management
│   ├── tagging.md            # Git tagging and releases
│   └── wiki.md               # GitHub Wiki setup
├── Labs/                      # Hands-on lab exercises
│   ├── CodeQL-Demo-App/      # Vulnerable Python app for CodeQL demos
│   ├── GitHub-Actions/       # GitHub Actions workflow examples
│   ├── Projects/             # GitHub Projects lab materials
│   └── lab-git-basics/       # Git basics practice repository
└── readme.md                  # This file
```

---

### Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/kuljotSB/GH900-Certification.git
   cd GH900-Certification
   ```

2. **Explore the Instructions folder** to find step-by-step guides for each topic.

3. **Complete the labs** in the `Labs/` directory to practice hands-on skills.

4. **Refer to the documentation** in `Instructions/` for detailed explanations and best practices.

---

## 📖 Lab Modules

### 1. Git Basics
**Location**: `Instructions/lab-git-basics.md` | `Labs/lab-git-basics/`

Learn fundamental Git commands and workflows:
- Clone a repository
- Create branches and commits
- Submit your first pull request
- Understand Git staging and history

---

### 2. GitHub Issues & Milestones
**Location**: `Instructions/issues.md`

Master project tracking with:
- Creating and managing issues
- Setting up milestones for project goals
- Using templates for consistency
- Organizing work with labels and assignees

---

### 3. GitHub Wikis
**Location**: `Instructions/wiki.md`

Build effective project documentation:
- Enable and configure Wikis
- Create structured documentation pages
- Write in Markdown
- Organize long-form guides and FAQs

---

### 4. Code Ownership (CODEOWNERS)
**Location**: `Instructions/codeowners.md`

Implement code review governance:
- Define code ownership rules
- Automate reviewer assignment
- Protect critical code paths
- Use pattern matching for ownership

---

### 5. CodeQL Security Scanning
**Location**: `Instructions/codeql_cli.md` | `Labs/CodeQL-Demo-App/`

Detect vulnerabilities in your code:
- Set up CodeQL CLI
- Create and analyze CodeQL databases
- Run security queries
- Customize CodeQL workflows
- Practice with intentionally vulnerable Python app

---

### 6. GitHub Actions
**Location**: `Labs/GitHub-Actions/`

Automate workflows with CI/CD:
- Create workflow files
- Trigger jobs on events
- Use actions from the marketplace
- Build, test, and deploy code automatically

---

### 7. GitHub Copilot
**Location**: `Instructions/github_copilot.md` | `Instructions/copilot_agents_in_github.md`

Leverage AI-powered coding assistance:
- Use inline code suggestions
- Explain and document code with `/explain` and `/docs`
- Generate tests with `/tests`
- Create issues and improve documentation with Copilot agents

---

### 8. GitHub Projects
**Location**: `Instructions/personal_projects.md` | `Labs/Projects/`

Manage work with project boards:
- Create project boards with custom fields
- Track issues and PRs visually
- Use iterations and roadmap views
- Automate project workflows

---

### 9. Git Tagging & Releases
**Location**: `Instructions/tagging.md`

Version your software:
- Create semantic version tags
- Push tags to remote repositories
- Generate releases with changelogs

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Git** | Version control system |
| **GitHub** | Collaboration and hosting platform |
| **CodeQL** | Security vulnerability scanning |
| **GitHub Actions** | CI/CD automation |
| **GitHub Copilot** | AI-powered code assistance |
| **Markdown** | Documentation formatting |
| **Python** | Example application language (CodeQL lab) |

---

## 🤝 Contributing

We welcome contributions to improve this course material!

### How to Contribute:
1. Fork this repository
2. Create a feature branch (`git checkout -b feature/improve-docs`)
3. Make your changes
4. Commit with clear messages (`git commit -m "docs: improve CodeQL instructions"`)
5. Push to your fork (`git push origin feature/improve-docs`)
6. Open a pull request

### Contribution Guidelines:
- Follow existing documentation structure
- Use clear, concise language
- Test all code examples before submitting
- Add screenshots or diagrams where helpful
- Update the README if adding new content

See `contributors.txt` for a list of contributors.

---

## 📝 License

This repository is provided for educational purposes as part of the GH-900 GitHub Fundamentals certification preparation.

---

## 🔗 Additional Resources

- [GitHub Documentation](https://docs.github.com/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Skills](https://skills.github.com/)
- [CodeQL Documentation](https://codeql.github.com/docs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

---

## 📧 Support

If you have questions or need help with the course material:
- Open an [issue](https://github.com/kuljotSB/GH900-Certification/issues) in this repository
- Review existing issues for common problems
- Refer to the official [GitHub Support](https://support.github.com/)

---

## ⚠️ Important Notes

- The **CodeQL-Demo-App** in `Labs/CodeQL-Demo-App/` contains **intentionally vulnerable code** for learning purposes. **Do not use in production.**
- Always follow security best practices when working with real projects
- Some labs may require additional permissions or GitHub features (e.g., GitHub Actions, CodeQL)

---

## 🎓 Certification Information

This repository supports preparation for the **GitHub Fundamentals (GH-900)** certification. For official certification details, visit [GitHub Certifications](https://examregistration.github.com/).

---

## 🌟 Acknowledgments

Special thanks to all contributors who have helped improve this course material and make GitHub fundamentals accessible to learners worldwide.

---

**Happy Learning! 🚀**
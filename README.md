<br />
<p align="center">
  <a href="https://github.com/rmenai/python-structure">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Python Structure</h3>

  <p align="center">
    The most complete python projects structure
    <br />
    <a href="https://github.com/rmenai/python-structure"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rmenai/python-structure">View Demo</a>
    ·
    <a href="https://github.com/rmenai/python-structure/issues/new?assignees=&labels=&template=bug_report.md&title=">Report Bug</a>
    ·
    <a href="https://github.com/rmenai/python-structure/issues/new?assignees=&labels=&template=feature_request.md&title=">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This is my main projects structure. It is pretty much complete, containing all the tools you need for a professional
project.

Project features:

* [Poetry](https://python-poetry.org/) for dependency management.
* [Docker](https://www.docker.com/) for container packaging.
* [.env](https://pypi.org/project/python-dotenv/) for environment variables.
* [Colorlog](https://pypi.org/project/colorlog/) for colorful logging.
* [Pytest](https://docs.pytest.org/en/6.2.x/) for writing powerful tests.

GitHub features:

* [pre-commit](https://pre-commit.com/) and [flake8](https://flake8.pycqa.org/en/latest/) for git hooks linting.
* [Lint & Test](https://github.com/rmenai/python-structure/blob/main/.github/workflows/lint-test.yaml)
  and [Build & Push](https://github.com/rmenai/python-structure/blob/main/.github/workflows/build-push.yaml) github
  workflows.

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

* [Poetry](https://python-poetry.org/docs/)
* [Docker](https://docs.docker.com/get-docker/) (optional)

### Installation

1. Clone the repo
   ```shell
   git clone https://github.com/rmenai/python-structure.git
   ```
2. Install the dependencies
   ```shell
   poetry install
   ```
3. Install the project git hooks
   ```shell
   poetry run task precommit
   ```

<!-- USAGE EXAMPLES -->

## Usage

Now you are done! You can start coding your project and run it using

```shell
poetry run task start
```

## Contributing

See [CONTRIBUTING.md](https://github.com/rmenai/python-structure/blob/main/CONTRIBUTING.md) for ways to get started.

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE](https://github.com/rmenai/python-structure/blob/main/LICENSE) for more
information.

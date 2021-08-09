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
    <a href="https://github.com/rmenai/python-structure/issues">Report Bug</a>
    ·
    <a href="https://github.com/rmenai/python-structure/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-structure">Project structure</a></li>
      </ul>
        <ul>
        <li><a href="#integrated-tools">Integrated tools</a></li>
      </ul>
        <ul>
        <li><a href="#special-features">Special features</a></li>
      </ul>
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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This is my main projects structure. It is pretty much complete, containing all the tools you need for a professional
project.

### Project structure

```

```

### Integrated tools

* [Poetry](https://python-poetry.org/) for dependency management.
* [Docker](https://www.docker.com/) for container packaging.
* [pre-commit](https://pre-commit.com/) and [flake8](https://flake8.pycqa.org/en/latest/) for git hooks and linting.

### Special features

* Easily manage your environment variables using [.env](https://pypi.org/project/python-dotenv/).
* [Colourful](https://pypi.org/project/colorlog/) console logging and rotating log files.
* Powerful unittests using [pytest](https://docs.pytest.org/en/6.2.x/) and the built
  in [unittest](https://docs.python.org/3/library/unittest.html).

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
4. Now change the files and options according to your project

<!-- USAGE EXAMPLES -->

## Usage

Now you are done! You can start your project and run it using

```shell
poetry run task start
```

## Contributing

See `CONTRIBUTING.md` for ways to get started.

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Menai Rami - [@menai_rami](https://twitter.com/menai_rami) - rami.menai@outlook.com

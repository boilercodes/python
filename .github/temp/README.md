<br />
<p align="center">
  <a href="{repo}">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">{title}</h3>

  <p align="center">
    {description}
    <br />
    <a href="{repo}"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="{repo}">View Demo</a>
    ·
    <a href="{repo}/issues/new?assignees=&labels=&template=bug_report.md&title=">Report Bug</a>
    ·
    <a href="{repo}/issues/new?assignees=&labels=&template=feature_request.md&title=">Request Feature</a>
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

The most complete python projects structure.


<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

* [Poetry](https://python-poetry.org/docs/)
* [Docker](https://docs.docker.com/get-docker/) (optional)

### Installation

1. Clone the repo
   ```shell
   git clone {repo}.git
   ```
2. Install the dependencies
   ```shell
   poetry install
   ```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

| Settings | Description                   | Required |
|----------|-------------------------------|----------|
| DEBUG    | Toggles debug mode in logging | No       |

<!-- USAGE EXAMPLES -->

## Usage

Now you are done! You can run the project using

```shell
poetry run task start
```

## Contributing

See [CONTRIBUTING.md]({repo}/blob/main/CONTRIBUTING.md) for ways to get started.

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE]({repo}/blob/main/LICENSE) for more
information.

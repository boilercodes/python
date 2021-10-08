# Contributing guidelines

Thank you for your interest in this project!

If you are interested in contributing, **this page contains the golden rules to follow when contributing**. Do note that
failing to comply with our guidelines may lead to a rejection of the contribution.

***

## The Golden Rules of Contributing

1. **Lint before you push**. We have simple but strict style rules that are enforced through linting. You must always
   lint your code before committing or pushing.

2. **Make great commits**. Great commits should be atomic, with a commit message explaining what and why.

3. **Do not open a pull request if you aren't assigned to the issue**. If someone is already working on it, consider
   offering to collaborate with that person.

4. **Use assets licensed for public use**. Whenever the assets are images, audio or even code, they must have a license
   compatible with our projects.

## Before commits

Install the project git hooks using [poetry]

```shell
poetry run task precommit
```

Now `pre-commit` will run automatically on `git commit`

```console
root@user:~$ git commit -m "some commit"
Check docstring is first.................................................Passed
Check for merge conflicts................................................Passed
Check Toml...............................................................Passed
Check Yaml...............................................................Passed
Detect Private Key.......................................................Passed
Fix End of Files.........................................................Passed
Tests should end in _test.py.............................................Passed
Trim Trailing Whitespace.................................................Passed
Flake8...................................................................Passed
```

Or you can run it manually

```shell
poetry run task lint
```

[flake8]: https://flake8.pycqa.org/en/latest/

[pre-commit]: https://pre-commit.com/

[poetry]: https://python-poetry.org/

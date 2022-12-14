# Contributing

BetterLib is open source, and contributions are welcome. If you want to contribute, please read the following guidelines.

## Code Style

BetterLib has a strict code style. It is based on [PEP 8](https://www.python.org/dev/peps/pep-0008/), but with a few extra rules:

- Indentation is always tabs. No spaces. No exceptions. Ever.
- Docstrings are always triple double quotes, not triple single quotes, and are always multi-line.
- Speaking of docstrings, always add them to every function and class made.
- Docstrings should consist of the following: The first line being a short description of the function/class, followed by a blank line, followed by a list of parameters (if any).
- There should be a blank line between every function, and two blank lines between every class.
- There should be a blank line between every import and the code that follows it.
- Also, on the topic of imports, make sure to condense them into one line if possible (if the imports become insanely long, exceptions can be made).
- Whenever adding functions or classes, also make sure to add them to the respective documentation file in the `docs` folder.
- When adding new modules, make sure to add them to the `__init__.py` file in the `betterlib` folder and the `docs/modules.md` file.
- Use markdownlint. If your markdown isn't compliant with the rules (except `no-duplicate-header`), I will not accept your PR until you fix it.

## Pull Requests

When making a pull request, please make sure to follow these guidelines:

- Make sure your code follows the code style guidelines.
- Make sure your changes are documented in the `docs` folder and in the pull request description.
- Make sure your pull request is up to date with the latest version of the `master` branch.
- When dealing with merge conflicts, make sure to resolve them in favor of the `master` branch (unless you are confident that your changes are correct).

## Issues

If you find a bug or a missing key feature, please report it on the [issues page](https://github.com/HENRYMARTIN5/betterlib) on GitHub. Please make sure to follow these guidelines:

- Make sure your issue is not a duplicate of another issue.
- Ensure that your issue is related to BetterLib, and not your own code.
- Always include a code snippet that reproduces the issue, if applicable.

## License

BetterLib is licensed under the Unlicense. This means that you can use it in any project, commercial or otherwise, without any restrictions whatsoever.

## Credits

BetterLib was created and maintained by [Henry Martin](http://henrymartin.co/).

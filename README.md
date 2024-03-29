<p align="center">
    <img src="https://raw.githubusercontent.com/matheusfelipeog/vermon/master/.github/assets/images/vermon.png" alt="Logo Vermon" width="450px" />
</p>

<p align="center">
    <a href="https://pypi.org/project/vermon/">
        <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/vermon" />
    </a>
    <a href="https://pypi.org/project/vermon/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/vermon" />
    </a>
    <a href="https://github.com/matheusfelipeog/vermon/releases">
        <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/matheusfelipeog/vermon" />
    </a>
    <a href="https://github.com/matheusfelipeog/vermon/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/matheusfelipeog/vermon" alt="License MIT" />
    </a>
</p>


## Index

- [About](#about)
- [Install](#install)
    - [with pipenv](#install-with-pipenv)
    - [with pip and virtualenv](#install-with-pip-and-virtualenv)
- [Use](#use)
- [Contributions](#contributions)
- [License](#license)


## About

**Vermon** monitors the version of the package specified on the [`pypi`](https://pypi.org/) platform, compares the version of the package installed in your environment with the latest published version and, if less, shows a warning with instructions for updating in the terminal.

***For example:*** *suppose you created a package called `foo` and published version `1.0.0` in pypi. Some users are already using the foo package as a dependency on their projects. You found a bug and released a patch with the fix, now the latest version of `foo` is `1.0.1`. All users using version `1.0.0` (less than the last release) of the package will receive a warning on the terminal similar to this one whenever they run the project:*

```bash
> python your_project.py
You are using an old version of the foo package (v1.0.0)
a new version has been released (v1.0.1).
Please run: python -m pip install foo --upgrade
```

Now users know they have a dependency that needs to be updated ;)


## Install

Use [`pipenv`](https://pipenv.pypa.io/en/latest/) to install fordev in your environment. It will create a virtual environment and separate all dependencies and subdependencies from your global environment.

### Install with pipenv

Create a directory and enter it:

```bash
$ mkdir my_project && cd my_project
```

Install with pipenv using:

```bash
$ pipenv install vermon
```

Now activate the virtual environment:

```bash
$ pipenv shell
```

### Install with pip and virtualenv

Alternatively, if you don't want to use pipenv, use `pip` + `virtualenv` to do the same thing.

Create a directory and enter it:

```bash
$ mkdir my_project && cd my_project
```

Create and activate the virtual environment:

```bash
$ virtualenv venv && source venv/Scripts/activate
```
> Note: In linux environment, use `source venv/bin/activate` to activate the virtual environment.

Now install with pip:

```bash
$ pip install vermon
```

Done, now you can start the job ;)


## Use

To use the vermon package, call `Vermon.run` method in your package's `__init__.py` file:

```python
from vermon import Vermon

Vermon.run(
    package='YOUR_PACKAGE',
    current_version=your_package.__version__
)
```

Done 🎉


## Contributions

All contributions are welcome!

Found a problem, want to give a tip? [open an issue](https://github.com/matheusfelipeog/vermon/issues)

Do you have a solution to the problem? [Send me a PR](https://github.com/matheusfelipeog/vermon/pulls)

Did you like this project? [Click on the star ⭐](https://github.com/matheusfelipeog/vermon/stargazers)


## License

This project is using the MIT license, see in [MIT LICENSE](https://github.com/matheusfelipeog/vermon/blob/master/LICENSE).

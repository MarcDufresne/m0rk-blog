Title: Intro to Poetry
Subtitle: Python Packaging and Dependency Management Made Easy
Date: 2018-09-14 22:00
Category: Python
Tags: python, poetry, packaging, dependency management
Cover: https://github.com/MarcDufresne/m0rk-blog/raw/master/m0rk-theme/static/img/banners/intro-to-poetry.png


[Poetry](https://poetry.eustace.io) is a Python packaging and dependency management tool that works really well
and will bring you into the future of Python project management. The goal of this article is to show you what
Poetry can do, and how to do it.

To install Poetry you can simply use `pip install -U poetry`, this will install the latest version on your system.
You might have to do a `--user` install if you're using the Python distribution that is pre-installed on your machine.

To demonstrate Poetry we will be going through some integration steps in a Python project. For the sake of simplicity
the project we start with contains only one Python file in a top-level package, here's is the structure of the
project and the contents of our Python file:

```
.
└── example_app
    ├── app.py
    └── __init__.py
```

**app.py**
```python
import time

import click


def demo():
    with click.progressbar(range(7)) as entries:
        for _ in entries:
            time.sleep(1)


if __name__ == '__main__':
    demo()

```

Now that we have our project and Poetry is installed, let's get to it. First, you need to create the project's
`pyproject.toml` file at the root of your project. This file contains metadata about your project and all
dependencies it might have. To create this file simply run `poetry init` from the root of the project and follow the
prompts, values between square brackets are defaults.

Once you are done with the prompts you will notice the new `pyproject.toml` file at the root of your project. You
are now ready to add any dependencies your project might need. In our case we use the library
[`click`](http://click.pocoo.org/5/). You can add it with `poetry add`, like so:

```bash
$ poetry add click

Using version ^6.7 for click

Updating dependencies
Resolving dependencies... (0.3s)


Package operations: 1 install, 0 updates, 0 removals

Writing lock file

  - Installing click (6.7)
```

`click` will be added to the `pyproject.toml` and Poetry will update the `pyproject.lock` file.

Note that adding a package will create your project's virtual environment but if at any time you want to install
your venv manually you can do so with `poetry install` which will install your dependencies into the
project's venv. `install` will not however install your own project in the environment, to do this you need to use
`poetry develop`, which does all of what `install` does but also symlinks your project in the venv.

Poetry also supports defining "dev" dependencies, those are libraries that will need to develop and test, but that
are not required to run your app. You can add those dependencies with `poetry add --dev <library>`. Usually, you
will find `flake8`, `pytest` and other tools in this section.

So, now that we have our code and Poetry-managed virtual environment ready we can run it. Poetry provides two useful
commands for this scenario, they are `poetry run` and `poetry shell`.

- `run` will run a given command from inside the Poetry venv. So if we wanted to run our app we could do
`poetry run python example_app/app.py`.
- `shell` mimics the behaviour of activating a venv. This allows you to run commands from inside the venv without using
`poetry run` all the time.

And finally, one great reason to be using Poetry is that it can build and publish your library or app if you need
it to.
Simply use `poetry build` and `poetry publish`, or `poetry publish --build` to do both at the same time! You will be
prompted to enter your PyPI credentials when publishing, and once you do that your package will upload to PyPI.

Publishing is completely configurable so you don't have to enter your username and password all the time. And it can
even publish to other repos, even private ones.

**Bonus**: Poetry can show you the outdated dependencies in your project if you do `poetry show --outdated` or a
dependency graph if you do `poetry show --tree`.

For more information consult the official [Poetry documentation](https://poetry.eustace.io/docs/).

You can find the full example of the above files on the
[blog's examples repo](https://github.com/MarcDufresne/m0rk-blog-examples/tree/master/intro-to-poetry).

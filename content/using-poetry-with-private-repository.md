Title: Using Poetry with a Private Repository
Subtitle: How to Install and Publish Packages
Date: 2018-09-24 22:00
Category: Python
Tags: python, poetry, packaging, private repositories
Cover: https://github.com/MarcDufresne/m0rk-blog/raw/master/m0rk-theme/static/img/banners/using-poetry-with-private-repository.png


In a [previous article]({filename}/intro-to-poetry.md) we went through the basic configuration and usage
steps for [Poetry](https://poetry.eustace.io). One thing that is often needed in professional setting is
access to password-protected private package indexes, luckily Poetry can do that, lets see how we can go about it.

We will be reusing the Poetry example from the
[blog's examples repo](https://github.com/MarcDufresne/m0rk-blog-examples/tree/master/intro-to-poetry)
as a base for this article. Any required changes wil be detailed.

#### Downloading and installing packages

Poetry uses configuration files to store custom indexes' credentials, so most of our work will be done using
`poetry config` and some changes to our `pyproject.toml` file.

First, let's add a reference to our repository in the `pyproject.toml` file (above the
`tool.poetry.dependencies` section), add the section below to your file and make sure to replace the
values to fit your setup.

```toml
[[tool.poetry.source]]
name = "my-custom-repo"  # This name will be used in the configuration to retreive the proper credentials
url = "https://my.customrepo.com/simple/"  # URL used to download your packages from
```

Then, configure the credentials for your repo. Note that this only needs to be done once per
repo, not per project.

```bash
$ poetry config http-basic.my-custom-repo user1 secretp4ssword!
```

Once those two steps are done, you can use `poetry add` to install a package from your newly configured custom index.
So,

```bash
$ poetry add my_package
```

Poetry should find and install your package and update your `pyproject.toml` file with this new dependency.
You can add as many package indexes as you need without issue.

#### Publishing your own package

Now, chances are that if you have an internal package index you most likely will need a way to publish those packages.
Since Poetry does away with the `setup.py` file you need a new way to build and publish your custom packages, enter
`poetry build` and `poetry publish`.

The `build` command speaks for itself, when invoked it will build a source and a wheel release of your project in
the `dist` directory.

To use the `publish` command you will first need to configure your credentials (same as above, with `http-basic`) and
the repo's URL, where to upload your new files. You can do so with the command below:

```bash
$ poetry config repositories.my-custom-repo https://my.customrepo.com/simple/
```

Once those two configuration values are set you can invoke the `publish` command:

```bash
$ poetry publish -r my-custom-repo
```

This will take whatever is in the `dist` directory and upload it to your custom index (specified using `-r`).
You can skip the `build` command by adding the `--build` option to your `publish` command. This will build and publish
at the same time.

**PRO TIP**: You can also use the `poetry version` command to automatically change your project's version number!

That's it! You are done with installing and publishing private packages, for more information
consult the official [Poetry documentation](https://poetry.eustace.io/docs/).

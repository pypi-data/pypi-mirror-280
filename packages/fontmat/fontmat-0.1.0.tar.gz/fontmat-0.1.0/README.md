# fontmat

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A CLI to check font metadata.

- [Source code](https://gitlab.com/joaommpalmeiro/fontmat)
- [PyPI package](https://pypi.org/project/fontmat/)

## Usage

### Via [pipx](https://github.com/pypa/pipx)

```bash
pipx run fontmat --help
```

```bash
pipx run fontmat
```

## Development

Install [pyenv](https://github.com/pyenv/pyenv) (if necessary).

```bash
pyenv install && pyenv versions
```

```bash
pip install hatch==1.9.3 && hatch --version
```

```bash
hatch config set dirs.env.virtual .hatch
```

```bash
hatch config show
```

```bash
hatch env create
```

```bash
hatch status
```

```bash
hatch env show
```

```bash
hatch dep show table
```

```bash
hatch run pip list
```

```bash
hatch run fontmat --help
```

```bash
hatch run fontmat
```

```bash
hatch run lint
```

```bash
hatch run format
```

## Deployment

```bash
hatch version micro
```

```bash
hatch version minor
```

```bash
hatch version major
```

```bash
hatch build --clean
```

```bash
echo "v$(hatch version)" | pbcopy
```

- Commit and push changes.
- Create a tag on [GitHub Desktop](https://github.blog/2020-05-12-create-and-push-tags-in-the-latest-github-desktop-2-5-release/).
- Check [GitLab](https://gitlab.com/joaommpalmeiro/fontmat/-/tags).

```bash
hatch publish
```

- Check [PyPI](https://pypi.org/project/fontmat/).

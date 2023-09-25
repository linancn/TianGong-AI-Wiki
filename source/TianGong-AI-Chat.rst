TianGong-AI-Chat
================

Env Preparing
-------------

VSCode Dev Contariners
~~~~~~~~~~~~~~~~~~~~~~

1. Install VSCode

2. Install Docker

3. Install VSCode Extension: Remote - Containers

Python 3 -> Additional Options -> 3.11-bullseye -> ZSH Plugins (Last One) -> Trust @devcontainers-contrib -> Keep Defaults

Setup venv:
~~~~~~~~~~~

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements:
~~~~~~~~~~~~~~~~~~~~~

```bash
pip install --upgrade pip
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt --upgrade
```


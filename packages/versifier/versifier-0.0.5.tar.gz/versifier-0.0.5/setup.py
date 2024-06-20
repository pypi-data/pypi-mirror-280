# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['versifier']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0.3',
 'pip-requirements-parser>=32.0.1,<33.0.0',
 'tomli>=1.2.3,<2.0.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses==0.8']}

entry_points = \
{'console_scripts': ['versifier = versifier.__main__:cli']}

setup_kwargs = {
    'name': 'versifier',
    'version': '0.0.5',
    'description': 'Versifier: A lyrical tool to transform Python requirements into Poetry configurations, effortlessly and elegantly.',
    'long_description': '# versifier\n\n[![Release](https://img.shields.io/github/v/release/mrlyc/versifier)](https://img.shields.io/github/v/release/mrlyc/versifier)\n[![Build status](https://img.shields.io/github/actions/workflow/status/mrlyc/versifier/main.yml?branch=main)](https://github.com/mrlyc/versifier/actions/workflows/main.yml?query=branch%3Amain)\n[![codecov](https://codecov.io/gh/mrlyc/versifier/branch/main/graph/badge.svg)](https://codecov.io/gh/mrlyc/versifier)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/mrlyc/versifier)](https://img.shields.io/github/commit-activity/m/mrlyc/versifier)\n[![License](https://img.shields.io/github/license/mrlyc/versifier)](https://img.shields.io/github/license/mrlyc/versifier)\n\n## Overview\n\n这个项目提供了一套命令行工具集，主要用于处理 Python 项目的依赖管理。主要功能包括：\n- 将 requirements.txt 转化为 Poetry 的 pyproject.toml\n- 将 Poetry 的 pyproject.toml 导出为 requirements.txt\n- 将私有包提取到指定目录\n\n## Installation\n\n使用 pip 来安装这个项目：\n\n```shell\npip install versifier\n```\n\n## Commands\n### requirements_to_poetry\n\n此命令将requirements.txt文件转换为Poetry格式。\n\n```bash\nversifier requirements_to_poetry --poetry-path <path_to_poetry> -r <requirements_files> -d <dev_requirements_files> -e <exclude_packages>\n```\n\n- `--poetry-path`: 指明Poetry的路径。默认为 "poetry"。\n- `-r, --requirements`: 一个或多个requirements文件。\n- `-d, --dev-requirements`: 一个或多个开发需求文件。\n- `-e, --exclude`: 需要排除的包。\n\n### poetry_to_requirements\n\n此命令将Poetry依赖项导出到requirements.txt格式。\n\n```bash\nversifier poetry_to_requirements -o <output_file> --poetry-path <path_to_poetry> --exclude-specifiers --include-comments -d -E <extra_requirements> -m <markers>\n```\n\n- `-o, --output`: 指明输出文件。如果未提供，则输出打印到控制台。\n- `--poetry-path`: 指明Poetry的路径。默认为 "poetry"。\n- `--exclude-specifiers`: 排除说明符。\n- `--include-comments`: 包括评论。\n- `-d, --include-dev-requirements`: 包括开发需求。\n- `-E, --extra-requirements`: 额外的需求。\n- `-m, --markers`: 过滤标记。\n- `-P, --private-packages`：私有包列表。\n\n### extract_private_packages\n\n此命令提取私有包。\n\n```bash\nversifier extract_private_packages --output <output_dir> --poetry-path <path_to_poetry> -E <extra_requirements> --exclude-file-patterns <exclude_files>\n```\n\n- `--output`: 指明输出目录。默认为当前目录。\n- `--poetry-path`: 指明Poetry的路径。默认为 "poetry"。\n- `-E, --extra-requirements`: 额外的需求。\n- `--exclude-file-patterns`: 需要排除的文件。\n- `-P, --private-packages`：私有包列表。\n\n### compile_private_packages\n\n此命令编译私有包。\n\n```bash\nversifier compile_private_packages --output <output_dir> --poetry-path <path_to_poetry> --nuitka-path <path_to_nuitka3> -E <extra_requirements>\n```\n\n- `--output`: 指明输出目录。默认为当前目录。\n- `--poetry-path`: 指明Poetry的路径。默认为 "poetry"。\n- `--nuitka-path`: 指明nuitka3的路径。默认为 "nuitka3"。\n- `-E, --extra-requirements`: 额外的需求。\n- `-P, --private-packages`：私有包列表。\n\n## License\n\n此项目使用 MIT 许可证。有关详细信息，请参阅 LICENSE 文件。\n\n## Contributing\n\n我们欢迎各种形式的贡献，包括报告问题、提出新功能、改进文档或提交代码更改。如果你想要贡献，请查看 CONTRIBUTING.md 获取更多信息。',
    'author': 'MrLYC',
    'author_email': 'fx@m.mrlyc.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mrlyc/versifier',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)

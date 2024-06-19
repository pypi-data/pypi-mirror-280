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
    'version': '0.0.3',
    'description': 'Versifier: A lyrical tool to transform Python requirements into Poetry configurations, effortlessly and elegantly.',
    'long_description': '# versifier\n\n[![Release](https://img.shields.io/github/v/release/mrlyc/versifier)](https://img.shields.io/github/v/release/mrlyc/versifier)\n[![Build status](https://img.shields.io/github/actions/workflow/status/mrlyc/versifier/main.yml?branch=main)](https://github.com/mrlyc/versifier/actions/workflows/main.yml?query=branch%3Amain)\n[![codecov](https://codecov.io/gh/mrlyc/versifier/branch/main/graph/badge.svg)](https://codecov.io/gh/mrlyc/versifier)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/mrlyc/versifier)](https://img.shields.io/github/commit-activity/m/mrlyc/versifier)\n[![License](https://img.shields.io/github/license/mrlyc/versifier)](https://img.shields.io/github/license/mrlyc/versifier)\n\n## Overview\n\n这个项目提供了一套命令行工具集，主要用于处理 Python 项目的依赖管理。主要功能包括：\n- 将 requirements.txt 转化为 Poetry 的 pyproject.toml\n- 将 Poetry 的 pyproject.toml 导出为 requirements.txt\n- 将私有包提取到指定目录\n\n## Installation\n\n使用 pip 来安装这个项目：\n\n```shell\npip install versifier\n```\n\n## Commands\n\n### requirements_to_poetry\n\n这个命令将 requirements.txt 转化为 Poetry 的 pyproject.toml。\n\n使用方法：\n\n```shell\nrequirements_to_poetry -r <requirements> -d <dev_requirements> -e <exclude>\n```\n\n参数说明：\n\n- `-r, --requirements`：指定一个或多个 requirements 文件。\n- `-d, --dev-requirements`：指定一个或多个 dev requirements 文件。\n- `-e, --exclude`：指定需要排除的包。\n\n### poetry_to_requirements\n\n这个命令将 Poetry 的 pyproject.toml 导出为 requirements.txt。\n\n使用方法：\n\n```shell\npoetry_to_requirements -o <output> --exclude-specifiers --include-comments -d -E <extra_requirements> -m <markers>\n```\n\n参数说明：\n\n- `-o, --output`：输出文件的路径。如果不指定，将直接打印到控制台。\n- `--exclude-specifiers`：如果指定，将排除版本规定。\n- `--include-comments`：如果指定，将包含注释。\n- `-d, --include-dev-requirements`：如果指定，将包含 dev requirements。\n- `-E, --extra-requirements`：指定额外的 requirements。\n- `-m, --markers`：指定 markers。\n\n### extract_private_packages\n\n这个命令用于提取私有包。\n\n使用方法：\n\n```shell\nextract_private_packages --output <output_dir> --poetry-path <poetry_path> -E <extra_requirements> --exclude-file-patterns <exclude_patterns>\n```\n\n参数说明：\n\n- `--output`：输出目录的路径。\n- `--poetry-path`：Poetry 的路径。\n- `-E, --extra-requirements`：指定额外的 requirements。\n- `--exclude-file-patterns`：指定需要排除的文件模式。\n\n## License\n\n此项目使用 MIT 许可证。有关详细信息，请参阅 LICENSE 文件。\n\n## Contributing\n\n我们欢迎各种形式的贡献，包括报告问题、提出新功能、改进文档或提交代码更改。如果你想要贡献，请查看 CONTRIBUTING.md 获取更多信息。',
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

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['src']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.111.0,<0.112.0',
 'langchain-community>=0.2.5,<0.3.0',
 'langchain-core>=0.2.9,<0.3.0']

setup_kwargs = {
    'name': 'kithub',
    'version': '0.1.1',
    'description': 'KitHub is a powerful framework for creating and managing tool-based APIs. It integrates seamlessly with LangChain tools and provides a simple interface for exposing these tools as API endpoints.',
    'long_description': '<h1 align="center"> 🛠️ KitHub 🛠️ </h1>\n\n<p align="center">\n  <img src="public/logo.png" alt="KitHub Logo" width="250"/>\n</p>\n\n<p align="center">\n  <!-- <a href="https://github.com/uriafranko/kithub/actions"><img src="https://github.com/uriafranko/kithub/workflows/tests/badge.svg" alt="Build Status"></a> -->\n  <a href="https://pypi.org/project/kithub/"><img src="https://img.shields.io/pypi/v/kithub.svg" alt="PyPI version"></a>\n  <a href="https://github.com/uriafranko/kithub/blob/main/LICENSE"><img src="https://img.shields.io/github/license/uriafranko/kithub.svg" alt="License"></a>\n</p>\n\nKitHub is a powerful framework for creating and managing tool-based APIs. It integrates seamlessly with LangChain tools and provides a simple interface for exposing these tools as API endpoints.\n\n## ✨ Features\n\n- 🔧 Easy integration with LangChain tools\n- 🚀 Rapid API development with FastAPI\n- 🔒 Built-in input validation and error handling\n- 📚 Automatic OpenAPI (Swagger) documentation\n- 🌐 CORS support out of the box\n- 🧰 Modular design with support for multiple tool kits\n\n## 🚀 Quick Start\n\n### Installation\n\n```bash\npip install kithub\n```\n\n### Basic Usage\n\n```python\nfrom kithub import create_kit, create_kithub\nfrom langchain_core.tools import tool\n\n@tool\ndef example_tool(x: int, y: int):\n    """Add two numbers together."""\n    return x + y\n\n# Create a kit with your tools\nkit = create_kit(tools=[example_tool], prefix="/v1")\n\n# Create the KitHub app\napp = create_kithub([kit])\n\n# Run the app\nif __name__ == "__main__":\n    import uvicorn\n    uvicorn.run(app, host="0.0.0.0", port=8000)\n```\n\n## 📖 Documentation\n\nFor full documentation, visit [kithub.readthedocs.io](https://kithub.readthedocs.io).\n\n## 🧪 Running Tests\n\n```bash\npytest tests/\n```\n\n## 🤝 Contributing\n\nContributions are welcome! Please feel free to submit a Pull Request.\n\n## 📄 License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.\n\n## 🙏 Acknowledgements\n\n- [FastAPI](https://fastapi.tiangolo.com/) for the awesome web framework\n- [LangChain](https://python.langchain.com/) for the powerful tool abstractions\n\n---\n\n<p align="center">\n  Made with ❤️ by <a href="https://github.com/uriafranko">Uria Franko</a>\n</p>\n',
    'author': 'Uria Franko',
    'author_email': 'uriafranko@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

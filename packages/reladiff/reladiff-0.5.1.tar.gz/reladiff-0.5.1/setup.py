# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reladiff', 'reladiff.databases']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1',
 'dsnparse',
 'rich',
 'runtype>=0.5.0',
 'sqeleton>=0.1.4',
 'toml>=0.10.2']

extras_require = \
{'all': ['mysql-connector-python>=8.0.29',
         'psycopg2',
         'snowflake-connector-python>=2.7.2',
         'cryptography',
         'trino>=0.314.0',
         'presto-python-client',
         'clickhouse-driver',
         'duckdb>=0.6.0'],
 'clickhouse': ['clickhouse-driver'],
 'duckdb': ['duckdb>=0.6.0'],
 'mysql': ['mysql-connector-python>=8.0.29'],
 'postgresql': ['psycopg2'],
 'presto': ['presto-python-client'],
 'snowflake': ['snowflake-connector-python>=2.7.2', 'cryptography'],
 'trino': ['trino>=0.314.0']}

entry_points = \
{'console_scripts': ['reladiff = reladiff.__main__:main']}

setup_kwargs = {
    'name': 'reladiff',
    'version': '0.5.1',
    'description': 'Command-line tool and Python library to efficiently diff rows across two different databases.',
    'long_description': '![image](reladiff_logo.svg)\n\n&nbsp;\n<br/>\n<br/>\n<span style="font-size:1.3em">**Reladiff**</span> is a high-performance tool and library designed for diffing large datasets across databases. By executing the diff calculation within the database itself, Reladiff minimizes data transfer and achieves optimal performance.\n\nThis tool is specifically tailored for data professionals, DevOps engineers, and system administrators.\n\nReladiff is free, open-source, user-friendly, extensively tested, and delivers fast results, even at massive scale.\n\n### Key Features:\n\n 1. **Cross-Database Diff**: Reladiff employs a divide-and-conquer algorithm, based on matching hashes, to efficiently identify modified segments and download only the necessary data for comparison. This approach ensures exceptional performance when differences are minimal.\n\n    - ⇄  Diffs across over a dozen different databases (e.g. *PostgreSQL* -> *Snowflake*) !\n\n    - 🧠 Gracefully handles reduced precision (e.g., timestamp(9) -> timestamp(3)) by rounding according to the database specification.\n\n    - 🔥 Benchmarked to diff over 25M rows in under 10 seconds and over 1B rows in approximately 5 minutes, given no differences.\n\n    - ♾️ Capable of handling tables with tens of billions of rows.\n\n\n2. **Intra-Database Diff**: When both tables reside in the same database, Reladiff compares them using a join operation, with additional optimizations for enhanced speed.\n\n    - Supports materializing the diff into a local table.\n    - Can collect various extra statistics about the tables.\n\n3. **Threaded**: Utilizes multiple threads to significantly boost performance during diffing operations.\n\n3. **Configurable**: Offers numerous options for power-users to customize and optimize their usage.\n\n4. **Automation-Friendly**: Outputs both JSON and git-like diffs (with + and -), facilitating easy integration into CI/CD pipelines.\n\n5. **Over a dozen databases supported**. MySQL, Postgres, Snowflake, Bigquery, Oracle, Clickhouse, and more. [See full list](https://reladiff.readthedocs.io/en/latest/supported-databases.html)\n\n\nReladiff is a fork of an archived project called [data-diff](https://github.com/datafold/data-diff).\n\n## Get Started\n\n[**🗎 Read the Documentation**](https://reladiff.readthedocs.io/en/latest/) - our detailed documentation has everything you need to start diffing.\n\n## Quickstart\n\nFor the impatient ;)\n\n### Install\n\nReladiff is available on [PyPI](https://pypi.org/project/reladiff/). You may install it by running:\n\n```\npip install reladiff\n```\n\nRequires Python 3.8+ with pip.\n\nWe advise to install it within a virtual-env.\n\n### How to Use\n\nOnce you\'ve installed Reladiff, you can run it from the command-line:\n\n```bash\n# Cross-DB diff, using hashes\nreladiff  DB1_URI  TABLE1_NAME  DB2_URI  TABLE2_NAME  [OPTIONS]\n```\n\nWhen both tables belong to the same database, a shorter syntax is available:\n\n```bash\n# Same-DB diff, using outer join\nreladiff  DB1_URI  TABLE1_NAME  TABLE2_NAME  [OPTIONS]\n```\n\nOr, you can import and run it from Python:\n\n```python\nfrom reladiff import connect_to_table, diff_tables\n\ntable1 = connect_to_table("postgresql:///", "table_name", "id")\ntable2 = connect_to_table("mysql:///", "table_name", "id")\n\nsign: Literal[\'+\' | \'-\']\nrow: tuple[str, ...]\nfor sign, row in diff_tables(table1, table2):\n    print(sign, row)\n```\n\nRead our detailed instructions:\n\n* [How to use from the shell / command-line](https://reladiff.readthedocs.io/en/latest/how-to-use.html#how-to-use-from-the-shell-or-command-line)\n    * [How to use with TOML configuration file](https://reladiff.readthedocs.io/en/latest/how-to-use.html#how-to-use-with-a-configuration-file)\n* [How to use from Python](https://reladiff.readthedocs.io/en/latest/how-to-use.html#how-to-use-from-python)\n\n\n#### "Real-world" example: Diff "events" table between Postgres and Snowflake\n\n```\nreladiff \\\n  postgresql:/// \\\n  events \\\n  "snowflake://<username>:<password>@<password>/<DATABASE>/<SCHEMA>?warehouse=<WAREHOUSE>&role=<ROLE>" \\\n  events \\\n  -k event_id \\         # Identifier of event\n  -c event_data \\       # Extra column to compare\n  -w "event_time < \'2024-10-10\'"    # Filter the rows on both dbs\n```\n\n#### "Real-world" example: Diff "events" and "old_events" tables in the same Postgres DB\n\nMaterializes the results into a new table, containing the current timestamp in its name.\n\n```\nreladiff \\\n  postgresql:///  events  old_events \\\n  -k org_id \\\n  -c created_at -c is_internal \\\n  -w "org_id != 1 and org_id < 2000" \\\n  -m test_results_%t \\\n  --materialize-all-rows \\\n  --table-write-limit 10000\n```\n\n#### More examples\n\n<p align="center">\n  <img alt="diff2" src="https://user-images.githubusercontent.com/1799931/196754998-a88c0a52-8751-443d-b052-26c03d99d9e5.png" />\n</p>\n\n<p align="center">\n  <a href=https://www.loom.com/share/682e4b7d74e84eb4824b983311f0a3b2 target="_blank">\n    <img alt="Intro to Diff" src="https://user-images.githubusercontent.com/1799931/196576582-d3535395-12ef-40fd-bbbb-e205ccae1159.png" width="50%" height="50%" />\n  </a>\n</p>\n\n\n### Technical Explanation\n\nCheck out this [technical explanation](https://reladiff.readthedocs.io/en/latest/technical-explanation.html) of how reladiff works.\n\n### We\'re here to help!\n\n* Confused? Got a cool idea? Just want to share your thoughts? Let\'s discuss it in [GitHub Discussions](https://github.com/erezsh/reladiff/discussions).\n\n* Did you encounter a bug? [Open an issue](https://github.com/erezsh/reladiff/issues).\n\n## How to Contribute\n* Please read the [contributing guidelines](https://github.com/erezsh/reladiff/blob/master/CONTRIBUTING.md) to get started.\n* Feel free to open a new issue or work on an existing one.\n\nBig thanks to everyone who contributed so far:\n\n<a href="https://github.com/erezsh/reladiff/graphs/contributors">\n  <img src="https://contributors-img.web.app/image?repo=erezsh/reladiff" />\n</a>\n\n\n## License\n\nThis project is licensed under the terms of the [MIT License](https://github.com/erezsh/reladiff/blob/master/LICENSE).\n',
    'author': 'Erez Shinan',
    'author_email': 'erezshin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/erezsh/reladiff',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

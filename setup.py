from setuptools import setup, find_packages

setup(
    name='TecnooseNotionExporter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'tecnoose_notion_exporter=tecnoose_notion_exporter.main:main',
        ],
    },
)
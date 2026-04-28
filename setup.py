from setuptools import setup, find_packages

setup(
    name="Super-Directional-md-qd-Bridge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mistletoe>=1.0.0",
        "python-frontmatter>=1.1.0",
        "PyYAML>=6.0",
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "md-qd-bridge=md_qd_bridge.cli:main",
        ],
    },
    author="valorisa",
    author_email="valorisa@github.com",
    description="Bidirectional converter between Markdown (.md) and Quarkdown (.qd)",
    url="https://github.com/valorisa/Super-Directional-md-qd-Bridge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

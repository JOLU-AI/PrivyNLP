from setuptools import setup, find_packages

setup(
    name="privynlp",
    version="0.2.0",
    description="LLM-agnostic Python library for detecting and redacting PII/PHI/payment data in text.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your@email.com",
    url="https://github.com/JOLU-AI/PrivyNLP",
    packages=find_packages(),
    install_requires=[
        "spacy>=3.0.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    include_package_data=True
)
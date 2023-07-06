from setuptools import setup, find_packages

setup(
    name="qsafecrypto",
    version="1.0.0",
    author="Md Fazlul Karim",
    author_email="enterprise@mindread.io",
    description="A secure and user-friendly open-source cryptography library, offering modern cryptographic APIs that are resistant to quantum attacks. Protect your data with ease and confidence using advanced quantum-resistant algorithms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mindreadio/qsafecrypto",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
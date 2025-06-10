from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import sys

# Read the contents of your README file for the long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Custom install command to check for Python version compatibility
class CustomInstallCommand(install):
    """Customized setuptools install command - installs dependencies and checks Python version."""
    def run(self):
        # Check Python version
        if sys.version_info < (3, 7):
            raise RuntimeError("This package requires Python 3.7 or higher.")
        install.run(self)

setup(
    name="quantum_pi_network",  # Replace with your package name
    version="0.1.0",  # Initial version
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="A powerful and advanced quantum network simulation framework.",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quantum_pi_network",  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find packages in the current directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # Change as needed
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Natural Language :: English",
    ],
    python_requires='>=3.7',  # Specify the minimum Python version
    install_requires=[
        "pandas==1.5.3",
        "numpy==1.23.5",
        "tensorflow==2.11.0",
        "scikit-learn==1.1.3",
        "web3==5.31.0",
        "matplotlib==3.6.2",
        "seaborn==0.11.2",
        "jupyter==1.0.0",
        "python-dotenv==0.20.0",
        "pytest==7.2.0",
        "requests==2.32.4",
        "beautifulsoup4==4.11.1",
        "Flask-SocketIO==5.3.0",
        "Flask-JWT-Extended==4.4.0",
        "cryptography==37.0.2",
        "dask==2022.10.0",
        "xgboost==1.6.2",
        "lightgbm==3.3.2",
    ],
    entry_points={
        'console_scripts': [
            'quantum-pi=quantum_pi_network.main:main',  # Replace with your main entry point
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
    },
)

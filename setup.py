from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("config/requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="dss-gymnasium",
    version="1.0.0",
    author="DSS-Gymnasium Team",
    author_email="your-email@example.com",
    description="Deep Reinforcement Learning for Distribution System Operations using OpenDSS, Gymnasium, and Stable Baselines3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/DSS-Gymnasium",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dss-gym-train=scripts.train_simple_pv:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.dss", "*.csv", "*.txt"],
    },
)

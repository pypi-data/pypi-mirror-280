from setuptools import setup, find_packages

setup(
    name="django-api-vue",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Django>=3.2",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Django framework tailored for APIs with Vue.js frontend integration.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
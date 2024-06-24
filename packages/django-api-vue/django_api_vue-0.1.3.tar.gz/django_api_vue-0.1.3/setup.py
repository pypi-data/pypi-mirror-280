from setuptools import setup, find_packages

setup(
    name="django-api-vue",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "Django>=3.2",
    ],
    author="Song Hao",
    author_email="173077850@qq.com",
    description="A Django framework tailored for APIs with Vue.js frontend integration.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

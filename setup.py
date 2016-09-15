from setuptools import setup, find_packages

setup(
    name="fixed-width",
    version='1.0.0',
    author="madisona",
    author_email="aaron.l.madison@gmail.com",
    description="Convert Python Objects to/from fixed format records.",
    url="https://github.com/madisona/django-copybook",
    long_description=open('README.txt', 'r').read(),
    packages=find_packages(),
    install_requires=['six'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
)

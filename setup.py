from setuptools import setup

from herokuapp import __version__


version_str = ".".join(str(n) for n in __version__)
        

setup(
    name = "django-herokuapp",
    version = version_str,
    license = "BSD",
    description = "A set of utilities and a project template for running Django sites on heroku.",
    author = "Dave Hall",
    author_email = "dave@etianen.com",
    url = "https://github.com/etianen/django-herokuapp",
    entry_points = {
        "console_scripts": [
            "start_herokuapp_project = herokuapp.bin.start_herokuapp_project:main",
        ],
    },
    packages = [
        "herokuapp",
        "herokuapp.bin",
        "herokuapp.management",
        "herokuapp.management.commands",
    ],
    package_data = {
        "herokuapp": [
            "project_template/*.py",
            "project_template/*.conf",
            "project_template/*.txt",
            "project_template/Procfile",
            "project_template/project_name/*.py",
            "project_template/project_name/templates/.gitignore",
            "project_template/project_name/static/js/.gitignore",
            "project_template/project_name/apps/*.py",
            "project_template/project_name/settings/*.py",
            "project_template/project_name/static/*.py",
        ],
    },
    install_requires = [
        "django",
        "pytz",
        "waitress",
    ],
    extras_require = {
        "postgres": [
            "dj-database-url",
            "psycopg2",
        ],
        "s3": [
            "django-storages",
            "boto",
        ],
        "requirejs": [
            "django-require-s3",
        ],
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
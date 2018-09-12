#!/usr/bin/env python
"""Setup script"""

from setuptools import setup


with open('README.md') as fp:
    README = fp.read()


setup(
    name='kibitzr-sentry',
    version='1.0.0',
    description="Kibitzr integration with Sentry",
    long_description=README,
    long_description_content_type='text/markdown',
    author="Peter Demin",
    author_email='kibitzrrr@gmail.com',
    url='https://github.com/kibitzr/kibitzr-sentry',
    py_modules=[
        'kibitzr_sentry',
    ],
    entry_points={
        'kibitzr.before_start': [
            'before_start=kibitzr_sentry:on_before_start'
        ]
    },
    install_requires=['kibitzr', 'raven'],
    license="MIT license",
    zip_safe=False,
    keywords='kibitzr',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

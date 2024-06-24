.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/jorwoods/sweet_logs/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Sweet Logs could always use more documentation, whether as part of the
official Sweet Logs docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/jorwoods/sweet_logs/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `sweet_logs` for local development.

1. Fork the `sweet_logs` repo on GitHub.
2. Clone your fork locally::

.. code-block:: bash
    git clone git@github.com:your_name_here/sweet_logs.git

3. Install your local copy into a virtualenv.

.. code-block:: bash
    mkvirtualenv sweet_logs
    cd sweet_logs/
    python setup.py develop

4. Create a branch for local development::

.. code-block:: bash
     git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass ruff and the
   tests, including testing other Python::

.. code-block:: bash
    ruff sweet_logs tests
    pytest

   To get ruff, just pip install it into your virtualenv.

6. Commit your changes and push your branch to GitHub::

.. code-block:: bash
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.8+.

Tips
----

To run a subset of tests::

.. code-block:: bash
  pytest tests.test_sweet_logs


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

.. code-block:: bash
    git push
    git push --tags

GitHub will then deploy to PyPI if tests pass.

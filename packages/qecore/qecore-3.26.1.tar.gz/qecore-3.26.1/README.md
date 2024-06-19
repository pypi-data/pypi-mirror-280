## qecore

[![Build Status](https://img.shields.io/gitlab/pipeline/dogtail/qecore)](https://gitlab.com/dogtail/qecore/-/pipelines) [![PyPI Version](https://img.shields.io/pypi/v/qecore)](https://pypi.org/project/qecore/)

The future goal for qecore is for it to become project template for automation testing.
As of now the qecore provides a lot of quality of life features for GNOME Desktop testing.

It can be described as a sandbox of sorts for test execution.
Paired with behave and dogtail this project serves as a useful tool for test execution with minimal required setup.

[Project Documentation in gitlab Pages](https://dogtail.gitlab.io/qecore/index.html) - build by CI pipelines on every change


## This project was featured in Fedora Magazine:
  - https://fedoramagazine.org/automation-through-accessibility/
  - Full technical solution of our team's (Red Hat DesktopQE) automation stack https://modehnal.github.io/


### Execute unit tests

Execute the tests (from the project root directory) on machine with dogtail:

```bash
rm -f /tmp/qecore_version_status.txt
rm -f dist/*.whl
python3 -m build
python3 -m pip install --force-reinstall --upgrade dist/qecore*.whl
sudo -u test scripts/qecore-headless "behave -f html-pretty -o /tmp/report_qecore.html -f plain tests/features"
```

You can use `-f pretty` instead of `-f plain` to get colored output.

The standard output should not contain any python traceback, produced HTML should be complete (after first scenario there is `Status`).

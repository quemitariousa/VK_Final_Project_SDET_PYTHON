#!/bin/bash

pytest -s -v -l /tmp/code/api/tests_api/test_api.py --alluredir=/tmp/allure-results
#pytest -s -v -l /tmp/code/ui/tests_ui/test_ui.py --alluredir=/tmp/allure-results



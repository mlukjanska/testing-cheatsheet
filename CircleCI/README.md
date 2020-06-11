# About

Quick cheatsheet list for [CircleCI](https:/circleci.com/).

## Content

- [Configure environment variables](#configure-environment-variables)
- [Split tests by timings for parallel run](#split-tests-by-timings-for-parallel-run)

## Configure environment variables

It is possible to do with the sed command replacing respective variables in the project's environment/configuration file.

Tip: use delimiter in the `<sed>` command '|' in case you need also to replace URLs that contain forward slashes '/', nevertheless if your values might contain the delimiter '|' then you'll need to come up with a different one.

Example of the circleci command:

`<{%CIRCLECI_ACCEPTANCE_USERNAME%}>` - this value will be replaces (it will be in the file)
`<${ACCEPTANCE_USERNAME}>` - this is the CircleCI environment variable name and when running CircleCI build this will be replaced by the environment variable value.

```yml
    configure_acceptance_suite:
        description: "Configure Acceptance test suite"
        steps:
            - run:
                name: "Configure acceptance tests for circleci"
                command: |
                    sed -i "s|{%CIRCLECI_ACCEPTANCE_USERNAME%}|${ACCEPTANCE_USERNAME}|g" tests/acceptance.suite.circleci.yml
```

## Split tests by timings for parallel run

CircleCI supports the parallel test runs feature. In essence it allows splitting the tests across the containers based on their timing or class names.
In order to use splitting by timing you need to make sure that the test results store the relative paths to and not the full paths in the results files. 

Example:

Correct:

```xml
<testcase name="testOne" class="RoobHilpertDonnellyOldTest" file="tests/RoobHilpertDonnellyOldTest.php" assertions="2" time="92.572086"/>
```

Incorrect:

```xml
<testcase name="testOne" class="RoobHilpertDonnellyOldTest" file="root/project/tests/RoobHilpertDonnellyOldTest.php" assertions="2" time="92.572086"/>
```

In order to fix it you can clean up the file before using circleci `<store_test_results>`, also make sure to use `<when: always>`, in case the test run command fails since CircleCI does not execute the rest of the commands in the job.

```yml
      - run:
          name: "Clean up the absolute paths from the test report"
          command: sed -i 's/\/root\/project\///g' tests/_output/integration/result${CIRCLE_NODE_INDEX}.xml
          when: always
```

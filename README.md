# TechnicalTest

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#toolkit">Toolkit overview</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#prerequisites">Installation</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
        <ul>
            <li><a href="#reports">Artifacts and Reports</li>
            <li><a href="#CI/CD"> CI/CD </li>
        </ul>
    </li>
    <li><a href="#Limitations">Limitations</a></li>
    <li><a href="#Assumptions">Requirement Assumptions</a></li>
  </ol>
</details>

## Toolkit

As a brief overview, this submission uses the following tools/frameworks: 

| Function       | Tool           |
| -------------  | -------------  |
| Language       | <a href="https://www.python.org/about/">Python 3.12.7</a>  |
| UI Automation  | <a href="https://playwright.dev/python/docs/intro">Playwright</a>     |
| BDD test runner| <a href="https://behave.readthedocs.io/en/latest/">Behave</a>         |
| Reporting      | <a href="https://github.com/hrcorval/behavex">Behavex</a>        |
| Autoformatting | <a href="https://github.com/psf/black">Black</a>          | 

## Getting started 

### Prerequisites

    - Python 3.12.7
    - Pip

>[!NOTE]
>If you are on windows you may be required to install VS buildtools before you can install >greenlet (a dependency of playwright)
 
### Installation

1. Create a virtual environment in the repo directory
    ```
    python -m venv .venv
    ```
2. Pip install requirements.txt
    ```
    pip install -r requirements.txt
    ```
3. Install playwright with dependencies
    ```
    python -m playwright install --with-deps
    ```

## Usage

To execute the full test suite:
```
behavex ./
```
>[!NOTE] 
>Behavex suppresses all of the default behave logs. If you're running in headless mode (default) it is easy it mistake the lack of logs as the program hanging. The full suite shouldn't take more than 5 minutes on it's own. 
>
>The log level can be changed with the "--logging-level" parameter 

To execute a single feature file:
```
behavex -i <feature_file_name>
```
You dont need to specify an extension to the file. The feature name it'self can also be used. 

To execute all scenarios with a specific tag:
```
behavex -t <tag_expression>

behavex -t @fast_tests
behavex -t ~@slow_tests
```
Tag expressions can include negation (useful for avoiding long running tests)

To alter the runtime parameters of behave, you can edit the userdata section in behave.ini. This can be used to slow down the browser, change the browser target, or disable headless mode. You can also override the parameters with the -D flag
```
behave -D headless=false
```
Current custom parameters supported:
| parameter      | description                                                          | type |
| -------------  | -------------                                                        | ---- | 
| baseURL        | set a static variable containing the base URL inherited by all POMs  | String |
| headless       | enables headless mode. Any value other than 'true' is false | String |
| browser        | sets target browser. Options are chrome, firefox, or chromium. Any unrecognised value is defaulted to chromium | String |

# Reports

The run reports will be generated in the ./output folder. After running a test you'll find screenshots and logs for the run in the behavex HTML report.

# CI/CD

The github workflow "Trigger behave suite" can be used to execute the full test suite. The behavex report will be zipped and uploaded as an artifact upon completion. There are also pre and post merge workflows that also run the test on both firefox and chrome targets.  

## Limitations

The @repeat5 tag isn't clear about what it's doing in reporting. It's collapsing all 5 scenario runs into a single success or failure, which would ideally be handled on the report serving side. 

The current workflow doesn't merge test results between chrome and firefox runs and so can't return a single unified report. It also doesn't provide meaningful summary results to be displayed in github. The workflows are also currently duplicated instead of being reusable. 

## Assumptions

Given the nature of unsupervised technical tests I've taken the liberty of making some assumptions about the provided requirements.

Test case 1
- I've split this testcase into two parts. It's not ideal, but I had to compromise between the Given-When-Then BDD format and staying as strictly to the source of truth as possible. The two parts are the 'submit an empty form and verify errors' stage and 'confirm that an error doesn't prevent valid submission'.

- Since no error message or element was provided to verify against, I've used the banner at the top of the page. Originally I was also using the class of the parent element but felt like this wasn't very valuable (or true to the requirements). 

Test case 2 
- Repeating this test multiple times could be done a few different ways to different ends. For example, if we had dedicated runners we could load test the service with requests from multiple sources at once. For the sake of this submission I've opted to try and collapse all 5 instances of running this test into a single scenario without significantly increasing complexity. (i.e. If they all pass, it's one success). 

Test case 3
- In an effort to maintain transparency for a user reading the feature files, I decided to hardcode the expected values in the scenario. It's a trade off between having clear expectations and being inflexible to changes in the backend (e.g. price changes). Assuming we were in a managed slice, that's not an issue. 

- Since no data was provided I've taken the prices that were present at the time of writting and assumed they what was intended.

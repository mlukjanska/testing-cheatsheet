# About

> My personal list of useful testing software, scripts, extensions and resources collected over several years of testing career

## Content

- [Testing stratregy](#testing-strategy)
- [Test heuristics and checklists](#test-heuristics-and-checklists)
- [Tools](#tools)
  - [Functional automated testing](#functional-automated-testing)
    - [Web](#web)
    - [Mobile](#mobile)
  - [Visual and Content testing](#visual-and-content-testing)
  - [Performance testing](#performance-testing)
    - [Server side](#server-side)
    - [Client side](#client-side)
  - [Security testing](#security-testing)
  - [Usability testing](#usability-testing)
    - [Accessibility testing](#accessibility-testing)
  - [Contract testing](#contract-testing)
  - [Handy tools to make tester's life easier](#handy-tools-to-make-testers-life-easier)
    - [Email services](#email-services)
    - [Forms](#forms)
    - [Screenshots and recording](#screenshots-and-recording)
    - [CLI](#cli)
    - [Utilities](#utilities)
  - [Test reporting tools](#test-reporting-tools)
- [Scripts](#scripts)
- [Continuous Integration](#continuous-integration)
- [Blogs](#blogs)
- [Useful Resources](#useful-resources)
- [Communities and Conferences](#communities-and-conferences)
- [Articles](#Articles)

## Testing strategy
Various sources and articles about and around testing strategy (testing pyramid, testing types and other considerations)

- [Software Testing Guide (Martin Fowler)](https://martinfowler.com/testing/)

## Test heuristics and checklists

- [Test heuristics cheat sheet](http://testobsessed.com/wp-content/uploads/2011/04/testheuristicscheatsheetv1.pdf), [PDF in this repo](Heuristics/testheuristicscheatsheetv1.pdf) - Data type attacks, WEB tests, testing wisdom and frameworks
- [Software testing pyramid](https://archive.openconcept.ca/sites/openconcept/files/software_testing_cheat_sheet.pdf), [PDF in this repo](Heuristics/software_testing_cheat_sheet.pdf)

## Tools

### Functional automated testing

#### Web

- [Selenium](https://www.selenium.dev/) - web applications automation (multibrowser support).
- [Cypress](https://www.cypress.io/) - javascript end to end testing for browser based apps (not extensive multibrowser support).
- [Courgette](https://courgette-testing.com) - Simple UI testing. Proper declarative BDD scenarios using Gherkin, Gherkin templates and composable YAML-style page and component objects. Selenium-based UI Testing Framework written in JS that’s built on top of Cucumber with Protractor for desktop / hybrid apps and Cucumber with WDIO and appium for native mobile apps.
- [Codeception](https://codeception.com/) - collects and shares best practices and solutions for testing PHP web applications.

#### Mobile

- [http://appium.io/](Appium) - open source test automation framework for use with native, hybrid and mobile web apps. It drives iOS, Android, and Windows apps using the WebDriver protocol.

#### API

- [Postman](https://www.postman.com/) - the collaboration platform for API development.

### Visual and Content testing

- [Percy](https://percy.io/) - Automation tool for visual UI changes with versions comparison and workflows for changes approvals.
- [Applitools](https://applitools.com/products-eyes/) - Automated testing platform powered by Visual AI.
- [Fluxguard](https://fluxguard.com) - Screenshot pixel and DOM change comparisons and regressions.
- [recheck-web](https://github.com/retest/recheck-web) - Open Source change comparison tool with local Golden Masters, git-like ignore syntax and "unbreakable selenium" tests.

### (Docker) Containers testing

- [Container Structure Tests](https://github.com/GoogleContainerTools/container-structure-test) - validate the structure of a container image. These tests can be used to check the output of commands in an image, as well as verify metadata and contents of the filesystem.

### Performance testing

#### Server side

##### For endpoint checks

- [k6.io](https://k6.io/) - write your tests as a series of HTTP calls and assertions. k6 does the heavy lifting
- [Apache Bench](https://httpd.apache.org/docs/2.4/programs/ab.html) - designed to give you an impression of how your current Apache installation performs. This especially shows you how many requests per second your Apache installation is capable of serving
- [Siege](https://www.joedog.org/siege-home/) - an http load testing and benchmarking utility. It was designed to let web developers measure their code under duress, to see how it will stand up to load on the internet

##### Complex transactions

- [k6.io](https://k6.io/) - write your tests as a series of HTTP calls and assertions. k6 does the heavy lifting. 
- [Apache JMeter](https://jmeter.apache.org/) - popular tool with strong community backing, supports many different protocols and has rich extensibility that can be leveraged to customize the tool to your needs
- [Locust.io](http://locust.io/) - define user behaviour with Python code, and swarm your system with millions of simultaneous users
- [Gatling](https://gatling.io/) - code-like scripting with own developed Domain Specific Language (DSL) with web recorder and colorful reports
- [Taurus](https://gettaurus.org/) - test automation framework for Continuous Testing which helps by hiding the complexities of running performance tests. Think of it as an automation-friendly wrapper
- [Bees with Machine Guns](https://github.com/newsapps/beeswithmachineguns) - authors describe it as "a utility for arming (creating) many bees (micro EC2 instances) to attack (load test) targets (web applications)."
- [Multi-Mechanize](https://github.com/cgoldberg/multi-mechanize) - runs concurrent Python scripts to generate load (synthetic transactions), commonly used for web performance and scalability testing, but you can also use it to generate a workload against any remote API accessible from Python.
- [Siege](https://www.joedog.org/siege-home/) - designed to let web developers measure their code under duress, to see how it will stand up to load on the internet
- [Artillery](https://artillery.io/) - performance testing toolkit with YAML based scripts, built on top of Node.js and allows tests customization with Javascript code
- [Httperf](https://code.google.com/p/httperf/) - provides a flexible facility for generating varied HTTP workloads and measuring web server performance.
- [Element](https://element.flood.io/) - a Puppeteer node library that uses a browser-based load-testing tool, create scripts using Typescript, and use them against a web app in the same way that the customers would do, opening a browser and interacting with page elements.
- [Neoload](https://www.neotys.com/neoload/overview) - YAML based code description, but also with code-less capabilities

##### Solutions in the cloud

- [Blazemeter](https://www.blazemeter.com/product/performance-testing) - continuous testing including performance testing
- [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) - a scalable, distributed, and serverless architecture to deliver a load testing tool for web application performance testing (demo)
- [Distributed load testing using Google Kubernetes Engine with Locust](https://cloud.google.com/solutions/distributed-load-testing-using-gke) - Google Kubernetes Engine (GKE) to deploy a distributed load testing framework that uses multiple containers to create traffic for a simple REST-based API
- [Alternatives in Azure](https://docs.microsoft.com/en-us/azure/devops/test/load-test/overview?view=azure-devops#alternatives)

#### Client side

- [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) - is an open-source, automated tool for improving the quality of web pages, is available in Google Chrome tools.
- [Google PageSpeed Insights and Tools](https://developers.google.com/speed/pagespeed/insights/) - a service that analyzes the content of a web page and generates suggestions to make your pages load faster. Reducing page load times reduces bounce rates and increases conversion rates.
- [sitespeed.io](https://www.sitespeed.io/) - a set of open source tools evaluating client-side performance from real browsers.
- [webpagetest.org](https://www.webpagetest.org/) - a service that provides insights into the performance of the client side in a variety of real browsers. This utility will test a web page in any browser, from any location, over any network condition—and it's free.
- [Yslow](http://yslow.org/) - Analyse why web pages are slow based on Yahoo!'s rules for performance. Last update on 15.03.2014

#### Reusing the functional test tools

- Cypress to [capture Google Chrome's performance data](https://www.cypress.io/blog/2019/05/22/how-we-improved-network-speed-by-300-in-cypress-3-3-0/) - allows to find and fix common performance issues such as slow-time-to-first-byte.
- Selenium and [BrowserMob Proxy (BMP)](https://github.com/lightbody/browsermob-proxy) - has a few ways to capture performance data as well. One common approach is using a HAR file. This is done using the BrowserMob Proxy (BMP). BMP lets you manipulate HTTP requests and responses, capture HTTP content, and export performance data as a HAR file.
- [JMeter Webdriver Sampler](https://www.blazemeter.com/blog/jmeter-webdriver-sampler/) with Selenium Webdriver - useful for testing the performance of AJAX, GWT-based web applications, and simulated user actions.

### Security testing

#### Checklists and how-tos
- [Cheatsheet God](https://github.com/OlivierLaflamme/Cheatsheet-God) - a collection of resources, scripts and easy to follow how-to's for OSCP and general penetration testing.

#### Tools
- [Tracy](https://github.com/nccgroup/tracy) - A pentesting tool designed to assist with finding all sinks and sources of a web application and display these results in a digestible manner.
- [Burp Suite](https://portswigger.net/burp/communitydownload) - Burp Suite Community Edition is a feature-limited set of manual tools for exploring web security. Proxy your HTTPS traffic, edit and repeat requests, decode data, and more.
- [Requestly](https://requestly.io/) - Setup redirects, modify headers, switch hosts, insert user scripts, cancel requests and much more.
- [Fiddler](https://www.telerik.com/fiddler) - Capture all HTTP(S) traffic between your computer and the Internet with Fiddler HTTP(S) proxy. Inspect traffic, set breakpoints, and fiddle with requests & responses.
- [BeEF](http://beefproject.com/) - Manipulate the browser exploiting any XSS vulnerabilities you find.
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) - This intercepting proxy allows you to see all HTTP traffic and manipulate it in real time. Easy to scan, catalog and exploit security issues.
- [Cookie Inspector](https://chrome.google.com/webstore/detail/cookie-inspector/jgbbilmfbammlbbhmmgaagdkbkepnijn) - View and Edit Cookies easily using the developer tools pane.

### Usability testing

#### Accessibility testing
Ensure that the application being tested is usable by people with disabilities like hearing, color blindness, old age and other disadvantaged groups

- [Colour Blindness Simulator](https://altreus.github.io/colourblind/) - Simulate all types of Colour Blindness instantly!

### Contract Testing
Ensure that services (an API provider, a client etc) can communicate with each other.

Good articles describing consumer driven contracts in details: 
- [Consumer-Driven Contracts: A Service Evolution Pattern](https://martinfowler.com/articles/consumerDrivenContracts.html)
- [Contract test](https://martinfowler.com/bliki/ContractTest.html)

Tools:
- [Pact](https://docs.pact.io/)
- [Postman Collections](https://www.postman.com/collection/)


### Handy tools to make tester's life easier

#### Email services
Sometimes for end to end testing we need to use email services and be able to access those programatically ie create email account and read emails. The following services can be considered depending on the user cases (for full services review read this [article](https://medium.com/koahealth/why-you-shouldnt-use-guerrillamail-for-automated-e2e-testing-use-mailslurp-instead-a73f16240444)):

- [MailSlurp](https://www.mailslurp.com/) - probably the best suited for testing
- [Mailosaur](https://mailosaur.com/) - probably the best suited for testing
- [Mailinator](https://www.mailinator.com/v4/pricing.jsp)
- [Gmail API](https://developers.google.com/gmail/api/guides)
- [MessageBird](https://www.messagebird.com/en/pricing)
- [Mailgun](https://mailgun.com/)


#### Forms

- [Form Filler](https://chrome.google.com/webstore/detail/form-filler/bnjjngeaknajbdcgpfkgnonkmififhfo) - Large forms can be really irritating to fill out each time, speed it up with dummy data.
- [Bug Magnet](https://chrome.google.com/webstore/detail/bug-magnet/efhedldbjahpgjcneebmbolkalbhckfi) - Suggests values based on the field type.
- [Check All](https://chrispederick.com/work/web-developer/) - "Select All" is often not available. Why not bring your own?

#### Screenshots and recording

- [Full Page Screenshot](https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl) - For when PrintScreen isn't big enough.
- [Loom](https://www.loom.com/) - Google Chrome extension to record video of a website, automatically uploaded to loom and with link generated to view the video.
- [Captura](https://github.com/MathewSachin/Captura) - Open Source video recording tool.

#### CLI

- [BareTail](https://www.baremetalsoft.com/baretail/) - Brings the tail linux command to Windows, coloured lines and REGEX search and loads of other features.
- [ProxySwitcher](https://chrome.google.com/webstore/detail/proxy-switcher-manager/onnfghpihccifgojkpnnncpagjcdbjod) - We all have to mess with proxies, this makes it a lot easier when using Test/Prod/localhost proxies.

#### Utilities

- [MyWords](https://addons.mozilla.org/en-US/firefox/addon/mywords/) - Handy extension that can be used to save common snippets (Jira tables, test data etc.) you use often for easy typing.
- [Xmind](http://www.xmind.net/) - The free mindmapping tool for documenting your tests.
- [Cookie Inspector](https://chrome.google.com/webstore/detail/cookie-inspector/jgbbilmfbammlbbhmmgaagdkbkepnijn) - View and Edit Cookies easily using the developer tools pane.

## Test reporting tools

- [Reportportal.io](https://reportportal.io/) - AI-powered test automation dashboard
- [Allure](http://allure.qatools.ru/) - multi-language test report tool with graphical test results representations
- [Dashing.io](http://dashing.io/) - dashboard framework, so you'll need to implement visualizations yourself


## Scripts

Collection of useful scripts:

- [compareCSV.py](Scripts/compareCSV.py) - Python script to compare CSV files for differences

## Continuous Integration

### CircleCI

- [Cheatsheet for the config.yml](CircleCI/README.md)

### Github

- [Multiple github accounts on Mac](https://medium.com/@ibrahimlawal/developing-with-multiple-github-accounts-on-one-macbook-94ff6d4ab9ca) - how to setup multiple github accounts on Mac

## Blogs

- [James Bach](http://www.satisfice.com/blog/) - exploratory testing, Rapid Software Testing methodology inventor, founder of Context-Driven School of testing.
- [Michael Bolton](http://www.developsense.com/blog/) - co-author of Rapid Software Testing methodology.
- [Janet Gregory](http://janetgregory.ca/blog/) - Agile testing.
- [Nielsen Group](https://www.nngroup.com/) - all about UX and usability.
- [Martin Fowler](https://martinfowler.com/) - agile software development tech patterns, microservices best practices.

## Useful Resources

### Handy lists for testers

- [Falsehoods](https://github.com/kdeldycke/awesome-falsehood) - A funny and educational list of why nothing in Software Development is ever easy.
- [Naughty Strings](https://github.com/minimaxir/big-list-of-naughty-strings) - This is the famous list of Naughty Strings. If you're doing some field validation, look no further for inspiration.
- [Unicode](https://github.com/jagracey/Awesome-Unicode) - A great resource for learning how unicode works and the issues it can cause.

### Useful awesome lists

- [Awesome Testing](https://github.com/TheJambo/awesome-testing/blob/master/README.md) - A curated list of testing software, extensions and resources.
- [Learn to Code](https://github.com/karlhorky/learn-to-program) - Learning to code, for those looking to make the move to automation
- [Application Security](https://github.com/paragonie/awesome-appsec) - Incredibly extensive, but you'll find something to fit the bill.
- [Selenium](https://github.com/christian-bromann/awesome-selenium) - Better than searching Google if you know what you want.
- [Security](https://github.com/sbilly/awesome-security) - This is mostly focused on Infrastructure, but if you're testing a series of systems, this is very useful.
- [Awesome Software Quality](https://github.com/ligurio/awesome-software-quality) - A list of free software testing and verification resources.
- [Awesome Cucumber](https://github.com/virajkulkarni14/awesome-cucumber) - A (relatively-newer) curated list of awesome Cucumber and Gherkin-related resources.
- [Awesome JMeter](https://github.com/aliesbelik/awesome-jmeter) - A curated collection of resources around Apache JMeter.
- [How They Test](https://github.com/abhivaikar/howtheytest) - A curated collection of public resources from tech companies on how they test their software and build a quality culture

### Useful resources

- [ISTQB](https://www.istqb.org/) - Organization to certify testers, but also has glossary of testing terms and description of the testing processes - handy reference when setting up testing from scratch.
- [Technology Radar](https://www.thoughtworks.com/) - an opinionated guide to technology frontiers.

## Communities and Conferences

- [Testers.io](http://www.testers.io/) - Community Slack for testers to discuss everything and rant. Mostly rant.
- [Software Testing Conferences](http://testingconferences.org/) - A list of software testing conferences and workshops.

## Articles

- [Visual testing of a Unity-based 3D world](https://www.coderskitchen.com/visual-testing-of-a-unity-based-3d-world/?li_fat_id=93bfb453-48f6-420c-a58e-8b049a3fab85)
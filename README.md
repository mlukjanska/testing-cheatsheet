# About

> My personal list of useful testing software, scripts, extensions and resources collected over several years of testing career

## Content

- [Tools](#tools)
  - [Functional automated testing](#functional-automated-testing)
  - [Visual and Content testing](#visual-and-content-testing)
  - [Performance testing](#performance-testing)
  - [Security testing](#security-testing)
- [Scripts](#scripts)
- [Continuous Integration](#continuous-integration)
- [Blogs](#blogs)
- [Useful Resources](#useful-resources)
- [Others](#Others)

## Tools

### Functional automated testing

#### Web

- [Courgette](https://courgette-testing.com) - Simple UI testing. Proper declarative BDD scenarios using Gherkin, Gherkin templates and composable YAML-style page and component objects. Selenium-based UI Testing Framework written in JS that’s built on top of Cucumber with Protractor for desktop / hybrid apps and Cucumber with WDIO and appium for native mobile apps.
- [Selenium](https://www.selenium.dev/) - web applications automation (multibrowser support).
- [Cypress](https://www.cypress.io/) - javascript end to end testing for browser based apps (not extensive multibrowser support).

#### Mobile

#### API

### Visual and Content testing

- [Percy](https://percy.io/) - Automation tool for visual UI changes with versions comparison and workflows for changes approvals.
- [Applitools](https://applitools.com/products-eyes/) - Automated testing platform powered by Visual AI.
- [Fluxguard](https://fluxguard.com) - Screenshot pixel and DOM change comparisons and regressions.
- [recheck-web](https://github.com/retest/recheck-web) - Open Source change comparison tool with local Golden Masters, git-like ignore syntax and "unbreakable selenium" tests.

### (Docker) Containers testing

- [Container Structure Tests](https://github.com/GoogleContainerTools/container-structure-test) - validate the structure of a container image. These tests can be used to check the output of commands in an image, as well as verify metadata and contents of the filesystem.

### Performance testing

### Security testing

- [Tracy](https://github.com/nccgroup/tracy) - A pentesting tool designed to assist with finding all sinks and sources of a web application and display these results in a digestible manner.
- [Burp Suite](https://portswigger.net/burp/communitydownload) - Burp Suite Community Edition is a feature-limited set of manual tools for exploring web security. Proxy your HTTPS traffic, edit and repeat requests, decode data, and more.
- [Requestly](https://requestly.io/) - Setup redirects, modify headers, switch hosts, insert user scripts, cancel requests and much more.
- [Fiddler](https://www.telerik.com/fiddler) - Setup redirects, modify headers, switch hosts, insert user scripts, cancel requests and much more.
- [BeEF](http://beefproject.com/) - Manipulate the browser exploiting any XSS vulnerabilities you find.
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) - This intercepting proxy allows you to see all HTTP traffic and manipulate it in real time. Easy to scan, catalog and exploit security issues.
- [Cookie Inspector](https://chrome.google.com/webstore/detail/cookie-inspector/jgbbilmfbammlbbhmmgaagdkbkepnijn) - View and Edit Cookies easily using the developer tools pane.

### Handy tools to make tester's life easier

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
- [Xmind](http://www.xmind.net/) - The best (free) Mindmapping tool for documenting your tests.

### Other

- [Colour Blindness Simulator](https://altreus.github.io/colourblind/) - Simulate all types of Colour Blindness instantly!
- [Yslow](http://yslow.org/) - Analyse why web pages are slow based on Yahoo!'s rules for performance.

## Scripts

Collection of useful scripts:

- [compareCSV.py](Scripts/compareCSV.py) - Python script to compare CSV files for differences

## Continuous Integration

### CircleCI

- [Cheatsheet for the config.yml](CircleCI/README.md)

### Github

- [Multiple github accounts on Mac](https://medium.com/@ibrahimlawal/developing-with-multiple-github-accounts-on-one-macbook-94ff6d4ab9ca) - how to setup multiple github accounts on Mac

## Blogs

- [James Bach](http://www.satisfice.com/blog/)
- [Michael Bolton](http://www.developsense.com/blog/)
- [Janet Gregory](http://janetgregory.ca/blog/)

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

### Other useful resources

- [ISTQB](https://www.istqb.org/) - Organization to certify testers, but also has glossary of testing terms and description of the testing processes - handy reference when setting up testing from scratch.

## Other

- [Testers.io](http://www.testers.io/) - Community Slack for testers to discuss everything and rant. Mostly rant.
- [Software Testing Conferences](http://testingconferences.org/) - A list of software testing conferences and workshops.

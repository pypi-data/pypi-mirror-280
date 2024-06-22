[![Build Status](https://github.com/khulnasoft/khulnasoft-sdk-python/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/khulnasoft/khulnasoft-sdk-python/actions/workflows/test.yml)

[Reference Docs](https://dev.khulnasoft.com/enterprise/reference)

# The Khulnasoft Enterprise Software Development Kit for Python

#### Version 2.0.1

The Khulnasoft Enterprise Software Development Kit (SDK) for Python contains library code designed to enable developers to build applications using the Khulnasoft platform.

The Khulnasoft platform is a search engine and analytic environment that uses a distributed map-reduce architecture to efficiently index, search, and process large time-varying data sets.

The Khulnasoft platform is popular with system administrators for aggregation and monitoring of IT machine data, security, compliance, and a wide variety of other scenarios that share a requirement to efficiently index, search, analyze, and generate real-time notifications from large volumes of time-series data.

The Khulnasoft developer platform enables developers to take advantage of the same technology used by the Khulnasoft platform to build exciting new applications.

## Getting started with the Khulnasoft SDK for Python


## Get started with the Khulnasoft Enterprise SDK for Python

The Khulnasoft Enterprise SDK for Python contains library code, and its examples are located in the [khulnasoft-app-examples](https://github.com/khulnasoft/khulnasoft-app-examples) repository. They show how to programmatically interact with the Khulnasoft platform for a variety of scenarios including searching, saved searches, data inputs, and many more, along with building complete applications.

### Requirements

Here's what you need to get going with the Khulnasoft Enterprise SDK for Python.

* Python 3.7 or Python 3.9 
  
  The Khulnasoft Enterprise SDK for Python is compatible with python3 and has been tested with Python v3.7 and v3.9.

* Khulnasoft Enterprise 9.2 or 8.2

    The Khulnasoft Enterprise SDK for Python has been tested with Khulnasoft Enterprise 9.2, 8.2 and 8.1

  If you haven't already installed Khulnasoft Enterprise, download it [here](http://www.khulnasoft.com/download). 
  For more information, see the Khulnasoft Enterprise [_Installation Manual_](https://docs.khulnasoft.com/Documentation/Khulnasoft/latest/Installation).

* Khulnasoft Enterprise SDK for Python

  Get the Khulnasoft Enterprise SDK for Python from [PyPI](https://pypi.org/project/khulnasoft-sdk/). If you want to contribute to the SDK, clone the repository from [GitHub](https://github.com/khulnasoft/khulnasoft-sdk-python).

### Install the SDK

Use the following commands to install the Khulnasoft Enterprise SDK for Python libraries. However, it's not necessary to install the libraries to run the unit tests from the SDK.

Use `pip`:

    [sudo] pip install khulnasoft-sdk

Install the Python egg:

    [sudo] pip install --egg khulnasoft-sdk

Install the sources you cloned from GitHub:

    [sudo] python setup.py install

## Testing Quickstart

You'll need `docker` and `docker-compose` to get up and running using this method.

```
make up KHULNASOFT_VERSION=9.2
make wait_up
make test
make down
```

To run the examples and unit tests, you must put the root of the SDK on your PYTHONPATH. For example, if you downloaded the SDK to your home folder and are running OS X or Linux, add the following line to your **.bash_profile** file:

    export PYTHONPATH=~/khulnasoft-sdk-python

### Following are the different ways to connect to Khulnasoft Enterprise
#### Using username/password
```python
import khulnasoftlib.client as client
service = client.connect(host=<host_url>, username=<username>, password=<password>, autologin=True)
```

#### Using bearer token
```python
import khulnasoftlib.client as client
service = client.connect(host=<host_url>, khulnasoftToken=<bearer_token>, autologin=True)
```

#### Using session key
```python
import khulnasoftlib.client as client
service = client.connect(host=<host_url>, token=<session_key>, autologin=True)
```

###
#### Update a .env file

To connect to Khulnasoft Enterprise, many of the SDK examples and unit tests take command-line arguments that specify values for the host, port, and login credentials for Khulnasoft Enterprise. For convenience during development, you can store these arguments as key-value pairs in a **.env** file. Then, the SDK examples and unit tests use the values from the **.env** file when you don't specify them.

>**Note**: Storing login credentials in the **.env** file is only for convenience during development. This file isn't part of the Khulnasoft platform and shouldn't be used for storing user credentials for production. And, if you're at all concerned about the security of your credentials, enter them at the command line rather than saving them in this file.

here is an example of .env file:

    # Khulnasoft Enterprise host (default: localhost)
    host=localhost
    # Khulnasoft Enterprise admin port (default: 8089)
    port=8089
    # Khulnasoft Enterprise username
    username=admin
    # Khulnasoft Enterprise password
    password=changed!
    # Access scheme (default: https)
    scheme=https
    # Your version of Khulnasoft Enterprise
    version=9.2
    # Bearer token for authentication
    #khulnasoftToken=<Bearer-token>
    # Session key for authentication
    #token=<Session-Key>

#### SDK examples

Examples for the Khulnasoft Enterprise SDK for Python are located in the [khulnasoft-app-examples](https://github.com/khulnasoft/khulnasoft-app-examples) repository. For details, see the [Examples using the Khulnasoft Enterprise SDK for Python](https://dev.khulnasoft.com/enterprise/docs/devtools/python/sdk-python/examplespython) on the Khulnasoft Developer Portal.

#### Run the unit tests

The Khulnasoft Enterprise SDK for Python contains a collection of unit tests. To run them, open a command prompt in the **/khulnasoft-sdk-python** directory and enter:

    make

You can also run individual test files, which are located in **/khulnasoft-sdk-python/tests**. To run a specific test, enter:

    make test_specific

The test suite uses Python's standard library, the built-in `unittest` library, `pytest`, and `tox`.

>**Notes:**
>*  The test run fails unless the [SDK App Collection](https://github.com/khulnasoft/sdk-app-collection) app is installed.
>*  To exclude app-specific tests, use the `make test_no_app` command.
>*  To learn about our testing framework, see [Khulnasoft Test Suite](https://github.com/khulnasoft/khulnasoft-sdk-python/tree/master/tests) on GitHub.
>   In addition, the test run requires you to build the searchcommands app. The `make` command runs the tasks to do this, but more complex testing may require you to rebuild using the `make build_app` command.

## Repository

| Directory | Description                                                |
|:--------- |:---------------------------------------------------------- |
|/docs      | Source for Sphinx-based docs and build                     |
|/khulnasoftlib | Source for the Khulnasoft library modules                      |
|/tests     | Source for unit tests                                      |
|/utils     | Source for utilities shared by the unit tests              |

### Customization
* When working with custom search commands such as Custom Streaming Commands or Custom Generating Commands, We may need to add new fields to the records based on certain conditions.
* Structural changes like this may not be preserved.
* Make sure to use ``add_field(record, fieldname, value)`` method from SearchCommand to add a new field and value to the record.
* ___Note:__ Usage of ``add_field`` method is completely optional, if you are not facing any issues with field retention._

Do
```python
class CustomStreamingCommand(StreamingCommand):
    def stream(self, records):
        for index, record in enumerate(records):
            if index % 1 == 0:
                self.add_field(record, "odd_record", "true")
            yield record
```

Don't
```python
class CustomStreamingCommand(StreamingCommand):
    def stream(self, records):
        for index, record in enumerate(records):
            if index % 1 == 0:
                record["odd_record"] = "true"
            yield record
```
### Customization for Generating Custom Search Command
* Generating Custom Search Command is used to generate events using SDK code.
* Make sure to use ``gen_record()`` method from SearchCommand to add a new record and pass event data as a key=value pair separated by , (mentioned in below example).

Do
```python
@Configuration()
class GeneratorTest(GeneratingCommand):
    def generate(self):
        yield self.gen_record(_time=time.time(), one=1)
        yield self.gen_record(_time=time.time(), two=2)
```

Don't
```python
@Configuration()
class GeneratorTest(GeneratingCommand):
    def generate(self):
        yield {'_time': time.time(), 'one': 1}
        yield {'_time': time.time(), 'two': 2}
```

### Access metadata of modular inputs app
* In stream_events() method we can access modular input app metadata from InputDefinition object
* See [GitHub Commit](https://github.com/khulnasoft/khulnasoft-app-examples/blob/master/modularinputs/python/github_commits/bin/github_commits.py) Modular input App example for reference.
```python
    def stream_events(self, inputs, ew):
        # other code
        
        # access metadata (like server_host, server_uri, etc) of modular inputs app from InputDefinition object
        # here inputs is a InputDefinition object
        server_host = inputs.metadata["server_host"]
        server_uri = inputs.metadata["server_uri"]
        
        # Get the checkpoint directory out of the modular input's metadata
        checkpoint_dir = inputs.metadata["checkpoint_dir"]
```

### Access service object in Custom Search Command & Modular Input apps

#### Custom Search Commands
* The service object is created from the Khulnasoftd URI and session key passed to the command invocation the search results info file.
* Service object can be accessed using `self.service` in `generate`/`transform`/`stream`/`reduce` methods depending on the Custom Search Command.
* For Generating Custom Search Command
  ```python
    def generate(self):
        # other code
        
        # access service object that can be used to connect Khulnasoft Service
        service = self.service
        # to get Khulnasoft Service Info
        info = service.info
  ```

 

#### Modular Inputs app:
* The service object is created from the Khulnasoftd URI and session key passed to the command invocation on the modular input stream respectively.
* It is available as soon as the `Script.stream_events` method is called.
```python
    def stream_events(self, inputs, ew):
        # other code
        
        # access service object that can be used to connect Khulnasoft Service
        service = self.service
        # to get Khulnasoft Service Info
        info = service.info
```


### Optional:Set up logging for khulnasoftlib
+ The default level is WARNING, which means that only events of this level and above will be visible
+ To change a logging level we can call setup_logging() method and pass the logging level as an argument.
+ Optional: we can also pass log format and date format string as a method argument to modify default format

```python
import logging
from khulnasoftlib import setup_logging

# To see debug and above level logs
setup_logging(logging.DEBUG)
```

### Changelog

The [CHANGELOG](CHANGELOG.md) contains a description of changes for each version of the SDK. For the latest version, see the [CHANGELOG.md](https://github.com/khulnasoft/khulnasoft-sdk-python/blob/master/CHANGELOG.md) on GitHub.

### Branches

The **master** branch represents a stable and released version of the SDK.
To learn about our branching model, see [Branching Model](https://github.com/khulnasoft/khulnasoft-sdk-python/wiki/Branching-Model) on GitHub.

## Documentation and resources

| Resource                | Description |
|:----------------------- |:----------- |
| [Khulnasoft Developer Portal](http://dev.khulnasoft.com) | General developer documentation, tools, and examples |
| [Integrate the Khulnasoft platform using development tools for Python](https://dev.khulnasoft.com/enterprise/docs/devtools/python)| Documentation for Python development |
| [Khulnasoft Enterprise SDK for Python Reference](http://docs.khulnasoft.com/Documentation/PythonSDK) | SDK API reference documentation |
| [REST API Reference Manual](https://docs.khulnasoft.com/Documentation/Khulnasoft/latest/RESTREF/RESTprolog) | Khulnasoft REST API reference documentation |
| [Khulnasoft>Docs](https://docs.khulnasoft.com/Documentation) | General documentation for the Khulnasoft platform |
| [GitHub Wiki](https://github.com/khulnasoft/khulnasoft-sdk-python/wiki/) | Documentation for this SDK's repository on GitHub |
| [Khulnasoft Enterprise SDK for Python Examples](https://github.com/khulnasoft/khulnasoft-app-examples) | Examples for this SDK's repository |

## Community

Stay connected with other developers building on the Khulnasoft platform.

* [Email](mailto:devinfo@khulnasoft.com)
* [Issues and pull requests](https://github.com/khulnasoft/khulnasoft-sdk-python/issues/)
* [Community Slack](https://khulnasoft-usergroups.slack.com/app_redirect?channel=appdev)
* [Khulnasoft Answers](https://community.khulnasoft.com/t5/Khulnasoft-Development/ct-p/developer-tools)
* [Khulnasoft Blogs](https://www.khulnasoft.com/blog)
* [Twitter](https://twitter.com/khulnasoftdev)

### Contributions

If you would like to contribute to the SDK, see [Contributing to Khulnasoft](https://www.khulnasoft.com/en_us/form/contributions.html). For additional guidelines, see [CONTRIBUTING](CONTRIBUTING.md). 

### Support

*  You will be granted support if you or your company are already covered under an existing maintenance/support agreement. Submit a new case in the [Support Portal](https://www.khulnasoft.com/en_us/support-and-services.html) and include "Khulnasoft Enterprise SDK for Python" in the subject line.

   If you are not covered under an existing maintenance/support agreement, you can find help through the broader community at [Khulnasoft Answers](https://community.khulnasoft.com/t5/Khulnasoft-Development/ct-p/developer-tools).

*  Khulnasoft will NOT provide support for SDKs if the core library (the code in the <b>/khulnasoftlib</b> directory) has been modified. If you modify an SDK and want support, you can find help through the broader community and [Khulnasoft Answers](https://community.khulnasoft.com/t5/Khulnasoft-Development/ct-p/developer-tools). 

   We would also like to know why you modified the core library, so please send feedback to _devinfo@khulnasoft.com_.

*  File any issues on [GitHub](https://github.com/khulnasoft/khulnasoft-sdk-python/issues).

### Contact Us

You can reach the Khulnasoft Developer Platform team at _devinfo@khulnasoft.com_.

## License

The Khulnasoft Enterprise Software Development Kit for Python is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

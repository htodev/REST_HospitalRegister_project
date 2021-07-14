REST_HospitalRegister Cucumber

========================================================================

**REST_HospitalRegister Cucumber** provides automated testing of REST_HospitalRegister apps.


Meta
-----

Author:

    `Hristo Todev`

========================================================================

How to deploy REST_HospitalRegister Cucumber on your local machine
------------------------------------------------------------------------

::

    * get the code from remote repo https://github.com/htodev/REST_HospitalRegister_project

    * fetch the code to your workspace

========================================================================

Prerequisites
------------------------------------------------------------------------

::
    yarn package manager

========================================================================

How to install yarn and package requirements - https://yarnpkg.com/lang/en/docs/install/#debian-stable
------------------------------------------------------------------------

::

    $ (for  Linux)
    
    $ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -

    $ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list deb https://dl.yarnpkg.com/debian/ stable main

        * This will install and configure Yarn via Yarn Debian package repository.

    $ sudo apt-get update && sudo apt-get install yarn.

        * Update Yarn  and install  package requirements.
     
    $ (for Windows)
        * npm install -g yarn
        
    $ yarn install
        * Tha command above will install node_modules

========================================================================

How to create features and step_definitions
------------------------------------------------------------------------

::

    1. features:

        * they are needed to create a collection of scenarios, which describes a specific behaviour of a backend or
    frontend application.

        * example: Scenario: Scenario 1
                      Given: preconditions
                      When: actions
                      Then: results

                   Scenario: Scenario 2
                        ...

    2. step_definitions:

        * we have to write expressions in step_definitions to put some logic into javascript code according to expected
    behavior of the application we are testing.


========================================================================

How to run drf tests
------------------------------------------------------------------------

::

    1. run backend server

    2. $ yarn cucumber-drf

        * The purpose is to execute an automated test, which will notify us whether our backends apps work correctly or
    not. If expression matches a given scenario, perform the logic and if there is no errors, the test is passed, else it is
    failed.
------------------------------------------------------------------------
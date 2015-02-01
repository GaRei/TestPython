Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

  Scenario: run
     Given get request
     When verify status ok
     Then verify lastUpdated is not empty
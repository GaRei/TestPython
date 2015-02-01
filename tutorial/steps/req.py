import json
import requests
from behave import when, given, then

@given('get request')
def step_impl(context):
    context.response = requests.get("http://countdown.tfl.gov.uk/stopBoard/58984")

@when('verify status ok')
def step_impl(context):
    assert context.response.status_code is 200

@then('verify lastUpdated is not empty')
def step_impl(context):
    binary = context.response.content
    output = json.loads(binary)
    assert output['lastUpdated'] is not None
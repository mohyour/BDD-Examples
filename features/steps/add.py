# flake8: noqa F811
from behave import given, when, then
from script import add

@given(u'I want to add two numbers with the add function')
def step_impl(context):
    print(u'Step: Given Add function is run')


@when(u'I pass in "{a}" and "{b}" to the function')
def step_impl(context, a, b):
    context.result = add(a, b)


@then(u'I should get "{output}"')
def step_impl(context, output):
    assert context.result == int(output)

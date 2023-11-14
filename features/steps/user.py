# flake8: noqa: F811
import json
from behave import given, when, then

@given(u'a background to implement before every scenario')
def step_impl(context):
    assert context.client

@given(u'a user is to be added')
def step_impl(context):
    assert context.client


@when(u'I send a request with their id and name')
def step_impl(context):
    context.ID = "3"
    context.name = "Jill"
    req = {"id": context.ID, "name": context.name}
    context.response = context.client.post("/user", json=req,
                                           content_type="application/json")


@then(u'they are added as a user')
def step_impl(context):
    assert context.response
    assert context.response.status_code == 200
    resp = json.loads(context.response.get_data(as_text=True))
    assert resp["id"] == context.ID
    assert resp["user"] == context.name


@given(u'users exist in the app')
def step_impl(context):
    assert context.client


@when(u'the details of all users is requested in the application')
def step_impl(context):
    context.response = context.client.get("/users")


@then(u'it should have the details with their id and names')
def step_impl(context):
    assert context.response.status_code == 200
    resp = json.loads(context.response.get_data(as_text=True))
    assert len(resp) == 4


@when(u'the details of a user is requested')
def step_impl(context):
    id = context.user1["id"]
    context.response = context.client.get(f"/user/{id}")


@then(u'it should respond with the detail of the user')
def step_impl(context):
    assert context.response.status_code == 200
    resp = json.loads(context.response.get_data(as_text=True))
    assert resp["id"] == context.user1["id"]
    assert resp["name"] == context.user1["name"]

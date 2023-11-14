# flake8: noqa: F811
from behave import given, when, then
from script import EmployeeSystem


@given(u'new employees are hired by the company')
def step_impl(context):
    context.emp = EmployeeSystem()


@when(u'I register their details with "{}", "{}" and "{}"')
def step_impl(context, ID, name, dept):
    context.ID = ID
    context.emp.add_employee(ID, name, dept)


@then(u'the employee should be created with details "{}", "{}", "{}"')
def step_impl(context, ID, name, department):
    employee = context.emp.get_employee(ID)
    assert employee["id"] == ID
    assert employee["name"] == name
    assert employee["department"] == department


@then(u'if employee already exist with the same ID')
def step_impl(context):
    try:
        context.emp.add_employee(context.ID, "Lucas", "IT")
    except Exception as e:
        context.exception = e


@then(u'it should fail to register the new employee')
def step_impl(context):
    assert context.exception is not None
    assert "Employee with id already exist" in str(context.exception)


@given(u'employees already exist in the system')
def step_impl(context):
    context.emp = EmployeeSystem()
    context.emp.add_employee("1", "Sharon", "Product")
    context.emp.add_employee("2", "Boyle", "HR")
    context.emp.add_employee("3", "Musa", "Data")


@when(u'I query all employees')
def step_impl(context):
    context.all_employees = context.emp.get_all_employees()


@then(u'I have the total number of registered employees')
def step_impl(context):
    all_employees = context.all_employees
    assert len(all_employees) == 3
    assert all_employees["1"]["name"] == "Sharon"
    assert all_employees["2"]["department"] == "HR"


@when(u'I input an id of "{id}"')
def step_impl(context, id):
    context.emp_id = id


@then(u'employee should be returned with id "{id}" and name "{name}"')
def step_impl(context, id, name):
    employee = context.emp.get_employee(context.emp_id)
    assert employee["id"] == id
    assert employee["name"] == name


@given(u'I want to update employee\'s details')
def step_impl(context):
    pass


@when(u'I input their ID "{id}" and new department "{dept}"')
def step_impl(context, id, dept):
    update_data = {
        "department": dept
    }
    context.ID = id
    context.employee = context.emp.update_employee(id, update_data)


@then(u'employee details should be updated with new "{dept}"')
def step_impl(context, dept):
    employee = context.employee
    assert employee["id"] == context.ID
    assert employee["department"] == dept


@given(u'employee no longer works with the company')
def step_impl(context):
    context.emp = EmployeeSystem()


@given(u'I want to delete employee\'s details')
def step_impl(context):
    context.emp.add_employee("1", "Joy", "Operation")
    context.emp.add_employee("2", "Sean", "Customer Service")


@when(u'I input their id to delete')
def step_impl(context):
    context.emp_ID = "1"


@then(u'employee details should be removed from the system')
def step_impl(context):
    context.emp.delete_employee(context.emp_ID)
    employee = context.emp.get_employee(context.emp_ID)
    assert employee is None


@then(u'should fail if employee does not exist')
def step_impl(context):
    try:
        context.emp.delete_employee("10")
        context.exception = None
    except Exception as e:
        exception = e
    assert exception is not None
    assert "delete: Employee not found" in str(context.exception)

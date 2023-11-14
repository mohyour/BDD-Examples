def add(a, b):
    return int(a) + int(b)


class EmployeeSystem:

    def __init__(self):
        self.__employees = {}

    def add_employee(self, id, name, department):
        emp_id = self.__employees.get(id)
        if emp_id:
            raise Exception("Employee with id already exist, update if needed")
        employee = dict(id=id, name=name, department=department)
        self.__employees[id] = employee

    def update_employee(self, id, details):
        employee = self.__employees.get(id)
        if not employee:
            raise Exception("Cannot update: Employee not found")
        new_name = details.get("name")
        new_dept = details.get("department")
        if new_name:
            employee["name"] = new_name
        if new_dept:
            employee["department"] = new_dept
        return employee

    def get_employee(self, id):
        return self.__employees.get(id)

    def delete_employee(self, id):
        if id in self.__employees:
            del self.__employees[id]
            return
        raise Exception("Cannot delete: Employee not found")

    def get_all_employees(self):
        return self.__employees

    def delete_all_employees(self):
        self.__employees.clear()

    def __str__(self):
        return f"{self.id}, {self.name}, {self.department}"


a = EmployeeSystem()
d = EmployeeSystem()
a.add_employee(1, "hello", "hr")
c = a.get_employee(1)
print(c["name"], c["id"])
print(a.update_employee(1, {"name": "wohefa", "department": "it"}))
a.add_employee(2, "sharon", "hr")
print(a.get_all_employees())
print(d.get_all_employees(), "==")
print(d.get_employee(1), "haa ==")

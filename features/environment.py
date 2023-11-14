from app import app


# Executes prior everything
def before_all(context):
    print("This runs before all features")


# Executes prior every feature.
def before_feature(context, feature):
    context.client = app.test_client()
    context.user1 = {"id": "1", "name": "Plum"}
    context.user2 = {"id": "2", "name": "John"}
    users = [context.user1, context.user2]
    for user in users:
        context.client.post("/user", json=user,
                            content_type="application/json")


# Executes prior every tag
def before_tag(context, tag):
    if tag == "users":
        context.user4 = {"id": "4", "name": "Lilly"}
        context.client.post("/user", json=context.user4,
                            content_type="application/json")


# Executes prior every scenario.
def before_scenario(context, scenario):
    pass


# Executes post every scenario
def after_scenario(context, scenario):
    pass


# Executes post every feature
def after_feature(context, feature):
    pass


# Executes prior every step
def before_step(context, step):
    pass


# Executes post every step
def after_step(context, step):
    pass


# Executes post every tag
def after_tag(context, tag):
    pass


# Executes post everything
def after_all(context):
    pass

from invoke import task

@task
def hello(c):
    print("Hello world!")

@task
def greet(c, name):
    c.run(f"echo {name}加油!")
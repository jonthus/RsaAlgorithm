from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 ui/gui.py")

@task
def test(ctx):
    ctx.run("pytest .")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest .")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

from rfctl.awslocal import lambda_command
from rfctl.build import do_build
import click
import os


@click.command()
@click.pass_context
def create_command(ctx: click.Context):
    funcdef = ctx.obj["funcdef"]
    out = os.path.join(ctx.obj["working_dir"], "lambda.zip")
    if not do_build(ctx, out):
        return
    click.echo("Creating function %s/%s" % (funcdef["metadata"]["namespace"], funcdef["metadata"]["name"]))
    environment = []
    environment_spec:dict = funcdef["spec"].get("environment",{})
    for env,value in environment_spec.items():
        environment.append("{}={}".format(env,value))
    lambda_args = ["create-function",
                   "--function-name", funcdef["metadata"]["name"],
                   "--handler", funcdef["spec"]["handler"],
                   "--zip-file", "fileb://{}".format(out),
                   "--runtime", funcdef["spec"]["runtime"],
                   "--timeout", funcdef["spec"]["timeout"]]
    if environment:
        lambda_args.extend(["--environment", '''Variables={%s}''' % ",".join(environment)])
    lambda_command(ctx.obj["endpoint"], lambda_args)
    concurrency = funcdef["spec"].get("concurrency",1)
    lambda_args = ["put-function-concurrency",
                   "--function-name", funcdef["metadata"]["name"],
                   "--reserved-concurrent-executions", concurrency]
    lambda_command(ctx.obj["endpoint"], lambda_args)
    os.remove(out)

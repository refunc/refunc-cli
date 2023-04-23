import click


@click.command()
@click.pass_context
def update_code_command(ctx: click.Context):
    funcdef = ctx.obj["funcdef"]
    click.echo("Updating code for function %s/%s" % (funcdef["metadata"]["namespace"], funcdef["metadata"]["name"]))

import click


@click.command()
@click.pass_context
def update_config_command(ctx: click.Context):
    funcdef = ctx.obj["funcdef"]
    click.echo("Updating config for function %s/%s" % (funcdef["metadata"]["namespace"], funcdef["metadata"]["name"]))

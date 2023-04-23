import click


@click.command()
@click.pass_context
def create_url_command(ctx: click.Context):
    funcdef = ctx.obj["funcdef"]
    click.echo("Creating url for function %s/%s" % (funcdef["metadata"]["namespace"], funcdef["metadata"]["name"]))

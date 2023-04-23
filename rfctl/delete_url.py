import click


@click.command()
@click.pass_context
def delete_url_command(ctx: click.Context):
    funcdef = ctx.obj["funcdef"]
    click.echo("Deleting url for function %s/%s" % (funcdef["metadata"]["namespace"], funcdef["metadata"]["name"]))

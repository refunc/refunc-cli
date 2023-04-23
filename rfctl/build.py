from aws_lambda_builders.builder import LambdaBuilder
from aws_lambda_builders.architecture import X86_64
import traceback
import tempfile
import click
import os


def get_dependency_manager(lang: str):
    if "python" in lang:
        return "pip"
    if "go" in lang:
        return "modules"
    raise Exception("not support language %s" % lang)


def get_runtime(runtime: str):
    if "golang" in runtime:
        return runtime.replace("golang", "go")
    return runtime


@click.command()
@click.pass_context
def build_command(ctx: click.Context):
    funcdef = ctx.obj["funcdef"]
    click.echo("Building function %s/%s" % (funcdef["metadata"]["namespace"], funcdef["metadata"]["name"]))
    build = funcdef["spec"]["build"]
    capabilities = {
        "language": build["language"],
        "dependency_manager": get_dependency_manager(build["language"])
    }
    with tempfile.TemporaryDirectory() as scratch_dir:
        click.echo("Building in temporary directory %s" % scratch_dir)
        try:
            params = {
                "source_dir": build["source"],
                "artifacts_dir": os.path.join(os.getcwd(), "dist"),
                "scratch_dir": scratch_dir,
                "manifest_path": os.path.join(build["source"], build["manifest"]),
                "architecture": build["architecture"],
                "runtime": get_runtime(funcdef["spec"]["runtime"]),
                "optimizations": {},
                "options": {
                    "artifact_executable_name": funcdef["spec"]["entry"],
                }
            }
            builder = LambdaBuilder(
                language=capabilities["language"],
                dependency_manager=capabilities["dependency_manager"],
                application_framework=None,
            )
            builder.build(
                params["source_dir"],
                params["artifacts_dir"],
                params["scratch_dir"],
                params["manifest_path"],
                executable_search_paths=params.get("executable_search_paths", None),
                runtime=params["runtime"],
                optimizations=params["optimizations"],
                options=params["options"],
                mode=params.get("mode", None),
                download_dependencies=params.get("download_dependencies", True),
                dependencies_dir=params.get("dependencies_dir", None),
                combine_dependencies=params.get("combine_dependencies", True),
                architecture=params.get("architecture", X86_64),
                is_building_layer=params.get("is_building_layer", False),
                experimental_flags=params.get("experimental_flags", []),
                build_in_source=params.get("build_in_source", None),
            )
        except Exception as ex:
            click.echo("Build error:\n %s" % traceback.format_exc())

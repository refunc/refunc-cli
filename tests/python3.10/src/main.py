import requests


def lambda_handler(event, ctx):
    ctx.log("this is log")
    return {
        "msg": "hello py3.10"
    }

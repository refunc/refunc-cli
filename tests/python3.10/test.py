from rfctl.client import LambdaClient

client = LambdaClient("dpool")

rsp = client.invoke_function("demo-py310", {}, get_log=True)

print(rsp)

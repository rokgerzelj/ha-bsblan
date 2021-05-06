import asyncio, aiohttp

from yarl import URL

class BSBLan:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.auth = aiohttp.BasicAuth(username, password)

    async def query_params(self, param_list):
        url = URL.build(scheme="http", host=self.host, port=self.port, path="/JQ=" + ",".join([str(p) for p in param_list])).join(URL())
        headers = {
            "Accept": "application/json, */*",
        }

        async with aiohttp.ClientSession() as session:
            response = await session.get(
                url, auth=self.auth
            )
            #print(await response.json())
            return await response.json()

    # type = 1 => SET message
    # type = 0 => INF message (used for setting the actual measured room temp)
    async def set_param(self, param, value, type = 1):
        data = {
            "Parameter": str(param),
            "Value": str(value),
            "Type": str(type)
        }
        url = URL.build(scheme="http", host=self.host, port=self.port, path="/JS").join(URL())

        # TODO implement exception/returned value based on returned status
        async with aiohttp.ClientSession() as session:
            response = await session.post(
                url, auth=self.auth, json=data
            )
            #print(await response.json())
            return await response.json()

if __name__ == "__main__":

    bsblan = BSBLan("192.168.0.7", "80", "admin", "PASSWORD")

    loop = asyncio.get_event_loop()
    #loop.run_until_complete(bsblan.query_params([700, 701]))
    loop.run_until_complete(bsblan.set_param(710, 22))


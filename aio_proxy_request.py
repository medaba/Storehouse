# -*- coding: utf-8 -*-

# async request via proxy

import aiohttp
import asyncio
from aiohttp_proxy import ProxyConnector


async def fetch(proxy_ip, proxy_port, url="http://ip-api.com/json/"):
    connector = ProxyConnector(
        host=proxy_ip,
        port=proxy_port)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()

if __name__ == '__main__':
    pass
    # r = asyncio.run(fetch(url="http://ip-api.com/json/", proxy_ip='95.84.137.193', proxy_port='53281'))
    # print(r)

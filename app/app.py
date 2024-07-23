import asyncio
import aiohttp

from visualization import create_visualization
from db import write_to_db
from data import fetch_data
from flatten import flatten_input_data
from merge_sources import merge_source_dfs

CROWDSTRIKE_ENDPOINT = f"/api/crowdstrike/hosts/get"
QUALYS_ENDPOINT = f"/api/qualys/hosts/get"


async def main():
    async with aiohttp.ClientSession() as session:
        crowdstrike_data, qualys_data = await asyncio.gather(fetch_data(session, CROWDSTRIKE_ENDPOINT),
                                                             fetch_data(session, QUALYS_ENDPOINT))

    crowdstrike_df, qualys_df = await asyncio.gather(flatten_input_data(crowdstrike_data), flatten_input_data(qualys_data))

    merged_df = await merge_source_dfs(qualys_df=qualys_df, crowdstrike_df=crowdstrike_df)

    await asyncio.gather(write_to_db(merged_df), create_visualization(merged_df))


if __name__ == '__main__':
    asyncio.run(main())

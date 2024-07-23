import pandas as pd


async def merge_source_dfs(qualys_df: pd.DataFrame, crowdstrike_df: pd.DataFrame):
    qualys_df = qualys_df.rename(columns={"_id": "qualys_id", 'address': '_id'})
    crowdstrike_df = (crowdstrike_df.rename(columns={"_id": "crowdstrike_id", 'local_ip': '_id'})
                      .drop(columns=['bios_manufacturer', 'bios_version', 'connection_ip',
                                     'default_gateway_ip', 'device_id', 'external_ip',
                                     'hostname', 'instance_id', 'os_version', 'platform_name',
                                     'system_manufacturer', 'system_product_name']))

    return pd.merge(crowdstrike_df, qualys_df, on='_id', how='outer')
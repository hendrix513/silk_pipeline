import pandas as pd


async def flatten_data(json_obj):
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    out = {}
    flatten(json_obj)
    return out


async def flatten_input_data(input_data: list[dict]):
    return pd.DataFrame([await flatten_data(input_data_obj) for input_data_obj in input_data])


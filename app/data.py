import os

URL = "https://api.recruiting.app.silk.security"
API_KEY = os.getenv('API_KEY')

async def fetch_data(session, endpoint):
    skip = 0
    data_list = []
    while True:
        async with session.post(f"{URL}{endpoint}", params={"skip": skip}, headers={"token": API_KEY}) as response:
            if response.status == 500:
                break
            data = await response.json()
            data_list.extend(data)  # Assuming the data is a list of records
            skip += 1
    return data_list
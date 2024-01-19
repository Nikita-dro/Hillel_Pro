import asyncio
import httpx


async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        keys = list(data.keys())
        values = list(data.values())
        print(f"--------\nData fetched from {url}: {data}")
        print(f"Keys - {keys}")
        print(f"Values - {values}")
        return keys, values


async def process_data(keys, values):
    upper_keys = [key.upper() for key in keys]
    str_values = [str(value) for value in values]
    print(f"--------\nProcessed data:\nUpper keys - {upper_keys}\nString values - {str_values}")


async def analyze_data(keys, values):
    count_keys = len(keys)
    dict_types = {}
    for value in values:
        value_type = str(type(value))
        if value_type in dict_types:
            dict_types[value_type] += 1
        else:
            dict_types[value_type] = 1
    print(f"--------\nNumber of keys: {count_keys}")
    print(f"Types of values: {dict_types}")


async def save_data(keys, values):
    with open("saved_data.txt", "w") as file:
        keys_str = ', '.join(map(str, keys))
        values_str = ', '.join(map(str, values))
        file.write(f"Keys: {keys_str}\nValues: {values_str}")
    print("--------\nData saved to saved_data.txt")


async def cleanup_lists(keys, values):
    keys.clear()
    values.clear()
    print(f"--------\nCleaning up resources\nEmpty list of keys - {keys}\nEmpty list of values - {values}")


async def main():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    data = await fetch_data(url)

    tasks = [
        process_data(data[0], data[1]),
        analyze_data(data[0], data[1]),
        save_data(data[0], data[1]),
        cleanup_lists(data[0], data[1])
    ]

    await asyncio.gather(*tasks)

    print("--------\nMain coroutine is done, stopping event loop")
    asyncio.get_event_loop().stop()


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

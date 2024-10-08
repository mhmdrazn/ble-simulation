import asyncio
from bleak import BleakClient
import sys

uuid_first_name = "00002a8a-0000-1000-8000-00805f9b34fb"
uuid_last_name = "00002a90-0000-1000-8000-00805f9b34fb"
uuid_gender = "00002a8c-0000-1000-8000-00805f9b34fb"

async def get_services(mac):
    async with BleakClient(mac) as client:

        await client.write_gatt_char(uuid_first_name, "ITS".encode())
        await client.write_gatt_char(uuid_last_name, "Surabaya".encode())
        
        first_name = await client.read_gatt_char(uuid_first_name)
        print("First name: " + first_name.decode("utf-8"))
        last_name = await client.read_gatt_char(uuid_last_name)
        print("Last name: " + last_name.decode("utf-8"))
        gender = await client.read_gatt_char(uuid_gender)
        print("Gender: " + gender.decode("utf-8"))

        await client.disconnect()

try:
    asyncio.run(get_services("40:8E:F6:58:08:56"))
except KeyboardInterrupt:
    print("User stopped the program")
    sys.exit(0)



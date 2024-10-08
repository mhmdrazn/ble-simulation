import asyncio
from bleak import BleakClient
import sys

uuid_first_name = "00002a8a-0000-1000-8000-00805f9b34fb"
uuid_last_name = "00002a90-0000-1000-8000-00805f9b34fb"
uuid_gender = "00002a8c-0000-1000-8000-00805f9b34fb"

async def get_services(mac):
    async with BleakClient(mac) as client:
        print(f"Connected: {client.is_connected}")

        svcs = await client.get_services()
        print("Services:", svcs)
        for service in svcs:
            print("Service: ")
            print(service)

            print("\nCharacteristics: ")
            for char in service.characteristics:
                print(char)
                print("\nProperties:")
                print(char.properties)

        await client.disconnect()

try:
    asyncio.run(get_services("40:8E:F6:58:08:56"))
except KeyboardInterrupt:
    print("User stopped the program")
    sys.exit(0)



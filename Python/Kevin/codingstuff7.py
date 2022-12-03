## Drone Library!
from Mambo import Mambo

## This stores the MAC address as a variable
mamboAddress = "e0:14:0a:ad:3d:d0"

## Thhis creates an instance of a Mambo
mamboDrone = Mambo(mamboAddress, use_wifi=False)

## This connects to the drone
print("Trying to connect...")
success=mambo.connect(num_retries=3)
print("connected: %s" % success)

## If we are connected, Let's take off!
if(success):
    print("get status info")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("Take off!")
    mambo.safe_takeoff(5)


    print("Land!!!")
    mambo.safe_land(5)

    print("disconnect from Mambo.")
    mambo.disconnect()

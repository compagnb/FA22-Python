## Drone Library
from Mambo import Mambo
mamboAddress= "e0:14:0a:ad:3d:d0"
mambo = Mambo(mamboAddress, use_wifi=False)

## conect to the drone
print("trying to connect...")
success=mambo.connect(num_retries=3)
print("connected: %s" %success)

## if we are connected I wanna Take off!!
if (success):
    print("get status info")
    mambo.smart_sleep(2)
    mambo.ask_for_status_update()
    mambo.smart_sleep(2)

    print("Take off!")
    mambo.safe_takeoff(5)

    print("Land!!!")
    mambo.safe_land(5)

    Print("disconnect from mambo.")
    mambo.disconnect()
    

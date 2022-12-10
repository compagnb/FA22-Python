## drone library
##imports the Mambo class from the library
from Mambo import Mambo

##stores the MAC address as a variable
mamboAddress="e0:14:0a:ad:3d:d0"

##creates an instance of an object Mambo
mambo = Mambo(mamboAdddress, use_wifi=False)

## connect to the drone
print("trying to connect...")
success=mambo.connect(num_retries=3)
print("connected: %s" % success)

## if we are connected I wanna take off!!!
if(success):
    print("get status info")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("Take Off!")
    mambo.safe_takeoff(5)

    print("land!!!")
    mambo.safe_land(5)

    print("disconnect from mambo.")
    mambo.disconnect()
          
          


from Mambo import Mambo
mamboAddress= "e0:14:0a:ad:3d:d0"
mambo = Mambo(mamboAddress, use_wifi=False)
print("trying to connect..")
success+ mambo.connect(num_retries=3)
print("connected: %s" % success
if(success):
      print("get status info")
      mambo.smart_sleep(2)
      mambo.ask_for_state_update()
      mambo.smart_sleep(2)

      print("Take Off!")
      mambo.safe_takeoff(5)
      mambo.fly_direct(roll=50, pitch=50,yaw=50,vertical_movement=50, duration=3)
      print("Land!!!")
      mambo.safe_land(5)

      print ("disconnect from Mambo.")
      mambo.disconnect()

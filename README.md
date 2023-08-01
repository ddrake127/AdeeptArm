# AdeeptArm

I purchased [this](https://www.amazon.com/gp/product/B09SG8TLQ1/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1) with the intent of doing some image recognition things with it.  Unfortunately, a lot of the packages the default drivers depend on have changed since they were written and Adeept had not yet updated their sample code, so I re-wrote it.  Figured I would put it out there in case somebody else ends up in the same boat.

If you're looking for batteries, try [these](https://www.amazon.com/gp/product/B0B145KQGY/).

## Installing and Running
### Install Adafruit Servokit
Run `sudo pip3 install adafruit-circuitpython-servokit`
### Download and Install Code
Download both files and put them on your pi in the home directory (`/home/pi`).
### Enable the I2C Interface
1.  From the terminal, run `sudo raspi-config`
2.  Select "Interfacing Options" > "I2C"
3.  Select "Yes" when prompted `Would you like the ARM I2C interface to be enabled?`
### Running the Program
`sudo python3 adeept_arm.py`
### Configure Auto-Run on Boot
1.  `sudo nano /etc/rc.local`
2.  Add `sudo bash -c 'python3 /home/pi/adeept_arm.py` at the bottom.
3.  `Ctrl+x`, `y`, `Enter` to save.
4.  Reboot

## Controls
### Left Stick
- Left-Right turns the whole claw
- Up-Down moves the whole arm up-down
- Click does nothing (see fun thing for what happens if you click both)
### Right Stick
- Left opens claw
- Right closes claw
- Up/Down moves the second joint up/down
- Click does nothing (see fun thing for what happens if you click both)

## Fun Thing I Added
If you click both joysticks at the same time, it positions itself so you can place something on the top of the claw.  You have to wait 4 seconds (can be changed) and then you can click both sticks again and it will throw whatever you placed up there.  Has to be something light....like a ping pong ball, but it will chuck it a good little ways.

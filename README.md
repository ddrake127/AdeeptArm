# AdeeptArm

I purchased [this](https://www.amazon.com/gp/product/B09SG8TLQ1/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1) with the intent of doing some image recognition things with it.  Unfortunately, a lot of the packages the default drivers depend on have changed since they were written and Adeept had not yet updated their sample code, so I re-wrote it.  Figured I would put it out there in case somebody else ends up in the same boat.

## Installing and Running (more detailed instructions coming soon)
Download both files and put them on your pi.  Run it with `sudo python3 adeept_arm.py`.  You will need to install some Adafruit packages -- it will tell you what its missing (I will document the installation process in detail at a later point in time).  I went ahead and threw `sudo bash -c 'python3 /home/pi/adeept_arm.py' &` in my `/etc/rc.local` so it runs on boot.

## Fun things
If you click both joysticks at the same time, it positions itself so you can place something on the top of the claw.  You have to wait 4 seconds (can be changed) and then you can click both sticks again and it will throw whatever you placed up there.  Has to be something light....like a ping pong ball, but it will chuck it a good little ways.

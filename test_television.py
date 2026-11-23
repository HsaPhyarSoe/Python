import pytest
import television

def test_init():
    tv = television.Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = television.Television()
    tv.power()          #on
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()          #off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    tv = television.Television()
    tv.power()
    tv.volume_up()
    tv.mute()           #on, up, mute
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()           #on, unmute
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.power()
    tv.mute()           #off, mute
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"
    tv.mute()           #off, unmuted
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

def test_channel_up():
    tv = television.Television()
    tv.channel_up()     #off, up
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()     #on, up
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()     #on, pass max
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    tv = television.Television()
    tv.channel_down()   #off, down
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_down()   #on, pass min
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up():
    tv = television.Television()
    tv.volume_up()      #off, up
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()      #on, up
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()           #on, mute, up
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()      #on, pass max
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv = television.Television()
    tv.volume_down()    #off, down
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()    #on, max volume, down
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_down()    #on, mute, down
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()    #on, pass max
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
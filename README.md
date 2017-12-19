# piduino-sensor


### project idea
Project for passing data from a sensor connected to a microcontroller to a Raspberry Pi, which sends it to a (remote or local) api.

Sensor -> microcontroller -> RasPi -> api -> sqlite database

### Folder Structure:
- api: the api based on flask, which saves teh data to a sqlite db and provides it to api users

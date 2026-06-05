# rp-pico-w-temperature-monitor

A home IoT project for temperature and humidity monitoring using a Raspberry Pi Pico W and a DHT11 sensor.

The device periodically reads temperature and humidity values from the sensor and sends the measurements as JSON data to a remote HTTP server over Wi-Fi.

## Hardware

- Raspberry Pi Pico W
- DHT11 temperature and humidity sensor

## Features

- Wi-Fi connectivity
- Periodic temperature measurement
- Periodic humidity measurement
- JSON serialization
- HTTP communication with backend server
- Lightweight embedded implementation

## Architecture

```text
DHT11 Sensor
      │
      ▼
Raspberry Pi Pico W
      │
      │ HTTP POST (JSON)
      ▼
pico-weather-server
```

## Example Payload

```json
{
  "temperature": "23.5",
  "humidity": "55",
  "room": "living-room"
}
```

## Related Project

The backend server implementation can be found here:

- https://github.com/DaliborLis/pico-weather-server

## Project Goals

This project was created as a learning exercise for:

- Embedded development
- Raspberry Pi Pico W
- IoT communication
- Sensor integration
- HTTP networking
- JSON data exchange
- Backend integration

## Hardware Setup

![pico-photo](https://github.com/user-attachments/assets/e08248e3-c5d0-4020-9504-fa717b5cf4f2)

from . import consumers

channel_routing = {
    'websocket.connect': consumers.ws_connect,
    'websocket.receive': consumers.ws_message,
    'websocket.disconnect': consumers.ws_disconnect,
}

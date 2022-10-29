# Simple Websocket Python UDP
a server that receives multiple clients in parallel, and then send them back their ip+port 
it first establishes connection (handshake type), then continuesly broadcast messages from server

## Usage
- Real time currency price, after a client sends currency name request


## To run
```
py server.py
```

### packages
```python
import asyncio
import datetime
import random
import websockets
```
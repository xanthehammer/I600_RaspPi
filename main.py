import socket
from machine import Pin

led_red = Pin(5, Pin.OUT)
led_green = Pin(4, Pin.OUT)
led_blue = Pin(0, Pin.OUT)

CONTENT = """\
HTTP/1.0 200 OK
Content-Type: text/html

<html>
	<head>
	</head>
	<body>
		<p>Hello #%d from MicroPython!</p>
		<a href="/toggle_red">Turn on Red LED</a>
		<a href="/toggle_green">Turn on Green LED</a>
		<a href="/toggle_blue">Turn on Blue LED</a>
	</body>
</html>
"""

def main():
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://<this_host>:8080/")

    counter = 0
    while True:
        sock, addr = s.accept()
        print("Client address:", addr)
        stream = sock.makefile("rwb")
        req = stream.readline().decode("ascii")
        method, path, protocol = req.split(" ")
        print("Got", method, "request for", path)

        if path == "/toggle_red":
            led_pin.value(1-led_red.value())
	elif path == "/toggle_green":
	    led_pin.value(1-led_green.value())
	elif path == "/toggle_blue":
	    led_pin.value(1-led_blue.value())

        while True:
            h = stream.readline().decode("ascii").strip()
            if h == "":
                break
            print("Got HTTP header:", h)
        stream.write((CONTENT % counter).encode("ascii"))
        stream.close()
        sock.close()
        counter += 1
        print()

main() # Press Ctrl-C to stop web server

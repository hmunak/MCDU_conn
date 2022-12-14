#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# FlightDeckSolutions' HW MCDU unit to FlybyWire MCDU server connection
# simply recieve HW MCDU input and send it to MCDU server via WebSocket

import socket
from websocket import create_connection
import sys

MCDU_comm2 = {
"1":"event:DOT",
"2":"event:0",
"3":"event:PLUSMINUS",
"4":"event:Z",
"5":"event:DIV",
"6":"event:SP",
"7":"event:OVFY",
"8":"event:CLR",
"9":"event:7",
"10":"event:8",
"11":"event:9",
"12":"event:U",
"13":"event:V",
"14":"event:W",
"15":"event:X",
"16":"event:Y",
"17":"event:4",
"18":"event:5",
"19":"event:6",
"20":"event:P",
"21":"event:Q",
"22":"event:R",
"23":"event:S",
"24":"event:T",
"25":"event:1",
"26":"event:2",
"27":"event:3",
"28":"event:K",
"29":"event:L",
"30":"event:M",
"31":"event:N",
"32":"event:O",
"33":"event:PREVPAGE",
"34":"event:UP",
"35":"event:L1",
"36":"event:F",
"37":"event:G",
"38":"event:H",
"39":"event:I",
"40":"event:J",
"41":"event:AIRPORT",
"43":"event:L2",
"44":"event:A",
"45":"event:B",
"46":"event:C",
"47":"event:D",
"48":"event:E",
"49":"event:FPLN",
"50":"event:RAD",
"51":"event:L3",
"52":"event:FUEL",
"53":"event:SEC",
"54":"event:ATC",
"55":"event:MENU",
"56":"event:L5",
"57":"event:DIR",
"58":"event:PROG",
"59":"event:L4",
"60":"event:PERF",
"61":"event:INIT",
"62":"event:DATA",
"65":"event:R1",
"66":"event:R2",
"67":"event:R3",
"68":"event:R4",
"69":"event:R5",
"70":"event:R6",
"71":"event:L6",
"73":"event:NEXTPAGE",
"74":"event:DOWN",
}

class BaseClient:
    def __init__(self, timeout:int=10, buffer:int=1024):
        self.__socket = None
        self.__websocekt = None
        self.__address = None
        self.__timeout = timeout
        self.__buffer = buffer

    def connect(self, address, family:int, typ:int, proto:int):
        self.__address = address
        self.__socket = socket.socket(family, typ, proto)
        #self.__websocekt = create_connection("ws://192.168.11.91:8380/")
        self.__socket.settimeout(self.__timeout)
        self.__socket.connect(self.__address)

    def send(self, message:str="") -> None:
        flag = False
        while True:
            try:
                message_recv = self.__socket.recv(self.__buffer).decode('utf-8')
                self.received(message_recv)
                if flag:
                    break
            except KeyboardInterrupt:
                print(" Caught CTRL+C")
                self.__socket.shutdown(socket.SHUT_RDWR)
                self.__socket.close()
                sys.exit(0)
        try:
            self.__socket.shutdown(socket.SHUT_RDWR)
            self.__socket.close()
        except:
            pass

    def received(self, message:str):
        #print(message)
        if(message.split(':')[-1].strip()) == "ON":
            key_id = message.rsplit(':')[-2]
            if( key_id in MCDU_comm2):
                key_server = MCDU_comm2[key_id]
                print(key_server)
                #self.__websocekt.send(str(key_server))

class InetClient(BaseClient):
    def __init__(self, host:str="192.168.11.92", port:int=10346) -> None:
        self.server=(host,port)
        super().__init__(timeout=6000, buffer=1024)
        super().connect(self.server, socket.AF_INET, socket.SOCK_STREAM, 0)


def signal_handler(signal, frame):
        # close the socket here
        self.__socket.shutdown(socket.SHUT_RDWR)
        self.__socket.close()
        sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)


if __name__=="__main__":
    cli = InetClient()
    cli.send()

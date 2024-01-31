#!/bin/bash
ip=/home/art/shard/ip.txt
sleep 5
xpra attach ws://$(cat $ip):9009

#!/bin/bash

s/\n+printf\(/pprint\(/g
s/ +printf\(/pprint\(/g
s/\t+printf\(/pprint\(/g

s/\n+printf\t+\(/pprint\(/g
s/ +printf\t+\(/pprint\(/g
s/\t+printf\t+\(/pprint\(/g

s/\n+printf\n+\(/pprint\(/g
s/ +printf\n+\(/pprint\(/g
s/\t+printf\n+\(/pprint\(/g

s/\n+printf +\(/pprint\(/g
s/ +printf +\(/pprint\(/g
s/\t+printf +\(/pprint\(/g


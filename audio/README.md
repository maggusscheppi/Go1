### How to let the dog bark

Copy bark.sh on the raspberri (192.168.12.1) and +x chmod it<br>
Copy go1_bark.sh and bark.wav to the nano (192.168.123.13) and +x chmod it<br>
Make rasp and nano friendly with each other by copying an rsa_pub key from the raspberri to the nano .ssh/authorized_keys<br>
From this u can call .bark.sh on the raspberri to let the nano play bark.wav

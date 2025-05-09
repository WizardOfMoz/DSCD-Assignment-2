pkill -f "server\.py [0-9]"
pkill -f "regserver\.py"

python restart.py

N=3
Nw=2
Nf=2

python regserver.py $N $Nw $Nf &
sleep 1

for i in `seq 1 $N`; do
    python server.py $i &
    sleep 1
done

python client.py<input.txt

wait
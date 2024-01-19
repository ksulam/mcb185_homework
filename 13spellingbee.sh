cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep '^[zoniacr]*$' | grep r | grep -E ....+ 

echo "WORD COUNT:" 
gunzip -c dictionary.gz | grep '^[zoniacr]*$' | grep r | grep -E ....+ | wc -l 
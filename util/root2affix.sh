for r in $(grep -F '[verb' roots.txt | sed 's/).*//' | sed 's/.* (//' | uniq); do
       	a=$(grep -F "($r)" roots.txt | egrep ' _[a-z]|[a-z]_ ' | sed "s/.*) //" | sed 's/ .*//' | sed 's/_//g')
       	echo $r $a
done

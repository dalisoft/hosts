touch hosts-tmp

cat dalisoft-hosts >> hosts-tmp
curl https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts >> hosts-tmp
curl https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt >> hosts-tmp

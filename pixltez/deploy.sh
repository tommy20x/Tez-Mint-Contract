echo 'Build...'
./build.sh

echo 'Deploy PiXLTez Contract...'
./deploy-pixltez.sh

echo 'Deploy PiXLCoin Contract...'
./deploy-pixlcoin.sh

echo 'Deploy PiXLGame Contract...'
./deploy-pixlgame.sh
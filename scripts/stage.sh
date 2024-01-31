#!/bin/bash
SCRIPT_DIR=$(dirname $(readlink -f $0))

pip3 install \
        torch \
        scipy \
        unidecode \
        phonemizer \
        inflect \
        typing \
        flask \
        openai

rm -rf $SCRIPT_DIR/../build
mkdir -p $SCRIPT_DIR/../build
git clone -b me https://github.com/psiphon/glados-tts.git $SCRIPT_DIR/../build/glados-tts
mkdir -p $SCRIPT_DIR/../build/glados-tts/audio
mkdir -p $SCRIPT_DIR/../build/glados-tts/tmp

mkdir -p $SCRIPT_DIR/../build/sarcan
cp -a $SCRIPT_DIR/../src $SCRIPT_DIR/../build/sarcan
cp -a $SCRIPT_DIR/../config $SCRIPT_DIR/../build/sarcan
cp -a $SCRIPT_DIR/../audio $SCRIPT_DIR/../build/sarcan
mkdir -p $SCRIPT_DIR/../build/sarcan/tmp
mkdir -p $SCRIPT_DIR/../build/sarcan/audio

echo "
#!/bin/bash
set -m 
cd glados-tts
python3 engine.py &
cd ..
cd sarcan
python3 src/main.py &
fg %1 
" > $SCRIPT_DIR/../build/start.sh
chmod +x $SCRIPT_DIR/../build/start.sh

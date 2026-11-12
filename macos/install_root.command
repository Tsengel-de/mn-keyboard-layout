#!/bin/sh
here="`dirname \"$0\"`"
echo "Changing dir to $here"
cd "$here"

echo "Copying files to /Library/Keyboard Layouts/"
sudo cp -rf ./Mongol* /Library/Keyboard\ Layouts/

echo "Finished"

echo "More information at: http://dusal.blogmn.net/99944/"
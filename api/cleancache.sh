#remove all __pycache__ directories in the current directory and all subdirectories

find . -name '__pycache__' -exec rm -rf {} +


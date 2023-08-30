# Text recognition dataset generation

Clone and install:
```
pip install .
```

Now choose a command to run from a file in `commands/` folder and run it like below:
```
trdg --output_dir ./outputs/bw -l fa -fd trdg/fonts/fa --dict trdg/dicts/fa.txt -t 48 -c 1000 -w 1 -bl 0 -rbl -m 3,3,3,3 -tc "#284854,#542828" -k 5 -rk -na 1 -ws -b 0
```
Now there should be 1000 images under `outputs/bw` folder.
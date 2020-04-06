# CSV Explorer
Tiny command line utility that provide simple way to explore csv files in command line. You can access pandas data 
exploration functions easily. 

## Installation
```bash
git clone https://github.com/tahtaciburak/csve
pip3 install -r requirements.txt
chmod +x csve.py 
cp csve.py /usr/bin/csve
```

## Usage

Head of the csv file:
```bash
csve head test.csv
```

Tail of the csv file:
```bash
csve tail test.csv
```

Describe the csv file:
```bash
csve describe test.csv
```

Info of the csv file:
```bash
csve describe test.csv
```
from os import listdir, linesep
from os.path import isfile, join

myPath = '/home/timoveldt/Development/tools/testdata/HAB';

scenarios = open(myPath + '/scenarios.txt', 'w');

listedFiles = listdir(myPath);
listedFiles.sort();

files = [f for f in listedFiles if (isfile(join(myPath,f)) and f.endswith('.png'))];

for file in files:
	scenarios.write(file + '\t0' +linesep);

scenarios.close();

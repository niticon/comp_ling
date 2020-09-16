import word2vec
import pathlib
import argparse

def loop_dir(directory):
	directory += '/'
	path = pathlib.Path(directory)
	for fl in path.iterdir():
		with open(fl, 'r') as f:
			print("Processing file\t" + fl)
			for byts in f:
				print(byts)
			f.close()
	return f

if __name__ == "__main__":
#file_directory=open(args.path, "r").read()
	file_directory=args.path
	loop_dir(file_directory)

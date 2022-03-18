# Import dependencies
from PIL import Image
import sys
import os

# Load VGA 256 color palette
pal = Image.open("colors.png").convert('RGB')
palette = pal.load()

# Create other variables
convertFile = ""
outputFile = "image.bin"
image = None
pixels = None

# Check input validity
if len(sys.argv) > 2:
	print("Too many arguments provided. Please supply one file to be converted.")
elif len(sys.argv) < 2:
	print("Argument not provided. Please supply one file to be converted.")
else:
	print("Checking input validity...")
	if str(sys.argv[1]).endswith(".png"):
		convertFile = str(sys.argv[1])
		try:
			print("Opening input file...")
			image = Image.open(convertFile).convert('RGB')
			pixels = image.load()
			if image.width > 320 or image.height > 200:
				print("Image is too big. Maximum image size is 320x200.")
				sys.exit(0)
			else:
				if os.path.getsize(sys.argv[1]) > 32000:
					print("File must be less than 32000 bytes in size.")
					sys.exit(0)
		except:
			print("Input file invalid or was not found.")
			sys.exit(0)
	else:
		print("Only PNG format files are accepted.")
		sys.exit(0)

# Create/open binary file
print("Creating export binary...")
binary = open(outputFile, "wb")

# Gather palette data
print("Gathering palette data...")
list = []
for y in range(pal.height):
	for x in range(pal.width):
		list.append(palette[x,y])

# Convert image to binary
binary.write(bytearray([image.width&0xFF,image.height&0xFF]))
data = []
for x in range(image.width):
	x = image.width - x - 1
	for y in range(image.height):
		y = image.height - y - 1
		difference = 0xFFFFFFFF
		choice = 0
		index = 0
		for c in list:
			dif = sum([(pixels[x,y][i] - c[i])**2 for i in range(3)])
			if dif < difference:
				difference = dif
				choice = index
			index += 1
		print("Converting pixels... | X: "+str(x)+" - Y:"+str(y))
		binary.write(bytearray([choice&0xFF]))
binary.close()
print('File successfully converted')
sys.exit(0)
from PIL import Image
#!/usr/local/bin/python3

# using globals! SO BAD! What's a better way?
# or is it ok in this case??
width  = 0
height = 0
maxval = 0

#Reads image file and store RGB values in a 2-d array
def readImage(filename):
	img = Image.open(filename, 'r')
	w, h = img.size
	pix = list(img.getdata())
	return [pix[n:n+w] for n in range(0, w*h, w)]

def multiply(pixel, kernel, i, j, height, width):
	R, G, B = 0, 0, 0
	if i<1 or j<1 or i>=height-1 or j>=width-1:
		R = pixel[i][j][0]
		G = pixel[i][j][1]
		B = pixel[i][j][2]
	else:
		R = (
		pixel[i-1][j-1][0] * kernel[0][0] + pixel[i-1][j  ][0] * kernel[0][1] + pixel[i-1][j+1][0] * kernel[0][2] + 
		pixel[i  ][j-1][0] * kernel[1][0] + pixel[i  ][j  ][0] * kernel[1][1] + pixel[i  ][j+1][0] * kernel[1][2] + 
		pixel[i+1][j-1][0] * kernel[2][0] + pixel[i+1][j  ][0] * kernel[2][1] + pixel[i+1][j+1][0] * kernel[2][2]
		)

		G = (
		pixel[i-1][j-1][1] * kernel[0][0] + pixel[i-1][j  ][1] * kernel[0][1] + pixel[i-1][j+1][1] * kernel[0][2] + 
		pixel[i  ][j-1][1] * kernel[1][0] + pixel[i  ][j  ][1] * kernel[1][1] + pixel[i  ][j+1][1] * kernel[1][2] + 
		pixel[i+1][j-1][1] * kernel[2][0] + pixel[i+1][j  ][1] * kernel[2][1] + pixel[i+1][j+1][1] * kernel[2][2]
		)

		B = (
		pixel[i-1][j-1][2] * kernel[0][0] + pixel[i-1][j  ][2] * kernel[0][1] + pixel[i-1][j+1][2] * kernel[0][2] + 
		pixel[i  ][j-1][2] * kernel[1][0] + pixel[i  ][j  ][2] * kernel[1][1] + pixel[i  ][j+1][2] * kernel[1][2] + 
		pixel[i+1][j-1][2] * kernel[2][0] + pixel[i+1][j  ][2] * kernel[2][1] + pixel[i+1][j+1][2] * kernel[2][2]
		)
	
	# if <0, then 0
	R = R*(R>0)
	G = G*(G>0)
	B = B*(B>0)

	R = R if R<256 else 255
	G = G if G<256 else 255
	B = B if B<256 else 255


	# if >255, then 255
	if R<0 or R>255 or G<0 or G>255 or B<0 or B>255:
		print(R, G, B)
	return (R,G,B)


#================================================================================
def convolve(image,kernel):
	global height
	global width

	height = len(image)
	width  = len(image[0])

	#Array to store pixel values
	out = [[multiply(image, kernel, i, j, height, width) for j in range(width)] for i in range(height)]

	return out


#================================================================================

def writeImage(image_out,filename):
	#Array to store pixel values
	pix = []
	height = len(image_out)
	width = len(image_out[0])

	# Write pixel values to the array
	for i in range(height):
		for j in range(width):
			pix += [(int(image_out[i][j][0]), int(image_out[i][j][1]), int(image_out[i][j][2]))]
	outputIm = Image.new("RGB", (width, height))
	outputIm.putdata(pix)
	outputIm.save(filename,"JPEG")
	
#! /usr/bin/env python3

# Already created as per Google's QuickStarts:
# Google Cloud Project: tiny-cloud-projects
# Google Cloud Storage Bucket Name: tcp-data
# Credentials exported as an environment variable
#    export GOOGLE_APPLICATION_CREDENTIALS=


# Already installed from the Google Cloud SDK
# https://cloud.google.com/python/docs/reference
from google.cloud import storage
from google.cloud import vision

# Standard library
import argparse
import io
import os
import subprocess

# 3rd party libraries
from PIL import Image, ImageDraw # https://pillow.readthedocs.io/en/stable/installation.html

def copy_to_clipboard(text):
	"""
	Copy the specified text to the macOS clipboard
	"""
	result = False

	try:
		p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
		p.stdin.write(bytes(text, 'utf-8'))
		p.stdin.close()
		result = True
	except Exception as err: 
		print("Error: {}".format(err))

	return result

def upload_file_to_google_cloud_bucket(file_path, bucket_name):
	"""
	Upload the specified file to the specified Google Cloud Storage bucket
	"""
	result = False

	storage_client = storage.Client()
	bucket = storage_client.get_bucket(bucket_name)

	blob_fn = os.path.basename(file_path)
	blob = bucket.blob(blob_fn)    

	try:
		blob.upload_from_filename(file_path)
		print("Uploaded [{}] to Google Cloud Storage bucket [{}]".format(blob_fn, bucket_name))
		result = "gs://{}/{}".format(bucket_name, blob_fn)
	except Exception as err:
		print("Could not upload [{}] to Google Cloud Storage bucket [{}]".format(file_path, bucket_name))

	return result


def main():
	# Get the command line arguments
	parser = argparse.ArgumentParser(description="Live Text via the CLI!")
	parser.add_argument("-i", "--in", dest="input", required=True, help="Path to the incoming file")
	parser.add_argument("-o", "--out", dest="output", required=False, help="Path to save the highlight file to")
	parser.add_argument("-c", "--clipboard", dest="copy_to_clipboard", required=False, action="store_true", help="Copy the discovered text to the clipboard")
	args = parser.parse_args()

	# From the Google QuickStart...
	# Instantiates a client
	client = vision.ImageAnnotatorClient()

	# The name of the image file to annotate
	file_name = args.input

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = vision.Image(content=content)

	response = client.text_detection(image=image)
	texts = response.text_annotations
	results = texts[0].description.strip()

	print('Text found in the passed image:')
	print(results)

	if args.copy_to_clipboard:
		copy_to_clipboard(results)

	if args.output:
		# Open the source image file
		src_img = Image.open(args.input)
		src_img = src_img.convert('RGBA')
		overlay_img = Image.new('RGBA', src_img.size)

		# Draw each polygon on the image as a semi-transparent layer to highlight the text
		draw = ImageDraw.Draw(overlay_img, mode='RGBA')
		for i, text in enumerate(texts):
			if i == 0: continue # this text contains the entire text boundaries
			# Polygon is in a dictionary called 'bounding_poly' 
			xy = []
			for v in text.bounding_poly.vertices:
				xy.append((v.x, v.y))

			draw.polygon(xy, fill=(251, 155, 87, 72), outline=(152, 65, 4, 255))

		final_img = Image.alpha_composite(src_img, overlay_img)
		final_img.save(args.output, 'PNG')

if __name__ == '__main__': main()
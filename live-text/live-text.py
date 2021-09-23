#! /usr/bin/env python3

# Already created as per Google's QuickStarts:
# Google Cloud Project: tiny-cloud-projects
# Google Cloud Storage Bucket Name: tcp-data

# Already installed
from google.cloud import storage
from google.cloud import vision

# Standard library
import argparse
import io
import os
import subprocess

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
	parser.add_argument("-c", "--clipboard", dest="copy_to_clipboard", required=False, action="store_true", help="Copy the discovered text to the clipboard")
	args = parser.parse_args()

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
	print('Text found in the passed image:')

	print(texts[0].description.strip())
	results = texts[0].description.strip()

	if args.copy_to_clipboard:
		copy_to_clipboard(results)

	#for text in texts:
	#	print('\n"{}"'.format(text.description.strip()))

	#vertices = (['({},{})'.format(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices])

	#print('bounds: {}'.format(','.join(vertices)))

if __name__ == '__main__': main()
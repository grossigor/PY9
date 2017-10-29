import os
import subprocess
import queue
import threading

def get_source_abs_path(): 
	current_dir = os.path.dirname(os.path.abspath(__file__))
	source_path = os.path.join(current_dir, 'Source')
	return source_path

def get_jpg_files_in_folder(folder_path):
	files = os.listdir(folder_path)
	jpg_files = list(filter(lambda x: x.endswith('.jpg'), files))
	return jpg_files

def convert_file_from_queue():
	while True:
		item = q.get()
		if item is None:
			break
		cmd = 'convert ./Source/'+ item +' -resize 200 ./Result/' + item
		subprocess.run(cmd)
		q.task_done()

def put_source_to_queue(sources):
	for source in sources:
		q.put(source)

def run_threads():
	threads = []
	for i in range(4):
		t = threading.Thread(target=convert_file_from_queue)
		t.start()
		threads.append(t)
	return threads

def stop_threads(threads):
	for i in range(4):
		q.put(None)
	for t in threads:
		t.join()

if __name__ == '__main__':
	folder_path = get_source_abs_path()
	files = get_jpg_files_in_folder(folder_path)
	q = queue.Queue()
	put_source_to_queue(files)
	threads = run_threads()
	q.join()
	stop_threads(threads)

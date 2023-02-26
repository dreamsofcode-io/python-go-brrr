import time
import os
import multiprocessing
from PIL import Image, ImageFilter

outdir = "blurred"
filenames = [f'images/{i}.jpg' for i in range(1,6)]

def blur_image(filename):
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur(radius=160))
    img.save(f'{outdir}/{os.path.basename(filename)}')

def run_multi():
    processes = [multiprocessing.Process(target=blur_image, args=[filename]) 
                for filename in filenames]
    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    os.makedirs(outdir, exist_ok=True)

    # Multi processing test
    start = time.perf_counter()
    run_multi()
    finish = time.perf_counter()

    print(f'{finish-start: .2f} second(s) for multiprocessing')

    # Single processing test
    start = time.perf_counter()
    for filename in filenames:
        blur_image(filename)
    finish = time.perf_counter()

    print(f'{finish-start: .2f} second(s) for single processing')

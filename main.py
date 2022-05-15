import os, cv2
from tqdm import tqdm
from skimage.metrics import structural_similarity as ssim

from params import images_folder

def main():

    target_dim = (50, 50)

    # load and prepare the target image
    target_folder = 'input/'
    target_files = os.listdir(target_folder)
    target_image = cv2.imread(target_folder + target_files[0])
    target_image = cv2.resize(target_image, target_dim)
    gray_image1 = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

    # list of all the images to compare
    all_images = os.listdir(images_folder)

    # search the most similar
    max_similarity = 0
    match_images = []
    pbar = tqdm(total=len(all_images))
    for file in all_images:

        image2 = cv2.imread(images_folder + file)
        image2 = cv2.resize(image2, target_dim)
        gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        similarity = ssim(gray_image1, gray_image2)

        if similarity == max_similarity:
            match_images.append(file)

        if similarity > max_similarity:
            match_images = [file]
            max_similarity = similarity

        pbar.update(1)
    pbar.close()


    print(f'Most similar image is {match_images}')

    if len(match_images) > 1:
        print('WARNING: Multiple images have the same similarity.')
        print('Do a manual check, increase precision or remove grayscale')


if __name__ == '__main__':
    main()
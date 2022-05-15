# NFT image finder

### Features
- Given an NFT image find the **NFT id** by searching through a folder of NFT images (using a SSIM model)
- Requires a folder with all the indexed NFTs 

To speed up the computation images are resized and converted to grayscale (accuracy is still 100%).

### Usage
- Install the requirements in a Python 3.8+ environment
- Copy target NFT in the **input** folder, set the NFTs folder path in the params.py file, then launch main.py

from nii_procesor.image_loader import read_nii
#from nibabel.viewers import OrthoSlicer3D
import argparse

parser = argparse.ArgumentParser(description="nii loader")
parser.add_argument("--input", type=str, help="input nii file path")
parser.add_argument("--output", type=str, help="output nii file path")



def main(args):
    
    # 读取nii.gz文件
    nii_path = args.input
    img = read_nii(nii_path)
    #OrthoSlicer3D(img.dataobj).show()

    
if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
#Chap07_다운로드받은파일자동분류.py
import os
import shutil
import glob

# 다운로드 받은 폴더 경로 설정
download_folder = 'C:/Users/User/Downloads'

# 분류할 폴더 경로 설정
image_folder = 'C:/Users/User/Downloads/Images'
pdf_folder = 'C:/Users/User/Downloads/PDFs'
dataset_folder = 'C:/Users/User/Downloads/DataSets'
archive_folder = 'C:/Users/User/Downloads/Archives'

# 폴더 생성 함수
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# 파일 분류 함수
def classify_file(file_path, file_name):
    extension = os.path.splitext(file_name)[1].lower()
    if extension in ['.jpg', '.jpeg']:
        create_folder(image_folder)
        shutil.move(file_path, os.path.join(image_folder, file_name))
    elif extension == '.pdf':
        create_folder(pdf_folder)
        shutil.move(file_path, os.path.join(pdf_folder, file_name))
    elif extension in ['.csv', '.tsv', '.xlsx']:
        create_folder(dataset_folder)
        shutil.move(file_path, os.path.join(dataset_folder, file_name))
    elif extension == '.zip':
        create_folder(archive_folder)
        shutil.move(file_path, os.path.join(archive_folder, file_name))

# 다운로드 폴더 내 파일 분류
for file_path in glob.glob(os.path.join(download_folder, '*')):
    if os.path.isfile(file_path):
        classify_file(file_path, os.path.basename(file_path))

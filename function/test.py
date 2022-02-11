from dataAnalysis.workspace import select
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file1=BASE_DIR+"/file_page1/bh.txt"
file2=BASE_DIR+"/file_page2/us.txt"
result=str(select(file1,file2))

print(result)

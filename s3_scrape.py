import sys
import requests
from bs4 import BeautifulSoup


if len(sys.argv) < 3:
  print("\n\n------------ USAGE ------------------")
  print("Process a file of S3 bucket names:  s3_scrape.py -f <file name>")
  print("-------------------------------------\n\n")
  sys.exit(1)

check_type = sys.argv[1]

if "-f" in check_type:
  bucketsFile = sys.argv[2]


fileCounter = 0
totalFiles = 0
bucketsOpen = 0
bucketsClosed = 0
totalBuckets = 0

with open(bucketsFile, 'r') as f:
    for bucket in f:
        try:
            r = requests.get("http://"+bucket.strip(), verify=False)
            soup = BeautifulSoup(r.content, 'lxml-xml')
        except requests.exceptions.ConnectionError:
            print("\n\nConnection Error:  This S3 bucket could not be accessed\n\nExiting....\n\n")
            quit()
        if "200" not in str(r):
            print("[*] Access Denied:  " + bucket)
            bucketsClosed += 1
            totalBuckets += 1
        else:
            print("\n\n-------------------- BUCKET ACCESSIBLE --------------------")
            print("\n[!] Bucket Accessible:  " + bucket)
            entries = soup.find_all('Contents')
            files = soup.find_all('Key')
            lastModified = soup.find_all('LastModified')
            size = soup.find_all('Size')
            storage = soup.find_all('StorageClass')
            fileCounter = 0
            bucketsOpen += 1
            totalBuckets += 1
            for i in range(0, len(files)):
                print("\n\tFile Name: " + files[i].get_text(), end=' ')
                print("\n\tLast Modified: " + lastModified[i].get_text(), end=' ')
                print("\n\tFile Size: " + size[i].get_text(), end=' ')
                print("\n\tStorage Class: " + storage[i].get_text())
                fileCounter += 1
                totalFiles += 1
            print("\n\nTotal Files in Bucket:  " + str(fileCounter) + "\n\n")
            print("\n-----------------------------------------------------------\n\n")

print("\n\n\n-------------------- STATISTICS --------------------")
print("\nTotal Buckets Checked:  " + str(totalBuckets))
print("Accessible Buckets:  " + str(bucketsOpen))
print("Inaccessible Buckets:  " + str(bucketsClosed))
print("Accessible Files:  " + str(totalFiles))
print("\n-----------------------------------------------------\n\n")

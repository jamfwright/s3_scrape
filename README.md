# s3_scrape
Checks for and lists accessible files and file information for multiple AWS S3 Buckets

Throw the the list of AWS S3 Buckets into a file and run this tool to see what (if any) files are publicly accessible.  Makes assessments fast and easy.

## Usage

### Basic

`python s3_scrape.py -f file_with_buckets.txt`

### Redirect to file

`python s3_scrape.py -f file_with_buckets.txt > bucket_data.txt`

## Output

The output is live and shows whether or not the bucket is accessible and if accessible, provides information about the files.  Statistics are listed at the end of the output.

### Example Output

`-------------------- BUCKET ACCESSIBLE --------------------

[!] Bucket Accessible:  example1.s3.amazonaws.com


        File Name: filename1.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 7207
        Storage Class: STANDARD

        File Name: filename2.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 600
        Storage Class: STANDARD


Total Files in Bucket:  2



-----------------------------------------------------------




-------------------- BUCKET ACCESSIBLE --------------------

[!] Bucket Accessible:  example2.s3.amazonaws.com


        File Name: filename1.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 7207
        Storage Class: STANDARD

        File Name: filename2.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 600
        Storage Class: STANDARD

        File Name: filename3.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 7207
        Storage Class: STANDARD

        File Name: filename4.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 600
        Storage Class: STANDARD

        File Name: filename5.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 600
        Storage Class: STANDARD

       
Total Files in Bucket:  5



-----------------------------------------------------------




-------------------- BUCKET ACCESSIBLE --------------------

[!] Bucket Accessible:  example3.s3.amazonaws.com


       File Name: filename1.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 600
        Storage Class: STANDARD

       File Name: filename2.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 600
        Storage Class: STANDARD
		
		File Name: filename3.txt
        Last Modified: 2019-05-21T13:33:23.000Z
        File Size: 600
        Storage Class: STANDARD


Total Files in Bucket:  3



-----------------------------------------------------------


[*] Access Denied:  example4.s3.amazonaws.com

[*] Access Denied:  example5.s3.amazonaws.com

[*] Access Denied:  example6.s3.amazonaws.com



-------------------- BUCKET ACCESSIBLE --------------------

[!] Bucket Accessible:  example7.s3.amazonaws.com



Total Files in Bucket:  0



-----------------------------------------------------------


[*] Access Denied:  example8.s3.amazonaws.com

[*] Access Denied:  example9.s3.amazonaws.com

[*] Access Denied:  example10.com.s3.amazonaws.com




-------------------- STATISTICS --------------------

Total Buckets Checked:  10
Accessible Buckets:  4
Inaccessible Buckets:  6
Accessible Files:  10

-----------------------------------------------------
`

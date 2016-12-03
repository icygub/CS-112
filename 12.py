#Program: 12 Web Scraping
#Names: , Walter
#Date: //2016
#Instructor: Jeff Light
#Description:  A program that will put members of the Church into different classifications.

#https://automatetheboringstuff.com/files/rj.txt
import requests

def main(): #main function need in all programs for automated testing

    
    while True:# Loops the request for entering a URL
        try:
            print ("Enter a full, valid URL: ")# Prompt the user to enter a URLsol
            url = input ()
            if not('https://' in url or 'http://' in url):
                url = 'https://' + url
            res = requests.get(url)
            res.raise_for_status()
            break
        except:
            print ("Oops, That URL does not work. Try again. ")
            
            
    
    print ("Enter a Filename: ")# Prompts the user a filename to the file.
    filename = input ()
    playFile = open (filename, 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    
    
    playFile.close()



if __name__ == '__main__':
    main()  #excucte main function

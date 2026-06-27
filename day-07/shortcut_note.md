
1)  r+  - read + overwrite   - Pointer (start)     - no truncate 
2)  w+  - read + overwrite   - pounter(no matter)  - truncate
3)  a+  - read + append      - pointer (end)       - no truncate


Function	                           কাজ
1)open("file.txt", "w")	     -   File তৈরি/overwrite
2)open("file.txt", "r")	     -  File read
3)open("file.txt", "a")	     -   File append
4)os.remove("file.txt")	     -   File delete
5)os.path.exists("file.txt") -	File আছে কি না check
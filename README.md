
RSA Factoring Challenge
Algorithm
Factorize as many numbers as possible into a product of two smaller numbers.
Scripting
You can choose the language of your choice.
OS needs to be Standard Ubuntu 20.04 LTS.
Project Details
Weight: 1
Project will start on Mar 25, 2024, at 5:00 AM, and must end by Apr 8, 2024, at 5:00 AM.
Checker was released on Mar 28, 2024, at 5:00 PM.
An auto review will be launched at the deadline.
Background Context
Before you continue reading, start this [song](add link here) in the background.

We have sniffed an unsecured network and found numbers that are used to encrypt very important documents. It seems that those numbers are not always generated using large enough prime numbers. Your mission should you choose to accept it, is to factorize these numbers as fast as possible before the target fixes this bug on their server - so that we can decode the encrypted documents.

This project is NOT mandatory at all. It is 100% optional. Doing any part of this project will add a project grade of over 100% to your average. Your score won’t get hurt if you don’t do it, but if your current average is greater than your score on this project, your average might go down. Have fun!

Resources
Read or watch:

RSA
How does HTTPS provide security?
Prime Factorization
Why RSA?
Requirements
General

You can choose the language of your choice.
OS needs to be Standard Ubuntu 20.04 LTS.
Tasks

Factorize all the things!

Factorize as many numbers as possible into a product of two smaller numbers.
Usage: factors <file>
<file> is a file containing natural numbers to factor. One number per line.
Output format: n=p*q, one factorization per line. p and q don’t have to be prime numbers.
Your program should run without any dependency: You will not be able to install anything on the machine we will run your program on.
Time limit: Your program will be killed after 5 seconds if it hasn’t finished.
RSA Factoring Challenge

RSA Laboratories states that: for each RSA number n, there exist prime numbers p and q such that n = p × q. The problem is to find these two primes, given only n.
This task is the same as Task 0, except:
p and q are always prime numbers.
There is only one number in the files.
How far can you go in less than 5 seconds?
Example
ruby
Copy code
julien@ubuntu:~/factors$ cat tests/test00 
4
12
34
128
1024
4958
1718944270642558716715
9
99
999
9999
9797973
49
239809320265259
julien@ubuntu:~/factors$ time ./factors tests/test00
4=2*2
12=6*2
34=17*2
128=64*2
1024=512*2
4958=2479*2
1718944270642558716715=343788854128511743343*5
9=3*3
99=33*3
999=333*3
9999=3333*3
9797973=3265991*3
49=7*7
239809320265259=15485783*15485773

real    0m0.009s
user    0m0.008s
sys     0m0.001s
Repository
GitHub repository: RSA-Factoring-Challenge
Files: factors, rsa

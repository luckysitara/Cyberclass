

### **Retrieving System Information with Bash**

**1. Retrieving CPU Information:**

The CPU is the brain of the computer, and you can retrieve detailed information about it using Bash commands.

- **Command:**
  ```bash
  cat /proc/cpuinfo | grep 'model name'
  ```

- **Explanation:**
  - The `/proc/cpuinfo` file contains detailed information about the CPU, such as model name, number of cores, and more.
  - The `cat` command displays the content of this file.
  - `grep 'model name'` filters the output to only show lines containing the phrase "model name," which typically includes the CPU's model.

- **Example Output:**
  ```bash
  model name      : Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
  model name      : Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
  ```

This output shows that the system is using an Intel i7-8550U CPU.

**2. Retrieving Memory Information:**

Memory usage is crucial for understanding how your system is managing RAM.

- **Command:**
  ```bash
  free -h
  ```

- **Explanation:**
  - The `free` command provides a snapshot of the system's current memory usage, including total, used, and free memory.
  - The `-h` option stands for "human-readable," which displays the sizes in KB, MB, or GB instead of raw bytes, making it easier to interpret.

- **Example Output:**
  ```bash
               total        used        free      shared  buff/cache   available
  Mem:           16G        4.7G        2.8G        732M        8.5G        10G
  Swap:         8.0G        2.0M        8.0G
  ```

This output shows the total memory (16GB), used memory (4.7GB), and available memory (10GB), along with swap memory details.

**3. Retrieving Disk Usage:**

Monitoring disk usage helps in understanding how much storage space is used and available.

- **Command:**
  ```bash
  df -h
  ```

- **Explanation:**
  - `df` stands for "disk filesystem" and shows the amount of disk space used and available on mounted filesystems.
  - The `-h` option makes the output human-readable by using KB, MB, or GB instead of blocks.

- **Example Output:**
  ```bash
  Filesystem      Size  Used Avail Use% Mounted on
  /dev/sda1       500G  120G  360G  25% /
  tmpfs            16G  3.2M   16G   1% /dev/shm
  ```

This output indicates that the root partition (`/dev/sda1`) has a total size of 500GB, with 120GB used and 360GB available.

**4. Retrieving System Uptime:**

Knowing how long your system has been running can be useful for maintenance and troubleshooting.

- **Command:**
  ```bash
  uptime
  ```

- **Explanation:**
  - The `uptime` command shows how long the system has been running, the number of users currently logged in, and the load averages for the past 1, 5, and 15 minutes.

- **Example Output:**
  ```bash
  14:32:16 up 3 days,  4:52,  3 users,  load average: 0.25, 0.35, 0.45
  ```

This output shows that the system has been running for 3 days, 4 hours, and 52 minutes, with 3 users logged in and low load averages.

### **Monitoring System Processes and Resources**

Monitoring processes and resources is essential for maintaining system performance and diagnosing issues.

**1. Monitoring with `top`:**

- **Command:**
  ```bash
  top
  ```

- **Explanation:**
  - `top` is an interactive command-line utility that provides a dynamic, real-time view of the system’s running processes.
  - The display is constantly updated, showing the most resource-consuming processes at the top.
  - It includes information such as CPU and memory usage, process ID, user, and the command that started the process.

- **Example:**
  When you run `top`, you might see output like this:
  ```bash
  top - 15:00:01 up 3 days,  5:20,  2 users,  load average: 0.12, 0.18, 0.20
  Tasks: 193 total,   1 running, 192 sleeping,   0 stopped,   0 zombie
  %Cpu(s):  1.2 us,  0.3 sy,  0.0 ni, 98.3 id,  0.0 wa,  0.2 hi,  0.0 si,  0.0 st
  KiB Mem : 16308428 total,  4819548 free,  2985648 used,  8503248 buff/cache
  KiB Swap:  8191996 total,  8191988 free,        8 used. 11859488 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  14806 user      20   0  150352  16256   9592 S   1.3  0.1   0:00.45 gnome-terminal-
  14867 user      20   0   85704   6648   5896 S   0.7  0.0   0:00.18 bash
  ```

- **Key Sections:**
  - **Tasks:** Total processes and their states (running, sleeping, stopped, zombie).
  - **%Cpu(s):** Shows the CPU utilization percentages.
  - **KiB Mem:** Provides a breakdown of memory usage (total, free, used, and cache).
  - **Process List:** Displays running processes, sorted by CPU usage by default. It includes the PID, user, priority, CPU and memory usage, and the command name.

**2. Process Monitoring with `ps`:**

- **Command:**
  ```bash
  ps aux | grep process_name
  ```

- **Explanation:**
  - The `ps` command displays information about active processes.
  - `aux` is a set of options:
    - `a` shows processes for all users.
    - `u` shows the processes' owners.
    - `x` shows processes not attached to a terminal.
  - `grep process_name` filters the output to show only processes matching a specific name.

- **Example:**
  To find all instances of a process named "nginx," you would run:
  ```bash
  ps aux | grep nginx
  ```

- **Example Output:**
  ```bash
  root      1013  0.0  0.1 125460  1752 ?        Ss   Aug18   0:00 nginx: master process /usr/sbin/nginx
  www-data  1014  0.0  0.2 125700  2436 ?        S    Aug18   0:00 nginx: worker process
  www-data  1015  0.0  0.2 125700  2436 ?        S    Aug18   0:00 nginx: worker process
  ```

This output shows the `nginx` master process and its worker processes, along with their PIDs, user, CPU, and memory usage.

### **Monitoring Resources**

- **Monitoring Disk Usage with `du`:**
  
  To see the disk usage of a specific directory:
  ```bash
  du -sh /home/user
  ```
  - `-s`: Summarize, showing only the total size.
  - `-h`: Human-readable output.
  
  Example output:
  ```bash
  12G /home/user
  ```

- **Monitoring CPU and Memory Usage:**
  
  To monitor CPU and memory usage over time:
  ```bash
  vmstat 2
  ```
  This command displays system performance statistics every 2 seconds.

  Example output:
  ```bash
  procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
   r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
   1  0      0 2028596  23672 4563240    0    0    26    22  132  385  1  1 98  0  0
   0  0      0 2028316  23672 4563240    0    0     0     0  118  377  0  0 100  0  0
  ```

This displays CPU, memory, I/O, and process information at regular intervals.

These tools are indispensable for system administrators, allowing them

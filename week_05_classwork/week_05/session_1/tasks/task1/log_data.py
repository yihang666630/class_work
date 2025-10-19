# log files are provided by websites to track different http requests and where they come from
# this is useful for blocking disruptive IP addresses, tracking failed login attempts, and handling DDOS attacks
# site.log is an example of a log file - you can see it is not very human-readable

# open and read the file
# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format such as:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20

# Additional hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - Use list comprehension or loops to filter the data
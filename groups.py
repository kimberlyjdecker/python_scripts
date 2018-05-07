#!/usr/bin/python3

# Script to re-create GROUPS command
# GROUPS can be used in 2 ways:
#   - groups (alone)
#   - groups username(s)
# Evaluate whether entered usernames exist

import os
import sys
import grp
import getpass

def main():
   """Evaluate number of command line arguments"""
   if len(sys.argv) == 1:
      user_name = getpass.getuser()
      show_groups(user_name)      

   if len(sys.argv) == 2:
      user_name = sys.argv[1]
      show_groups(user_name)
  
   if len(sys.argv) > 2:
      num_users = len(sys.argv)
      for u in range(1, num_users):
         user_name = sys.argv[u]
         show_groups(user_name)

def show_groups(user_name):
  """Determine groups user belongs to; print"""

   check_user(user_name)

   group_id = os.getgid()
   groups = os.getgrouplist(user_name, group_id)

   print("The user " + user_name + " belongs to the following groups:")

   for g in groups:
      group_db = grp.getgrgid(g)
      gname = group_db[0]
      print(gname) 
     
def check_user(user_name):
   """Check if username exists"""
   
   with open('/etc/passwd') as f:
      users = [x.strip() for x in f.readlines()]

   for line in users:
      line = line.split(':')
      
      if line[0] == str(user_name):
         return
      
   print("You did not enter a correct user. Try again")
   exit()

main()

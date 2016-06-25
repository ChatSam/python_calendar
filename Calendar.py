"""
This is a calendar app
Author - Chatura Samarasinghe
"""

from time import sleep, strftime;

name = raw_input("Whats your name ? ");
calendar  ={};

def welcome ():
  print "Welcome "+ name +" !";
  print "opening your calendar ..."
  sleep(1);

  print "Today is "+ strftime('%A %B %d, %Y');
  print "Current Time is "+ strftime('%H:%M:%S');
  sleep(1);

  print "What would you like to do?";

def start_calendar():
  welcome();

  start = True;

  while(start):
    user_choice = raw_input('A to Add, U to Update,V to View, D to Delete, X to Exit:');
    user_choice = user_choice.upper();

    if (user_choice == 'V'):
      if(len(calendar.keys()) < 1):
        print "Your calendar is empty.";

      else:
        print calendar;

    elif(user_choice == 'U'):
      date = raw_input ('What date ? ');
      update = raw_input ('Enter the update:');

      calendar[date] = update;

    elif(user_choice == 'A'):
      event = raw_input ('Enter event: ');
      date = raw_input ('Enter date (MM/DD/YYYY) : ');

      if (len(date) > 10 or int (date[6:]) < int(strftime("%Y"))):

        print "Incorrect date or date format. Please re-enter the date";

        try_again = raw_input ("Try Again? Y for Yes, N for No: ");
        try_again = try_again.upper();

        if(try_again == 'Y'):
          continue;
        else:
          start = False;
      else:
        calendar[date] = event;

    elif(user_choice == 'D'):

      if(len(calendar.keys()) < 1):
        print "nothing to delete.";
      else:

        event = raw_input("What event?")

        for date in calendar.keys():
          if (calendar[date] == event):
            del calendar[date];
            print "Event sucessfully deleted";
          else:
            print "no similar events";

    elif(user_choice == 'X'):
     	start = False;
    else:
      print "Invaid command. Calendar is exciting. . ."

start_calendar();




















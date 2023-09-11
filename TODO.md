# NabaatBot TODO list
Initial proof of concept

### Todo

- [ ] Get a list of group topics and each corresponding ID (message_thread_id param in bot.send_message) 

### In Progress

- [ ] 

### Done ✓

- [x] Make sure telethon is capable of creating groups and topics
  - Topic IDs are integer values incremented each time a new topic is generated
- [x] Make sure the groups and topics are accessible by a PTB bot
  - Remember to add -100 to the group ID returned by telethon (ID is int)
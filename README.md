# bdaybot

[![Join the chat at https://gitter.im/bdaybot/Lobby](https://badges.gitter.im/bdaybot/Lobby.svg)](https://gitter.im/bdaybot/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is a bot that will like and comment 'Thank you' on all the birthday posts posted on your timeline.
It uses Selenium to automate facebook login and successively locating the birthday posts using web scrapping. The project is under heavy development.
***
This could have required no use of Selenium, and could have been done by using Facebook's Graph API, but only till the previous version. In the current version, API doesnt give access to the bdday posts individually. Instead, it groups all the 150 posts, say, and makes it a 1 story, with one story-id. There are no indvidual post-ids to access them.

##TODO :

- [x]  Automate facebook login
- [ ]  Locate Bdday posts from the user's wall, iterate over them, like and comment.
- [ ]  Convert above into an extension or a web-app
- [ ]  Launch it as an .exe file for windows

Any suggestions or contributions are welcome!

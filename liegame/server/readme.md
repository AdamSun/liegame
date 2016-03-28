
----------------------------intro-----------------------------------
this is a lie game server.

there are 5 parts for this server:
1 gate server,it is the first server that client(no specific platform) connects, its main job is distribute the client to
a logic server by some kind of principle.when the connection is successful,gate server will tell the client the info of login
server and then disconnect with the client

2 logic server,after the client disconnect with the gate server,logic server is the second step of the connection,its
main job is to handler the logic work, for example the login handler and the distribution of 'house' for the client. the
server distribution is working in this step.

3 db server

4 log server


------------------------------install---------------------------------------



------------------------------startup---------------------------------------
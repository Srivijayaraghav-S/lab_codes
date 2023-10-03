#include<bits/stdc++.h>
#include<arpa/inet.h>
#include<sys/socket.h>
#define n 5
using namespace std;
int main(void)
{
    sockaddr_in server,client;
    int m[n];
    //Create socket
    int server_sock=socket(AF_INET,SOCK_STREAM,0);
    if(server_sock==-1)
    {
        cerr<<"Socket creation failed"<<endl;
        return 1;
    }
    cout<<"Socket created"<<endl;
    //Prepare the sockaddr_in structure
    server.sin_family=AF_INET;
    server.sin_addr.s_addr=INADDR_ANY;
    server.sin_port=htons(8880);
    //Bind the socket
    int b=bind(server_sock,(sockaddr*)&server,sizeof(server));
    if(b<0)
    {
        cerr<<"Binding failed"<<endl;
        return 1;
    }
    cout<<"Binding done"<<endl;
    //Listen to the socket
    listen(server_sock,10);
    cout<<"Waiting for incoming connections"<<endl;
    //Accept connection from an incoming client
    int c=sizeof(sockaddr_in);
    int client_sock=accept(server_sock,(sockaddr*)&client_sock,(socklen_t*)&c);
    if(client_sock<0)
    {
        cerr<<"Accept failed"<<endl;
        return 1;
    }
    cout<<"Connection accepted"<<endl;
    //Receive a message from client
    int r;
    while((r=recv(client_sock,&m,5*sizeof(int),0))>0)
    {
        sort(m,m+n);
        write(client_sock,&m,5*sizeof(int));
    }
    if(r==0)
    {
        cout<<"Client disconnected"<<endl;
    }
    else if(r==-1)
    {
        cerr<<"Receiving failed"<<endl;
        return 1;
    }
    return 0;
}
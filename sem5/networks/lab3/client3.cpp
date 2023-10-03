#include<bits/stdc++.h>
#include<arpa/inet.h>
#include<sys/socket.h>
#define n 20
using namespace std;
int main(void)
{
    sockaddr_in server;
    string str;
    char buffer[1024];
    cout<<"Enter string"<<endl;
    cin>>str;
    //Create socket
    int sock=socket(AF_INET,SOCK_STREAM,0);
    if(sock==-1)
    {
        cout<<"Socket creation failed"<<endl;
        return 1;
    }
    cout<<"Socket created"<<endl;
    //Prepare the sockaddr_in structure
    server.sin_addr.s_addr=inet_addr("127.0.0.1");
    server.sin_family=AF_INET;
    server.sin_port=htons(4953);
    //Connect to remote server
    int con=connect(sock,(sockaddr*)&server,sizeof(server));
    if(con<0)
    {
        cerr<<"Connection failed"<<endl;
        return 1;
    }
    cout<<"Connected"<<endl;
    int s=send(sock,str.c_str(),str.size(),0);
    if(s<0)
    {
        cerr<<"Sending failed"<<endl;
        return 1;
    }
    //Receive reply from server
    int r=recv(sock,buffer,sizeof(buffer),0);
    if(r<0)
    {
        cerr<<"Receiving failed"<<endl;
        return 1;
    }
    cout<<"Server reply:"<<endl;
    cout<<buffer<<endl;
    //Close socket
    close(sock);
    return 0;
}
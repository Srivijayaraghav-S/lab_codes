#include<bits/stdc++.h>
#include<arpa/inet.h>
#include<sys/socket.h>
#define n 5
using namespace std;
int main(void)
{
    sockaddr_in server;
    int v[n],server_v[n];
    cout<<"Enter numbers"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>v[i];
    }
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
    server.sin_port=htons(8880);
    //Connect to remote server
    int con=connect(sock,(sockaddr*)&server,sizeof(server));
    if(con<0)
    {
        cerr<<"Connection failed"<<endl;
        return 1;
    }
    cout<<"Connected"<<endl;
    int s=send(sock,&v,n*sizeof(int),0);
    if(s<0)
    {
        cerr<<"Sending failed"<<endl;
        return 1;
    }
    //Receive reply from server
    int r=recv(sock,&server_v,n*sizeof(int),0);
    if(r<0)
    {
        cerr<<"Receiving failed"<<endl;
        return 1;
    }
    cout<<"Server reply:"<<endl;
    for(int i:server_v)
    {
        cout<<i<<" ";
    }
    cout<<endl;
    //Close socket
    close(sock);
    return 0;
}
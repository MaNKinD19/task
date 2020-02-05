var a=function()
{
var arr=[];
n=parseInt(prompt("Enter Length"));
for(i=0;i<n;i++)
{
    arr[i]=parseInt(prompt("Enter elements"));
}
for(i=0;i<n;i++)
    {   var rem=0, rev=0, temp;
        temp=arr[i];
        console.log("1")
        while(arr[i]>0)
        {
            console.log("2")
            rem=arr[i]%10;
            rev=(rev*10)+rem;
            arr[i]=parseInt((arr[i])/10);
        }
        if(temp==rev){
            console.log('3')
            document.write(temp);}
        else{
            console.log('4')
            break;}
}
}
a();

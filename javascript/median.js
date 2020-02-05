var a=function()
{
var arr=[];
n=parseInt(prompt("Enter number of elements"));
for(i=0;i<n;i++)
    arr[i]=parseInt(prompt("Enter elements"))
if(n%2==1)
{
    document.write(arr[(n-1)/2]);
}
else
{
    sum=(arr[n/2]+arr[(n/2)-1])/2;
    document.write(sum);
}
}
a();

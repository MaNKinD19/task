var a=function()
{
var arr=[];
var ct=0;
n=parseInt(prompt("Enter Length"));
for(i=0;i<n;i++)
{
    arr[i]=parseInt(prompt("Enter elements"));
}
document.write("Prime :")
for(i=0;i<n;i++)
    {
        for( j=2;j<arr[i];j++)
        {
            if(arr[i]==2)
                document.write(arr[i])
            if(arr[i]%j===0)
            {
                break
            }       
            else
            {
                document.write(+arr[i])
                break;
            }
      
    }
}
}
a();

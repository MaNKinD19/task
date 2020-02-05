var a=function(){
var sum=0;
var arr=[];
n=parseInt(prompt("Enter Length"));
for(i=0;i<n;i++){
    arr[i]=parseInt(prompt("Enter elements"));
    sum=sum+arr[i];
}
document.write("Sum: "+sum);
}
a();

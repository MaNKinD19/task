function fg1(n)
{
fetch("https://restcountries.eu/rest/v2/all")
    .then(response => response.json())
    .then(commits => {
            a=commits[n];
    document.write("Name :"+a.name+"<br>Alpha2Code : "+a.alpha2Code+"<br>Capital :"+a.capital+'<br> Region: '+a.region+'<br> Borders : '+a.borders)})
}

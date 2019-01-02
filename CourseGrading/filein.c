void main()
{
FILE * in;
/*Open the file*/
if((in=fopen("in.txt","r"))==NULL)
{
printf("Can&rsquo;t open in.txt!");
return;
}
/*Close the file,
and return.*/
fclose(in);
}
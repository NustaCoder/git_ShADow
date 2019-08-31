import java.math.*;

class MyClass
{
    public String returnBinary(int val,int n)
    {
        String str="";
        int rem=val;
        while(rem>0)
        {
            if(rem%2==0)
            {
                str+="0";
                rem=rem/2;
            }
            else if(rem==1)
            {
                str+="1";
                break;
            }
            else{
                str+="1";
                rem=rem/2;
            }
        }
        while(str.length()<n)
        {
            str+="0";
        }
        StringBuffer sb=new StringBuffer(str);
        str=sb.reverse().toString();
        return str;
    }
}
public class LongInc
{
    public static void main(String st[])
    {
        MyClass mc=new MyClass();   
        int[] arr={0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15};
        int n=arr.length;
        int p=(int)Math.pow(2, n);
        int len=0;
        for(int i=0;i<p;i++)
        {
            String bin=mc.returnBinary(i, n);
            int tmp=0;
            int val=0;
            for(int j=0;j<n;j++)
            {
                if(bin.charAt(j)=='1')
                {
                    if(val<=arr[j])
                    {
                        tmp+=1;
                        val=arr[j];
                    }
                    else{
                        break;
                    }
                }
            }
            if(tmp>len)
            {
                len=tmp;
            }
        }
        System.out.println(len);
    }
}
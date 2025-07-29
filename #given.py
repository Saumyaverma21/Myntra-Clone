 #given
#a=array,subarray size=k,subarray sum=t
#1<=a.length<=10^5 , 1<=k<=a.length
def checkSubarraySum(arr, n, k,sum ):

    for i in range (n - k + 1): 

        current_sum = 0;

        
        for j in range(k):
            current_sum = (current_sum +arr[i + j]) ;
                            

        if (current_sum == sum):
            return True;     
        return False;
arr=[1,2,1,2,3,1,1,3,4];
k=3;
t=5;
n = len(arr);

if (checkSubarraySum(arr, n, k, sum)):
    print("YES");
else:
    print("NO");



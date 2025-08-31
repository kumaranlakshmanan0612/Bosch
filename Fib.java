import java.util.*;
public class  Fib{
   public static void main(String[] args) {
    int n=fib(4 );
    System.out.println(n);
    int a=sum(1234);
    System.out.println(a);
    int[] arr={0,1,2,0};
    System.out.println(sorted(arr,0,1));
    ArrayList<Integer> list=new ArrayList<>();
    ArrayList<Integer> l=new ArrayList<>();
    l=find(arr,0,0);
    System.out.println(l);
    int[] ans=sort(arr);
    System.out.println(Arrays.toString(ans));
       }
       public static ArrayList<Integer> find(int[] arr, int n, int k) {
        ArrayList<Integer> list=new ArrayList<>();
        if(n==arr.length){
          return list;
        }
        if(arr[n]==k){
          list.add(n);
        }
        list.addAll(find(arr,n+1,k));
        return list;
      }
      public static int[] sort(int[] arr){
        if(arr.length==1){
          return arr;
        }
        int mid=(0+arr.length)/2;
        int[] left=sort(Arrays.copyOfRange(arr, 0, mid));
        int[] right=sort(Arrays.copyOfRange(arr, mid, arr.length));
        int i=0;
        int j=0;
        int k=0;
        int[] ans=new int[left.length+right.length];
        while(i<left.length && j<right.length){
          if(left[i]<=right[j]){
             ans[k]=left[i];
             i++;
             k++;
          }else{
            ans[k]=right[j];
            j++;
            k++;
          }
        }
        while(i<left.length){
          ans[k]=left[i];
          i++;
          k++;
        }
        while(j<right.length){
          ans[k]=right[j];
            j++;
            k++;
        }
        System.out.println("left"+Arrays.toString(left));
        System.out.println("right"+Arrays.toString(right));
        return ans;
      }
       public static int fib(int n){
       if(n==1){
        return 1;
       }
       return n*fib(n-1);
   }
   public static int sum(int n){
    if(n==0){
      return 0;
    }
    return (n%10)+sum(n/10);
   }
   public static boolean sorted(int[] arr,int a,int b){
    if(a==arr.length-2){
      return arr[a]<=arr[b];
    }
    return arr[a]<=arr[b] && sorted(arr,a+1,b+1);
   }
}
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class prac {
  public static void main(String[] args) {
    //Scanner sc=new Scanner(System.in);
    //int n=sc.nextInt();
    //System.out.println(sum(n));
    ArrayList<Integer> up=new ArrayList<>();
    up.add(1);
    up.add(2);
    up.add(3);
    ArrayList<Integer> p=new ArrayList<>();
    List<List<String>> anskk=new ArrayList<List<String>>();
    ArrayList<ArrayList<Integer>> ans=rec(up,p);
    for(ArrayList<Integer> li:ans){
      System.out.println(li);
    }
    String s="abc";
    String unp="";
    ArrayList<String> str=new ArrayList<>();
    str.add(unp);
    while(s.length()!=0){
      ArrayList<String> answer=new ArrayList<>();
       for(String ele:str){
          for(int i=0;i<ele.length()+1;i++){
            StringBuilder sb=new StringBuilder();
            sb.append(ele);
            String tem="";
            tem=tem+s.charAt(0);
            sb.replace(i, i,tem);
            String an=sb.toString();
            answer.add(an);
          }
       }
       str=new ArrayList<>(answer);
       s=s.substring(1, s.length());
    }
    System.out.println(str);

    int[] arr={3,3};
    System.out.println(count("",arr));

    int[][] array={{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}};
    bt("",array,0,0);
    }
      private static ArrayList<ArrayList<Integer>> rec(ArrayList<Integer> up, ArrayList<Integer> p) {
        if(up.size()==0){
          ArrayList<ArrayList<Integer>> list= new ArrayList<ArrayList<Integer>>();
          list.add(p);
          return list;
        }
        ArrayList<Integer> l=new ArrayList<>();
        l.addAll(p);
        l.add(up.get(0));
        ArrayList<ArrayList<Integer>> left= rec(new ArrayList<>(up.subList(1, up.size())),l);
        ArrayList<ArrayList<Integer>> right= rec(new ArrayList<>(up.subList(1, up.size())),p);
        left.addAll(right);
        return left;
      }
      public static ArrayList sum(int n){
    ArrayList<Integer> list=new ArrayList<>();
    if(n==0){
      list.add(0);
      return list;
    }
    list.addAll(sum(n-1));
    list.add(n);
    return list;
}
//maze


public static int count(String p,int[] arr){
  if(arr[0]==1 && arr[1]==1){
    System.out.println(p);
    return 1;
  }
  int down=0;
  int right=0;
  int diag=0;
  if(arr[0]>1 && arr[1]>1){
    diag=count(p+'X',new int[]{arr[0]-1,arr[1]-1});
  }
  if(arr[0]>1){
    down=count(p+'D',new int[]{arr[0]-1,arr[1]});
  }
  if(arr[1]>1){
    right=count(p+'R',new int[]{arr[0],arr[1]-1});
  }
  return down+right+diag;
}
public static void bt(String p,int[][] arr,int row,int n){
  if(row==arr.length){
    System.out.println(p);
    return;
  }
  int o=-1;
  int y=-1;
  for(int i=0;i<arr.length;i++){
    int s=1;
    for(int j=0;j<row;j++){
      if(arr[j][i]==0){
        s=0;
      }
    }
    int k=row-1;
    int l=i-1;
    while(k>=0 && l>=0){
       if(arr[k][l]==0){
        s=0;
       }
       k--;
       l--;
    }
    k=row-1;
    l=i+1;
    while(k>=0 && l<arr[row].length){
      if(arr[k][l]==0){
        s=0;
       }
       k--;
       l++;
    }
    if(s==1){
     arr[row][i]=0;
     bt(p+i,arr,row+1,++n);
     n--;
     arr[row][i]=1;
    // p=p.substring(0,p.length()-1);
    }
  }

}
}

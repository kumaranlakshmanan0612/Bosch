import java.util.Scanner;

public class demo {
  public static void main(String[] args) {
    int[] nums={1,2};
    int ele1=0;
    int ele2=0;
    int c1=0;
    int c2=0;
    for(int i=0;i<nums.length;i++){
        if(c1<=0){
            if(ele2!=nums[i]){
                ele1=nums[i];
                c1=1;
              //  System.out.println("hi"+ele1+c1);
            }else{
            c1=0;
            }
        }else if(ele1==nums[i]){
            c1++;
        }else{
          //System.out.println("no");
          if(ele2!=nums[i]){
            c1--;
            }
        }
       // System.out.println(c1);
        if(c2<=0){
            if(ele1!=nums[i]){
                ele2=nums[i];
                c2=1;
            }   
        }else if(ele2==nums[i]){
            c2++;
        }else{
          if(ele1!=nums[i]){
            c2--;
          }
        }
       // System.out.println("cc"+c1);
        
        }
        System.out.println(ele1+" "+ele2);
        System.out.println(c1+" "+c2);
        int count1=0;
    if(c1>0){
      for(int i=0;i<nums.length;i++){
        if(ele1==nums[i]){
            count1++;
        }
      }
    }
    int count2=0;
    if(c2>0){
      for(int i=0;i<nums.length;i++){
        if(ele2==nums[i]){
            count2++;
        }
      }
    }
  }
}

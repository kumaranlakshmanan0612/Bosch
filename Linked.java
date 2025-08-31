import java.util.Iterator;
import java.util.Scanner;

public class Linked<T> implements Iterable<T>{
  Node head;
  Linked(){
    head=null;
  }
  Linked(T data){
    head.data=data;
    head.next=null;
  }

  public class Node{
    T data;
    Node next;
    Node(T data){
      this.data=data;
      next=null;
    }
  }
  public void insert(T val){
    Node newNode=new Node(val);
    if(head==null){
      head=newNode;
      return;
    }
    Node temp=head;
    while(temp.next!=null){
      temp=temp.next;
    }
    temp.next=newNode;
  }
  public void insertAtBeg(T val){
    Node newNode=new Node(val);
    if(head==null){
      head=newNode;
    }
    else{
      newNode.next=head;
      head=newNode;
    }
  }
  public T valueAt(int pos){
    Node temp=head;
    int count=1;
    while(count!=pos){
      temp=temp.next;
      if(temp==null){
        return null;
      }
      count++;
    }
    return temp.data;
  }
  @Override
  public Iterator<T> iterator() {
    return new CusIterator(this);
  }
  public class CusIterator implements Iterator<T>{
    Linked<T> list;
    int size=1;
    public CusIterator(Linked<T> list){
      this.list=list;
    }

    @Override
    public boolean hasNext() {
      return list.valueAt(size)!=null;
    }

    @Override
    public T next() {
      return list.valueAt(size++);
    }
  }


}

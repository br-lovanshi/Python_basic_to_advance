class Node {
    int data;
    Node next;

    // constructor
    Node(int data){
        this.data = data;
        this.next = null;
    }
    
}

// {data:1,next:02} -> {data:2, next:null}
public class NodeList{
    Node head;

    // add not at the first
    public void addFirst(int data){
        Node temp = new Node(data);
        temp.next = head;
        head = temp;
    }

    // add node at the end
    public void addAtLast(int data){
        Node temp = new Node(data);
        if(head == null){
            head = temp;
            return;
        }
        
        Node curr = head;

        while(curr.next != null){
            curr = curr.next;
        }

        curr.next = temp;
        head = curr;
    }

    // print the list
    public void print(){
        Node curr = head;
        while(curr != null){
            System.out.print(curr.data+ " -> ");
            curr = curr.next;
        }
        System.out.println();
    }

    // find data in list
    public boolean search(int value){

        if(head != null && head.data == value) return true;
        Node curr = head.next;
        while(curr.next != null){
            if(curr.data == value) return true;
            curr = curr.next;
        }

        return false;
    }

    // find length
    public int length(){
        Node curr = head;
        if(head == null) return 0;
        int count = 0;
        while(curr != null){
            count++;
            curr = curr.next;
        }
        return count;
    }

     // reverse list
    // 1 -> 0 -> 2 -> 4 -> 5 ->  1 <- 0 <- 2 <- 4 <- 5
    public Node reverse(){
        Node curr = head;
        Node prev = null;
        while(curr != null){
            Node next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

     public Node findMiddle(){
        if(head == null)return null;
        Node slow = head;
        Node fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public void delete(int value){
        if(head != null && head.data == value){
            head = head.next;
        }

    }


    public static void main(String[] args) {
        NodeList list = new NodeList();
        list.addAtLast(2);
        list.addAtLast(3);
        list.addAtLast(4);
        list.addAtLast(5);
        list.addFirst(0);
        list.print();
        System.out.println("search " + list.search( 1));
        System.out.println("Size "  + list.length());

    }
}
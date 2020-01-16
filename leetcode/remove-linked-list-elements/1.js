function ListNode(val) {
  this.val = val; //值
  this.next = null;
}


const n1 = new ListNode(6);
const n2 = new ListNode(2);
const n3 = new ListNode(6);
const n4 = new ListNode(3);
const n5 = new ListNode(4);
const n6 = new ListNode(5);
const n7 = new ListNode(6);

n1.next = n2;
n2.next = n3;
n3.next = n4;
n4.next = n5;
n5.next = n6;
n6.next = n7;

// 移除结点
function removeElement(head, val) { //head 头结点 val要查验的值
  
  // 哨兵结点
  const dummy = {
    next: head
  }
  let current = dummy
  while (current && current.next) {
    let next = current.next
    if (next.val === val) {
      current.next = next.next
    }
    if (next.val !== val) {
      current = next
    }
  }
  return dummy.next
}

console.log(removeElement(n3, 6))